#!/usr/bin/env python3
"""koruma.py için testler. Çalıştır: python .claude/hooks/test_koruma.py
Her satır: (araç, girdi, engellenmeli_mi). Kancayı gerçek süreç olarak çağırır."""
import json
import os
import subprocess
import sys

BURASI = os.path.dirname(os.path.abspath(__file__))
PROJE = os.path.abspath(os.path.join(BURASI, "..", ".."))
KANCA = os.path.join(BURASI, "koruma.py")
P = PROJE.replace("\\", "/")

DURUMLAR = [
    # --- Düzenleme araçları ---
    ("Write", {"file_path": f"{PROJE}\\rtl\\alu.v"}, True),
    ("Edit", {"file_path": f"{P}/tb/tb_alu.v"}, True),
    ("Write", {"file_path": "sw/main.c"}, True),
    ("NotebookEdit", {"notebook_path": f"{PROJE}\\sw\\x.ipynb"}, True),
    ("Write", {"file_path": f"{PROJE}\\docs\\notlar.md"}, False),
    ("Write", {"file_path": f"{PROJE}\\konular\\konu-03-alu\\rtl_notu.md"}, False),
    ("Write", {"file_path": f"{PROJE}\\cizimler\\tb_dalga.html"}, False),
    # --- Bash: yazma ---
    ("Bash", {"command": "echo x > rtl/alu.v"}, True),
    ("Bash", {"command": "cat a >> tb/tb.v"}, True),
    ("Bash", {"command": f"echo x > {P}/rtl/a.v"}, True),
    ("Bash", {"command": "echo x > /c/Users/burak/Desktop/chip-design-course/sw/a.c"}, True),
    ("Bash", {"command": "cp /tmp/a.v rtl/"}, True),
    ("Bash", {"command": "mv rtl/a.v rtl/b.v"}, True),
    ("Bash", {"command": "rm -rf sw"}, True),
    ("Bash", {"command": "sed -i 's/a/b/' rtl/alu.v"}, True),
    ("Bash", {"command": "echo hi | tee tb/out.txt"}, True),
    ("Bash", {"command": "touch rtl/yeni.v"}, True),
    ("Bash", {"command": "cd rtl && echo x > a.v"}, True),
    ("Bash", {"command": "python -c \"open('rtl/a.v','w').write('x')\""}, True),
    ("Bash", {"command": "iverilog -o rtl/sim.vvp rtl/a.v"}, False),  # -o hedefi: aşağıda ayrıca
    ("Bash", {"command": "git checkout -- rtl/alu.v"}, True),
    ("Bash", {"command": "git restore tb/tb.v"}, True),
    ("Bash", {"command": "git reset --hard HEAD"}, True),
    ("Bash", {"command": "git clean -fd"}, True),
    ("Bash", {"command": "git stash"}, True),
    ("Bash", {"command": "git checkout ."}, True),
    # --- Bash: okuma / izinli ---
    ("Bash", {"command": "cat rtl/alu.v"}, False),
    ("Bash", {"command": "iverilog -g2012 -o sim_build/alu.vvp rtl/alu.v tb/tb_alu.v 2>&1"}, False),
    ("Bash", {"command": "vvp sim_build/alu.vvp > sim_build/log.txt"}, False),
    ("Bash", {"command": "verilator --lint-only -Wall rtl/alu.v 2>&1 | head -50"}, False),
    ("Bash", {"command": "./araclar/sema.sh rtl/alu.v alu"}, False),
    ("Bash", {"command": "cp rtl/alu.v /tmp/yedek.v"}, False),
    ("Bash", {"command": "grep -n always rtl/*.v"}, False),
    ("Bash", {"command": "ls tb sw rtl"}, False),
    ("Bash", {"command": "echo x > docs/a.md"}, False),
    ("Bash", {"command": "git add -A && git status"}, False),
    ("Bash", {"command": "git stash list"}, False),
    ("Bash", {"command": "git diff rtl/"}, False),
    # --- Git kuralları ---
    ("Bash", {"command": "git commit -m 'Ders 1: Konu 0'"}, False),
    ("Bash", {"command": "git push -u origin main"}, False),
    ("Bash", {"command": "git config user.name"}, False),
    ("Bash", {"command": "git commit -m 'x\n\nCo-Authored-By: Claude <noreply@anthropic.com>'"}, True),
    ("Bash", {"command": "git commit --author='Claude <c@a.com>' -m x"}, True),
    ("Bash", {"command": "git config user.email claude@anthropic.com"}, True),
    ("Bash", {"command": "git config --global user.name Claude"}, True),
    ("Bash", {"command": "git push --force origin main"}, True),
    ("Bash", {"command": "git push -f"}, True),
    ("Bash", {"command": "git push origin +main"}, True),
    ("Bash", {"command": "git commit --no-verify -m x"}, True),
    # --- PowerShell ---
    ("PowerShell", {"command": "Set-Content -Path rtl\\alu.v -Value x"}, True),
    ("PowerShell", {"command": "'x' | Out-File tb\\a.v"}, True),
    ("PowerShell", {"command": "Remove-Item -Recurse sw"}, True),
    ("PowerShell", {"command": "Copy-Item C:\\tmp\\a.v rtl\\a.v"}, True),
    ("PowerShell", {"command": "Get-Content rtl\\alu.v"}, False),
    ("PowerShell", {"command": "Set-Content -Path docs\\a.md -Value x"}, False),
]


def calistir(arac, girdi, asama="pre"):
    veri = {"tool_name": arac, "tool_input": girdi, "tool_use_id": "test"}
    r = subprocess.run([sys.executable, KANCA, asama], input=json.dumps(veri),
                       capture_output=True, text=True, encoding="utf-8",
                       env={**os.environ, "CLAUDE_PROJECT_DIR": PROJE, "PYTHONIOENCODING": "utf-8"})
    return r.returncode


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    hatalar = 0
    for arac, girdi, beklenen in DURUMLAR:
        kod = calistir(arac, girdi)
        if arac in {"Bash", "PowerShell"}:
            calistir(arac, girdi, "post")  # anlık kaydı temizle
        engellendi = kod == 2
        if engellendi != beklenen:
            hatalar += 1
            print(f"HATA  beklenen={'ENGEL' if beklenen else 'İZİN'}  {arac}: {girdi}")
    # Son denetim: geçici bir projede rtl/ altına komut sırasında dosya yazılırsa uyarmalı
    import tempfile
    with tempfile.TemporaryDirectory() as gecici:
        os.makedirs(os.path.join(gecici, "rtl"))
        ortam = {**os.environ, "CLAUDE_PROJECT_DIR": gecici, "PYTHONIOENCODING": "utf-8"}
        veri = json.dumps({"tool_name": "Bash", "tool_input": {"command": "make"}, "tool_use_id": "t2"})
        def kos(a):
            return subprocess.run([sys.executable, KANCA, a], input=veri, capture_output=True,
                                  text=True, encoding="utf-8", env=ortam).returncode
        sessiz = (kos("pre"), kos("post"))
        kos("pre")
        open(os.path.join(gecici, "rtl", "gizli.v"), "w").close()
        uyari = kos("post")
        if sessiz != (0, 0) or uyari != 2:
            hatalar += 1
            print(f"HATA  son denetim: degisiklik yokken={sessiz}, degisiklik varken={uyari}")
    print(f"{len(DURUMLAR) + 1 - hatalar}/{len(DURUMLAR) + 1} durum doğru")
    sys.exit(1 if hatalar else 0)


if __name__ == "__main__":
    main()
