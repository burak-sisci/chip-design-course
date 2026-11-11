#!/usr/bin/env python3
"""Koruma kancası: Claude'un rtl/, tb/, sw/ klasörlerine yazmasını ve
git kurallarının çiğnenmesini engeller.

Claude Code bu betiği iki noktada çağırır (bkz. .claude/settings.json):
  pre  -> PreToolUse : komut/düzenleme çalışmadan önce. Çıkış kodu 2 = engelle.
  post -> PostToolUse: Bash/PowerShell komutundan sonra korunan klasörlerde
                       değişiklik var mı diye bakar (bilinmeyen yollara karşı yedek).

Kullanım: python koruma.py pre|post   (girdi: stdin'den kancanın JSON'u)
Testler:  python .claude/hooks/test_koruma.py
"""
import hashlib
import json
import os
import re
import shlex
import sys

KORUNAN = ("rtl", "tb", "sw")
PROJE = os.path.abspath(os.environ.get("CLAUDE_PROJECT_DIR")
                        or os.path.join(os.path.dirname(__file__), "..", ".."))
ANLIK_DIZIN = os.path.join(PROJE, ".claude", "hooks", ".anlik")

# Korunan klasöre işaret eden yol: "rtl/x.v", "./tb", "C:\\...\\sw\\a.c", "rtl" (tek başına)
YOL_RE = re.compile(
    r"""(?:^|[\s"'=(,;:])(?:[^\s"'|;&<>]*[/\\])?(?:rtl|tb|sw)(?:[/\\]|(?=[\s"';|&)<>]|$))""",
    re.IGNORECASE,
)
# Yönlendirme hedefi: > x, >> x, 2> x, &> x, *> x  (>&1 gibi tanıtıcı kopyaları hariç)
YONLENDIRME_RE = re.compile(r"""(?:\d|&|\*)?>{1,2}(?!&)\s*(["']?)([^\s"'|;&<>]+)\1""")

# Argümanlarından biri korunan yolsa yazma sayılan komutlar
YAZAN = {
    # POSIX
    "rm", "rmdir", "mv", "touch", "mkdir", "tee", "truncate", "dd", "chmod",
    "chown", "unlink", "shred", "patch", "unzip", "tar",
    # PowerShell cmdlet ve takma adları
    "set-content", "add-content", "out-file", "new-item", "remove-item",
    "move-item", "rename-item", "clear-content", "set-itemproperty", "ni",
    "ri", "del", "erase", "rd", "sc", "ac", "move", "ren", "md", "mi", "rni",
    "expand-archive", "export-csv", "tee-object",
}
# Yalnızca SON argümanı (hedef) korunan yolsa yazma sayılanlar
HEDEFE_YAZAN = {"cp", "copy", "copy-item", "cpi", "install", "rsync", "ln", "xcopy", "robocopy"}
# Yerinde düzenleme bayrağıyla yazanlar
YERINDE = {"sed": re.compile(r"(^|\s)-[a-zA-Z]*i|--in-place"), "perl": re.compile(r"(^|\s)-[a-zA-Z]*i")}
# Satır içi betik çalıştıranlar
BETIK = {"python", "python3", "py", "node", "perl", "ruby", "powershell", "pwsh", "bash", "sh", "cmd"}
BETIK_YAZMA_RE = re.compile(
    r"open\s*\(|write|unlink|remove|rename|replace|rmtree|copy|move|mkdir|"
    r"set-content|out-file|add-content|new-item|remove-item|>",
    re.IGNORECASE,
)
# Çalışma ağacının tamamını ezebilen git alt komutları (yol verilmese de)
GIT_TUMUNU_EZER = [
    re.compile(r"\breset\b.*--(hard|merge|keep)"),
    re.compile(r"\bclean\b"),
    re.compile(r"\bstash\b(?!\s+(list|show)\b)"),
    re.compile(r"\bcheckout\b.*(\s--\s|\s\.(\s|$)|\s-f\b|--force)"),
    re.compile(r"\brestore\b"),
    re.compile(r"\bcheckout-index\b"),
    re.compile(r"\bread-tree\b.*-u"),
]
GIT_YOLLA_YAZAN = {"checkout", "restore", "rm", "mv", "apply", "am", "switch", "merge", "pull", "rebase", "cherry-pick", "revert"}

ONEK = {"sudo", "env", "command", "builtin", "exec", "nohup", "time", "&", "."}


def korunan_yol_mu(yol: str) -> bool:
    """Bir dosya yolu proje içindeki rtl/, tb/ veya sw/ altında mı?"""
    if not yol:
        return False
    yol = yol.strip("\"'")
    # Git Bash yolu: /c/Users/... -> C:/Users/...
    m = re.match(r"^/([a-zA-Z])/(.*)", yol)
    if m and os.name == "nt":
        yol = f"{m.group(1)}:/{m.group(2)}"
    tam = os.path.abspath(yol if os.path.isabs(yol) else os.path.join(PROJE, yol))
    try:
        goreli = os.path.relpath(tam, PROJE)
    except ValueError:  # farklı sürücü
        return False
    if goreli.startswith(".."):
        return False
    ilk = goreli.replace("\\", "/").split("/")[0].lower()
    return ilk in KORUNAN


def parcalara_ayir(komut: str):
    """Komutu ; && || | ve satır sonlarından parçalara böler."""
    return [p.strip() for p in re.split(r"&&|\|\||[;\n|]", komut) if p.strip()]


def sozcukler(parca: str):
    # posix=False: Windows yollarındaki ters eğik çizgiler korunur
    try:
        soz = shlex.split(parca, posix=False)
    except ValueError:
        soz = parca.split()
    return [w.strip("\"'") for w in soz]


def komut_adi(soz):
    i = 0
    while i < len(soz) and (soz[i].lower() in ONEK or re.match(r"^\w+=", soz[i])):
        i += 1
    if i >= len(soz):
        return "", []
    ad = os.path.basename(soz[i].replace("\\", "/")).lower()
    ad = re.sub(r"\.exe$", "", ad)
    return ad, soz[i + 1:]


def yazma_nedeni(komut: str):
    """Komut korunan klasörlere yazıyorsa nedenini, yazmıyorsa None döndürür."""
    korunan_icinde = False  # cd rtl gibi bir komuttan sonra
    for parca in parcalara_ayir(komut):
        soz = sozcukler(parca)
        ad, arg = komut_adi(soz)
        yol_var = korunan_icinde or bool(YOL_RE.search(parca))

        if ad in {"cd", "pushd", "set-location", "sl", "chdir"} and arg and korunan_yol_mu(arg[-1]):
            korunan_icinde = True
            continue

        for _, hedef in YONLENDIRME_RE.findall(parca):
            if hedef.lower() in {"/dev/null", "nul", "$null"}:
                continue
            if korunan_yol_mu(hedef) or (korunan_icinde and not os.path.isabs(hedef)):
                return f"yönlendirme ({hedef}) korunan klasöre yazıyor"

        if ad in YAZAN and yol_var:
            return f"'{ad}' korunan klasördeki bir yolu değiştiriyor"
        if ad in HEDEFE_YAZAN:
            hedefler = [a for a in arg if not a.startswith("-")]
            if hedefler and (korunan_yol_mu(hedefler[-1]) or (korunan_icinde and not os.path.isabs(hedefler[-1]))):
                return f"'{ad}' korunan klasöre kopyalıyor"
        if ad in YERINDE and YERINDE[ad].search(parca) and yol_var:
            return f"'{ad} -i' korunan klasördeki dosyayı yerinde değiştiriyor"
        if ad in BETIK and yol_var and BETIK_YAZMA_RE.search(parca):
            return f"'{ad}' betiği korunan klasöre yazıyor olabilir"
        if ad == "git" and arg:
            alt = " ".join(arg)
            for desen in GIT_TUMUNU_EZER:
                if desen.search(alt):
                    return "bu git komutu çalışma ağacındaki (rtl/tb/sw dahil) değişiklikleri ezebilir"
            if arg[0].lower() in GIT_YOLLA_YAZAN and yol_var:
                return f"'git {arg[0]}' korunan klasördeki dosyaları değiştiriyor"
    return None


def git_ihlali(komut: str):
    """Git ve GitHub kurallarına aykırılık varsa nedenini döndürür."""
    for parca in parcalara_ayir(komut):
        soz = sozcukler(parca)
        ad, arg = komut_adi(soz)
        if ad != "git" or not arg:
            continue
        alt = " ".join(arg).lower()
        if re.search(r"co-authored-by", komut, re.IGNORECASE) and "commit" in alt:
            return "commit'e ortak yazar eklenemez; yazar yalnızca öğrenci"
        if re.search(r"\bcommit\b", alt) and re.search(r"--author\b", alt):
            return "commit'te --author kullanılamaz; öğrencinin git kimliği kullanılır"
        if re.search(r"\bconfig\b", alt) and re.search(r"\buser\.(name|email)\b", alt) and len(
            [a for a in arg if not a.startswith("-")]) >= 3:
            return "git kimliği (user.name / user.email) değiştirilemez"
        if re.search(r"\bpush\b", alt) and re.search(r"(^|\s)(-f|--force|--force-with-lease|--mirror|--delete|-d)(\s|=|$)|\s\+\S", " " + alt):
            return "zorla push / dal silme yasak"
        if re.search(r"--no-verify\b", alt):
            return "--no-verify yasak"
        if re.search(r"\b(filter-branch|filter-repo)\b", alt) or re.search(r"\bcommit\b.*--amend", alt) and re.search(r"\bpush\b", komut.lower()):
            return "geçmişi yeniden yazmak yasak"
    return None


# ---- PostToolUse yedek denetimi: korunan klasörlerin parmak izi ----

def parmak_izi():
    iz = {}
    for k in KORUNAN:
        kok = os.path.join(PROJE, k)
        for dizin, _, dosyalar in os.walk(kok):
            for d in dosyalar:
                p = os.path.join(dizin, d)
                try:
                    s = os.stat(p)
                except OSError:
                    continue
                iz[os.path.relpath(p, PROJE).replace("\\", "/")] = f"{s.st_size}:{s.st_mtime_ns}"
    return iz


def anlik_dosyasi(veri):
    anahtar = veri.get("tool_use_id") or hashlib.sha1(
        json.dumps(veri.get("tool_input", {}), sort_keys=True).encode()).hexdigest()
    return os.path.join(ANLIK_DIZIN, re.sub(r"[^\w-]", "_", anahtar) + ".json")


def engelle(neden: str):
    print(f"KORUMA KANCASI ENGELLEDİ: {neden}. Bkz. CLAUDE.md 'Kod yazma kuralları' "
          f"ve 'Git ve GitHub kuralları'. Bu kuralı atlatmaya çalışma; gerekiyorsa öğrenciye sor.",
          file=sys.stderr)
    sys.exit(2)


def main():
    for akis in (sys.stdout, sys.stderr):
        try:
            akis.reconfigure(encoding="utf-8")
        except Exception:
            pass
    asama = sys.argv[1] if len(sys.argv) > 1 else "pre"
    try:
        veri = json.loads(sys.stdin.buffer.read().decode("utf-8"))
    except Exception:
        sys.exit(0)
    arac = veri.get("tool_name", "")
    girdi = veri.get("tool_input", {}) or {}

    if asama == "pre":
        if arac in {"Edit", "Write", "MultiEdit", "NotebookEdit"}:
            yol = girdi.get("file_path") or girdi.get("notebook_path") or ""
            if korunan_yol_mu(yol):
                engelle(f"{yol} öğrencinin kod klasöründe (rtl/tb/sw)")
        elif arac in {"Bash", "PowerShell"}:
            komut = girdi.get("command", "")
            neden = yazma_nedeni(komut) or git_ihlali(komut)
            if neden:
                engelle(neden)
            os.makedirs(ANLIK_DIZIN, exist_ok=True)
            with open(anlik_dosyasi(veri), "w", encoding="utf-8") as f:
                json.dump(parmak_izi(), f)
        sys.exit(0)

    if asama == "post" and arac in {"Bash", "PowerShell"}:
        yol = anlik_dosyasi(veri)
        if not os.path.exists(yol):
            sys.exit(0)
        with open(yol, encoding="utf-8") as f:
            once = json.load(f)
        os.remove(yol)
        sonra = parmak_izi()
        degisen = sorted(k for k in set(once) | set(sonra) if once.get(k) != sonra.get(k))
        if degisen:
            print("KORUMA KANCASI UYARISI: Bu komut çalışırken korunan klasörlerde değişiklik oldu: "
                  + ", ".join(degisen[:10])
                  + ". Öğrenci o sırada kendisi düzenlemediyse bu bir kural ihlalidir. "
                  "Dosyaları geri almaya çalışma; durumu hemen öğrenciye bildir.",
                  file=sys.stderr)
            sys.exit(2)
    sys.exit(0)


if __name__ == "__main__":
    main()
