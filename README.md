# Çip Tasarımı Çalışma Reposu

TEKNOFEST Çip Tasarım Yarışması, **Mikrodenetleyici Tasarım** kategorisi için sıfırdan hazırlık.
Program **zamandan bağımsızdır**: konular sırayla ilerler, hız sana bağlıdır.
Claude Code ile çalışılır. Kodu öğrenci yazar; Claude öğretir, inceler ve simülasyonla doğrular.

## Nereden başlamalı?

1. `docs/mufredat.md` — Sıralı konu listesi (Konu 0 – Konu 27). Her konu: ana fikir, önkoşul, konular, kaynaklar, bitiş ölçütü. Bu dosya sadece plandır; işaretleme yapılmaz.
2. `CLAUDE.md` — Claude'un bu repoda uyduğu ders kuralları.
3. `docs/cizim_rehberi.md` — Devreler, FSM'ler ve zamanlama nasıl çizilecek.
4. `docs/kaynaklar.md` — Türkçe kaynaklar ve bölüm haritası.

## Bir ders nasıl geçer?

Claude Code'a doğrudan yaz. Örneğin:

- **"Derse başlayalım"** → Önceki ödev kontrol edilir, kaldığımız yerden devam edilir.
- Ders sırasında → Konu çizimlerle anlatılır, sen kodunu yazarsın, "incele" dersin, takılınca ipucu istersin.
- **"Dersi bitirelim"** → Bir sonraki derse kadar yapacağın **ödev** verilir, ders özeti günlüğe eklenir.

Bir konuya başlarken o konunun klasörü açılır ve bitiş ölçütleri klasördeki `durum.md`'ye kopyalanır. İlerledikçe kutular orada işaretlenir. Hepsi işaretlenince notsuz bir mini sınav ve anlatma testi yapılır, sonra sıradaki konuya geçilir.

**Nerede ne tutuluyor?**
- Plan: `docs/mufredat.md` (değişmez)
- Konunun durumu: `konular/konu-XX-<ad>/durum.md`
- Ders ders kayıt: `docs/ilerleme_gunlugu.md`

## Klasörler

| Klasör | İçerik | Kim yazar? |
|---|---|---|
| `docs/` | Müfredat, günlük, hata defteri, kaynaklar, şartname | İkimiz (Claude taslak, öğrenci onay) |
| `konular/konu-XX-<ad>/` | Konunun durumu, notları, ödevleri, sınavı, anlatma değerlendirmesi | İkimiz |
| `rtl/` | Verilog/SystemVerilog tasarım dosyaları | **Sadece öğrenci** |
| `tb/` | Testbench'ler (Verilog ve cocotb) | **Sadece öğrenci** |
| `sw/` | Gömülü C kodu, linker script | **Sadece öğrenci** |
| `cizimler/` | Diyagramlar, HTML anlatım sayfaları | Claude |
| `araclar/` | Yardımcı betikler | Claude |

`rtl/`, `tb/` ve `sw/` klasörleri Claude'a kapalıdır: `.claude/settings.json`'daki kurallar ve `.claude/hooks/koruma.py` kancası, düzenleme araçlarıyla da kabuk komutlarıyla da bu klasörlere yazmayı engeller.

## GitHub

Repo: [github.com/burak-sisci/chip-design-course](https://github.com/burak-sisci/chip-design-course) (public). Her dersin sonunda Claude o dersin değişikliklerini commit edip push eder. Commit'lerin yazarı yalnızca öğrencidir; Claude ortak yazar olarak eklenmez. Şartname PDF'i repoya yüklenmez (bkz. `docs/sartname/README.md`).
