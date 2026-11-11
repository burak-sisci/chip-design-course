# Kaynaklar

Öncelik Türkçe kaynaklarda. İngilizce olanlar **(İng.)** ile işaretli ve sadece kısa başvuru için.

## Ana kaynaklar (Türkçe)

| Kısaltma | Kaynak | Ne için? | Erişim |
|---|---|---|---|
| **KS** | *Kapıdan Silikona* — Mehmet Burak Aykenar'ın 5 YouTube serisinin (132 video) konuya göre düzenlenmiş derlemesi | Programın omurgası. Her bölüm bir veya birkaç videoya karşılık gelir. | [leanpub.com/fromgatestosilicons](https://leanpub.com/fromgatestosilicons) ve Aykenar'ın YouTube kanalı |
| **Mano** | M. Morris Mano, *Sayısal Tasarım* (Türkçe çeviri) | Lojik devre teorisi, alıştırmalar | Kütüphane / kitapçı |
| **Kelleci** | Burak Kelleci, *VHDL ve Verilog ile Sayısal Tasarım* (Seçkin Yayıncılık) | Verilog dili ve Vivado uygulamaları | Kitapçı |
| **TÜTEL** | TÜBİTAK BİLGEM TÜTEL YouTube eğitimleri (2022-2023 yarışma eğitimleri) | Yarışmayı tanıma, OpenLane akışı | [YouTube oynatma listeleri](https://www.youtube.com/@tutel.bilgem.tubitak/playlists) |
| **BTK** | BTK Akademi – STM32 ile Gömülü Yazılım Geliştirme | Çevre birimlerini kullanıcı gözüyle tanıma (isteğe bağlı) | [btkakademi.gov.tr](https://www.btkakademi.gov.tr/portal/course/stm32-ile-gomulu-yazilim-gelistirme-35649) |

## Kapıdan Silikona bölüm haritası

Bu iki tablo `docs/mufredat.md`'den üretildi. Müfredatta bir konunun kaynağı değişirse bu tablolar da güncellenir.

### Konuya göre: hangi konuda hangi bölümler okunacak?

| Konu | Başlık | KS bölümleri | Kısım |
|---|---|---|---|
| 0 | Kurulum ve ilk simülasyon | B5–B6 | I |
| 1 | Sayı sistemleri, Boole cebri, kapılar | B1–B3, B6 | I |
| 2 | Sadeleştirme ve kombinasyonel yapı taşları | B4, B8 | I |
| 3 | Aritmetik devreler ve ALU | B7, B9, B53 | I, III |
| 4 | Latch, flip-flop, register | B10, B50 | I, III |
| 5 | Sayaçlar ve sonlu durum makineleri (FSM) | B11–B13, B51 | I, III |
| 6 | Zamanlama analizi ve senkronizasyon | B16–B17, B52 | I, III |
| 7 | Veri yolu + kontrol ayrımı ve bellek | B14–B15, B19–B20 | I |
| 8 | Verilog'u sağlamlaştırma ve SystemVerilog | B49 | III |
| T1 | Modül 1 tekrarı | — | — |
| 9 | Bilgisayar mimarisine giriş ve RISC-V komut kümesi | B42, B46–B48, B57–B59 | III |
| 10 | Sözde komutlar, prosedürler, yığıt, C ile ilişki | B60–B61 | III |
| 11 | Tek çevrimli işlemci (1): veri yolu | B63–B64 | III |
| 12 | Tek çevrimli işlemci (2): program çalıştırma | B65 | III |
| 13 | Boru hattı, tehlikeler ve çekirdek seçimi | B66–B67 | III |
| 14 | Bellek hiyerarşisi, kesmeler, mikrodenetleyici mimarisi | B68–B69, B72 | III |
| T2 | Modül 2 tekrarı | — | — |
| 15 | SoC mimarisi ve tasarım planı | B39, B80, B82 | II, IV |
| 16 | Bus protokolü ve GPIO | B80, B82 | IV |
| 17 | Çekirdek entegrasyonu ve boot | B84, B86 | IV |
| 18 | UART | B31 | II |
| 19 | Timer, PWM ve kesme | B72 | III |
| 20 | SPI ve I2C | B35 | II |
| 21 | Doğrulama sistematiği | B27, B30, B32 | II |
| 22 | FPGA prototipleme | B5, B36–B38 | I, II |
| 23 | Demo ve performans ölçümü | — | — |
| T3 | Modül 3 tekrarı | — | — |
| 24 | ASIC akışına giriş | B93–B100 | V |
| 25 | Fiziksel tasarım adımları ve raporlar | B101–B109 | V |
| 26 | Tam akış ve sonuçların toplanması | — | — |
| 27 | Yarışma raporları ve sunum | — | — |

### Kısıma göre: her kısım hangi konularda kullanılıyor?

| Kısım | Bölümler | Seri | Kullanıldığı konular | Müfredatta kullanılmayan bölümler (isteğe bağlı) |
|---|---|---|---|---|
| I – Mantıksal Devre Tasarımı | 1–23 | Mantıksal Devre Tasarımı (Verilog) | 0, 1, 2, 3, 4, 5, 6, 7, 22 | B18, B21–B23 |
| II – VHDL ile FPGA Programlama | 24–41 | VHDL ile FPGA Programlama | 15, 18, 20, 21, 22 | B24–B26, B28–B29, B33–B34, B40–B41 |
| III – Bilgisayar Mimarisi | 42–73 | Bilgisayar Mimarisi (RISC-V) | 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 19 | B43–B45, B54–B56, B62, B70–B71, B73 |
| IV – ZYNQ SoC Tasarımı | 74–92 | ZYNQ SoC HW/SW Tasarımı | 15, 16, 17 | B74–B79, B81, B83, B85, B87–B92 |
| V – Çip Tasarımı | 93–112 | Çip Tasarımı (OpenLane, SKY130) | 24, 25 | B110–B112 |

**Dikkat edilmesi gereken iki nokta:**
- **Kısım III'ün bir bölümü Modül 1'de kullanılıyor.** Bilgisayar Mimarisi serisinin B49–B53 bölümleri Verilog ile kombinasyonel ve ardışıl devreleri, zamanlama analizini ve toplayıcıları anlatır. Bu yüzden Konu 3, 4, 5, 6 ve 8'de, Kısım I'deki ilgili bölümlerin tamamlayıcısı olarak geçiyor.
- **Kısım II VHDL kullanır.** Bu kısımdaki bölümleri kavramlar (UART, CDC, zamanlama, doğrulama) için izle, dil olarak Verilog'da kal.

## Yarışma kaynakları

| Kaynak | Not |
|---|---|
| TEKNOFEST Çip Tasarım Yarışması sayfası | [teknofest.org](https://www.teknofest.org/en/competitions/chip-design-competition) — şartname, takvim, geçmiş dereceler |
| TÜTEL GitHub | [github.com/TUTEL-TUBITAK](https://github.com/TUTEL-TUBITAK) — 2022-2024 yarışma dosyaları |
| Geçmiş finalist raporları | TEKNOFEST sitesindeki takım sayfaları |
| Yarışma mail grubu | Şartnamede olmayan sorular için resmi kanal |

## Araçlar

| Araç | Ne için? |
|---|---|
| OSS CAD Suite | Icarus Verilog, Yosys, GTKWave, Verilator — tek paket |
| Ripes | RISC-V assembly ve boru hattı görselleştirme |
| RISC-V GCC | C programlarını çekirdek için derleme |
| cocotb | Python ile testbench |
| OpenLane | RTL → GDS fiziksel tasarım akışı (Konu 24'te kurulacak) |
| HDLBits **(İng.)** | Tarayıcıda Verilog alıştırmaları; metinler kısa, kod evrensel |

## İngilizce başvuru kaynakları (sadece gerektiğinde)

| Kaynak | Ne zaman? |
|---|---|
| RISC-V komut kümesi spesifikasyonu **(İng.)** | Komut ayrıntısı gerektiğinde (Konu 9-14) |
| Seçilen çekirdeğin dokümanı **(İng.)** | Konu 13'ten itibaren |
| Wishbone / AXI4-Lite spesifikasyonu **(İng.)** | Sadece sinyal tabloları (Konu 16) |
| cocotb dokümantasyonu **(İng.)** | Konu 16, 21 |
| OpenLane dokümantasyonu **(İng.)** | Konu 24-26 |

Bu kaynakları okurken Claude'dan ilgili kısmın Türkçe özetini iste.
