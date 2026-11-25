# İlerleme günlüğü

Her dersin sonunda bir giriş eklenir. En yeni giriş en altta.
Claude taslağı hazırlar, sen kontrol edip onaylarsın. 3-4 satırı geçmesin.

## Ders girişi şablonu

```
### Ders N — <tarih> — Konu XX: <konu adı>
- Yapılanlar: <bu derste işlenenler / bitenler>
- Önceki ödev: <yapıldı / kısmen / yapılmadı> — <kısa not>
- Verilen ödev: <odevler.md'deki numarası ve bir cümlelik özeti>
```

## Konu bitiş girişi şablonu

```
### ✔ Konu XX tamamlandı — <tarih>
- Mini sınav: <doğru / toplam> — zayıf nokta: <...>
- Anlatma testi: <yeterli / eksik: ...>
- Toplam ders sayısı: <N>
```

---

<!-- Girişler bu çizginin altına eklenir -->

### Ders 1 — 2026-11-11 — Konu 00: Kurulum ve ilk simülasyon
- Yapılanlar: HDL kavramı, AND kapısı doğruluk tablosu, testbench fikri, simülasyon akışı; OSS CAD Suite kuruldu ve doğrulandı.
- Önceki ödev: — (ilk ders)
- Verilen ödev: — (AND kapısını yazmak derse kaldı)

### Ders 2 — 2026-11-25 — Konu 00: Kurulum ve ilk simülasyon
- Yapılanlar: Verilog modül/testbench yazımı (NOT örneği); AND kapısı ve testbench'i yazıldı, GTKWave'de görüldü. Beklenen değer tasarımla aynı formülden hesaplanıyordu, doğruluk tablosuna çevrildi; beş bozuk kapıda test kaldı.
- Önceki ödev: —
- Verilen ödev: Ödev 1 — XOR kapısı + tablodan beklenen değer, 3 soru, simülasyon akışını anlatma.
