# Müfredat: Sıfırdan Mikrodenetleyici Tasarımı

Hedef: TEKNOFEST Çip Tasarım Yarışması, Mikrodenetleyici Tasarım kategorisi.

Bu müfredat **zamandan bağımsızdır**. Sadece konuların sırası vardır. Vaktin olduğunda çok, olmadığında az ilerlersin. Hangi yılın yarışmasına katılacağına konulardaki ilerlemene göre karar verirsin (bkz. sondaki "Yarışma kontrol noktaları").

---

## Temel kavramlar

- **Konu:** Müfredattaki bir öğrenme birimi (aşağıda Konu 0 – Konu 27). Bir konu bir ya da birkaç derste biter.
- **Ders:** Claude ile yaptığın her çalışma oturumu. Süresi serbest: 30 dakika da olabilir, 4 saat de.
- **Ödev:** Her dersin sonunda Claude bir sonraki derse kadar yapacağın ödevi verir. Bir sonraki ders bu ödevin kontrolüyle başlar.
- **Konu sonu değerlendirmesi:** Bir konu bittiğinde notsuz bir mini sınav ve anlatma testi yapılır. Geçince sıradaki konuya geçilir.
- **Plan ve durum ayrı tutulur:** Bu dosya sadece plandır ve değişmez. Hangi konunun neresinde olduğun konunun klasöründeki `durum.md`'de, ders ders ne yapıldığı `docs/ilerleme_gunlugu.md`'de tutulur.

## Her konu nasıl okunur?

- **Ana fikir:** Bu konunun programdaki yeri ve neden önemli olduğu. Önce bunu oku.
- **Önkoşul:** Bu konuya başlamadan bitmiş olması gereken konular.
- **Konular:** Öğrenilecek başlıklar.
- **Kaynaklar:** Kısaltmalar:
  - **KS-B12** = *Kapıdan Silikona*, Bölüm 12 (Aykenar'ın ilgili YouTube dersine karşılık gelir)
  - **Mano** = M. Morris Mano, *Sayısal Tasarım* (Türkçe çeviri). Baskıya göre bölüm numarası değişebilir, konu başlığına göre bul.
  - **Kelleci** = Burak Kelleci, *VHDL ve Verilog ile Sayısal Tasarım*
  - **TÜTEL** = TÜTEL YouTube kanalındaki yarışma eğitimleri
  - **(İng.)** = Türkçe karşılığı olmayan, sadece kısa başvuru için İngilizce kaynak
- **Konu bitti sayılır eğer:** Elinde olması gereken somut, ölçülebilir çıktılar. Bu liste plandır; burada işaretlenmez. Konuya başlarken konunun klasöründeki `durum.md` dosyasına kopyalanır ve işaretleme orada yapılır.
- **Ödev fikirleri:** Claude'un ders sonunda verebileceği ödevler için örnekler. Claude ödevi o dersin içeriğine göre seçer.
- **Tahmini emek:** Kabaca kaç saatlik çalışma gerektirdiği. Takvim değil, sadece fikir vermek için.

## Sıralama kuralı

Konular sırayla ilerler, çünkü her konu bir öncekinin üzerine kurulur. İki istisna:
- **Konu 21 (Doğrulama)** ve **gömülü C** kısımları SoC konularıyla (16-20) birlikte, paralel yürür.
- **Tekrar konuları (T1, T2, T3)** atlanmaz. Bir modülün bilgisi oturmadan sonrakine geçilmez.

---

## Genel bakış

| Modül | Konular | Sonunda elinde ne olacak? | Tahmini emek |
|---|---|---|---|
| 0 – Hazırlık | 0 | Çalışan simülasyon ortamı | ~8 saat |
| 1 – Sayısal tasarımın temelleri | 1-8, T1 | Verilog ile yazılmış ve test edilmiş ALU, register file, FSM, bellek | ~110 saat |
| 2 – Mimari ve RISC-V | 9-14, T2 | RISC-V'yi anlama, kendi tek çevrimli işlemcin | ~80 saat |
| 3 – SoC tasarımı | 15-23, T3 | Çekirdek + bus + bellek + çevre birimleri, C programı çalışıyor, FPGA'de demo | ~120 saat |
| 4 – ASIC ve raporlar | 24-27 | GDS çıktısı, sonuç tabloları, yarışma raporları | ~50 saat |

Toplam kabaca 350-400 saat. Haftada 12 saatle ~8 ay, 6 saatle ~15 ay demek. Bu sadece bir fikir; ilerleme hızın kendi ritmine göre değişecek.

---

# MODÜL 0 — HAZIRLIK

## Konu 0 — Kurulum ve ilk simülasyon
**Önkoşul:** Yok · **Tahmini emek:** ~8 saat

**Ana fikir:** Bir devreyi tasarlamak için önce onu çalıştırıp görebileceğin bir ortam gerekir. Bu konuda, yazdığın her şeyin dalga formunu görebileceğin düzeni kuruyoruz.

**Konular**
- Araçların kurulumu (birlikte): Git, VS Code, Claude Code masaüstü uygulaması, OSS CAD Suite (Icarus Verilog, Yosys, GTKWave, Verilator), Python, Node.js
- GitHub reposunu tanıma (repo hazır: [burak-sisci/chip-design-course](https://github.com/burak-sisci/chip-design-course)); commit, push ve ders sonu akışının nasıl işlediği
- İlk Verilog modülü: tek bir AND kapısı
- Testbench nedir, neden tasarımla aynı anda yazılır?
- Simülasyon akışı: `iverilog` ile derle → `vvp` ile çalıştır → `.vcd` dosyasını GTKWave'de aç
- Çizim araçlarını deneme (bkz. `docs/cizim_rehberi.md`)

**Kaynaklar:** KS-B5 (sadece giriş kısmı), KS-B6'nın ilk yarısı; TÜTEL – Sayısal Tümdevre Tasarımı Eğitimi 1. kısım (yarışmayı tanımak için)

**Konu bitti sayılır eğer**
- `rtl/and_kapisi.v` ve `tb/tb_and_kapisi.v` senin yazdığın dosyalar olarak repoda
- GTKWave'de dört giriş kombinasyonunu gösteren dalga formu
- AND kapısı dosyaları GitHub'da; commit yazarı olarak sadece senin adın var

**Ödev fikirleri:** OR, XOR ve NOT kapılarını aynı yöntemle yazıp simüle etmek.

---

# MODÜL 1 — SAYISAL TASARIMIN TEMELLERİ

## Konu 1 — Sayı sistemleri, Boole cebri, kapılar
**Önkoşul:** Konu 0 · **Tahmini emek:** ~12 saat

**Ana fikir:** Bilgisayar her şeyi 0 ve 1 ile temsil eder. Negatif sayıların nasıl tutulduğunu (ikinin tümleyeni) anlamadan ALU'yu, Boole cebrini anlamadan devre sadeleştirmeyi anlayamazsın.

**Konular**
- İkilik, sekizlik, onaltılık sistemler; taban dönüşümleri
- İşaretli sayılar: işaret-büyüklük, birin tümleyeni, ikinin tümleyeni ve neden ikinin tümleyeni kazandı
- Taşma (overflow) ve elde (carry) farkı
- Boole cebri: aksiyomlar, De Morgan, sadeleştirme
- Kapılar: AND, OR, NOT, NAND, NOR, XOR, XNOR; NAND'ın evrensel kapı olması
- Doğruluk tablosundan ifadeye: çarpımların toplamı (SOP), toplamların çarpımı (POS)
- Verilog: kapı seviyesi (gate-level) modelleme, modül hiyerarşisi
- Transistörün anahtar olarak çalışması ve CMOS kapının mantığı (sadece kavramsal)

**Kaynaklar:** KS-B1, KS-B2, KS-B3, KS-B6; Mano – İkili sistemler ve Boole cebri bölümleri

**Konu bitti sayılır eğer**
- Verilen 3 Boole fonksiyonunun kapı seviyesinde Verilog modülleri
- Her biri için tüm giriş kombinasyonlarını deneyen ve sonucu kendisi kontrol eden testbench
- Bir fonksiyonun kapı şeması (netlistsvg veya schemdraw ile)

**Ödev fikirleri:** XOR'u yalnızca NAND kapılarıyla kurmak; taban dönüşümü ve ikinin tümleyeni alıştırmaları.

---

## Konu 2 — Sadeleştirme ve kombinasyonel yapı taşları
**Önkoşul:** Konu 1 · **Tahmini emek:** ~12 saat

**Ana fikir:** Gerçek tasarımlar tek tek kapılardan değil, MUX ve kod çözücü gibi hazır yapı taşlarından kurulur. İşlemcide her seçim bir MUX, her adres çözümü bir kod çözücüdür.

**Konular**
- Karnaugh haritası (2, 3, 4 değişken), önemsiz (don't care) durumlar
- Çoğullayıcı (MUX), çoğullama çözücü (DEMUX)
- Kod çözücü (decoder), kodlayıcı (encoder), öncelikli kodlayıcı
- Karşılaştırıcı
- Verilog: dataflow modelleme (`assign`), koşullu operatör, vektörler, birleştirme `{}`
- Verilog'da `x` ve `z` değerleri

**Kaynaklar:** KS-B4, KS-B8; Mano – Kapı seviyesinde sadeleştirme ve kombinasyonel devreler

**Konu bitti sayılır eğer**
- Parametrik genişlikte 4:1 MUX, 3:8 decoder, 8:3 öncelikli kodlayıcı ve kendini kontrol eden testbench'leri
- Bir K-map sadeleştirmesinin elle çözümü ve simülasyonla doğrulanması

**Ödev fikirleri:** 7 segment gösterge kod çözücüsü; MUX ile Boole fonksiyonu gerçekleme.

---

## Konu 3 — Aritmetik devreler ve ALU
**Önkoşul:** Konu 2 · **Tahmini emek:** ~15 saat

**Ana fikir:** ALU işlemcinin hesap yapan kalbidir. RISC-V'nin toplama, çıkarma, mantık ve kaydırma komutlarının hepsi bu konuda.

**Konular**
- Yarım ve tam toplayıcı; ripple-carry toplayıcı ve gecikme sorunu
- Carry-lookahead toplayıcının ana fikri
- İkinin tümleyeni ile çıkarma; taşma algılama
- Kaydırıcı: mantıksal ve aritmetik kaydırma
- ALU tasarımı: işlem seçme, bayraklar (sıfır, negatif, taşma)
- Verilog: behavioral modelleme, `always @(*)`, `case`, istenmeyen latch oluşumu
- Testbench: rastgele test ve testbench içinde referans model

**Kaynaklar:** KS-B7, KS-B9, KS-B53; Mano – Kombinasyonel devrelerin aritmetik kısmı

**Konu bitti sayılır eğer**
- 32 bitlik ALU: ADD, SUB, AND, OR, XOR, SLT, SLTU, SLL, SRL, SRA
- En az 1000 rastgele girişle ALU'yu referans modelle karşılaştıran testbench
- ALU blok diyagramı (Mermaid)

**Ödev fikirleri:** 4 bitlik carry-lookahead toplayıcı ve ripple-carry ile karşılaştırma (Yosys `stat` ile kapı sayısı).

---

## Konu 4 — Latch, flip-flop, register
**Önkoşul:** Konu 3 · **Tahmini emek:** ~12 saat

**Ana fikir:** Şimdiye kadarki devreler hafızasızdı. Flip-flop ile devre hatırlamaya başlar. İşlemcinin register'ları, sayaçları, durum makineleri hep bunun üzerine kurulur.

**Konular**
- Latch ve flip-flop farkı; neden tasarımda latch'ten kaçınırız
- D flip-flop, saat kenarı, senkron ve asenkron reset
- Register, enable'lı register
- Verilog: `always @(posedge clk)`, **blocking (`=`) ve non-blocking (`<=`) farkı**
- Register file: çok portlu okuma, tek portlu yazma
- Testbench'te saat üretimi

**Kaynaklar:** KS-B10, KS-B50; Mano – Senkron ardışıl devreler bölümünün başı

**Konu bitti sayılır eğer**
- 32×32 bitlik register file: 2 okuma, 1 yazma portu, x0 her zaman 0 (RISC-V kuralı)
- Register file testbench'i: yazma-okuma, x0'a yazma denemesi, aynı anda okuma-yazma
- Blocking ve non-blocking farkını gösteren iki devrenin dalga formu karşılaştırması

**Ödev fikirleri:** 8 bitlik shift register; blocking/non-blocking çıktı tahmini soruları.

---

## Konu 5 — Sayaçlar ve sonlu durum makineleri (FSM)
**Önkoşul:** Konu 4 · **Tahmini emek:** ~15 saat

**Ana fikir:** UART, SPI, I2C gibi çevre birimlerinin hepsi aslında bir FSM'dir. İşlemcinin kontrol birimi de bir FSM'dir. Yarışmada en çok kullanacağın tasarım kalıbı bu.

**Konular**
- Sayaçlar: yukarı/aşağı, modulo-N, saat bölücü
- FSM: Moore ve Mealy farkı, durum diyagramı, durum tablosu
- Durum kodlama: ikili, one-hot
- Üç bloklu FSM şablonu (durum register'ı, sonraki durum mantığı, çıkış mantığı)
- Durum diyagramını Mermaid ile çizme

**Kaynaklar:** KS-B11, KS-B12, KS-B13, KS-B51; Mano – Register ve sayaçlar

**Konu bitti sayılır eğer**
- Trafik ışığı FSM'i: durum diyagramı + Verilog + testbench
- 50 MHz saatten 115200 Hz darbe üreten "baud tick" sayacı (UART'a hazırlık)
- "1011" desen algılayıcı: hem Moore hem Mealy sürümü

**Ödev fikirleri:** Buton titreşimi giderici (debouncer).

---

## Konu 6 — Zamanlama analizi ve senkronizasyon
**Önkoşul:** Konu 5 · **Tahmini emek:** ~10 saat

**Ana fikir:** Devren simülasyonda doğru çalışabilir ama gerçek çipte belirli bir hızın üstünde çalışmaz. Raporda "tasarımımız X MHz'te çalışır" diyebilmek için bu konu şart.

**Konular**
- Yayılım gecikmesi, kritik yol, maksimum saat frekansı
- Setup ve hold zamanı; ihlal olursa ne olur
- Metastabilite ve iki flip-floplu senkronizatör (CDC'ye giriş)
- Yosys ile sentez: `stat` komutu, netlistsvg ile kendi ALU'nun şeması

**Kaynaklar:** KS-B16, KS-B52 (KS-B17 Vivado uygulaması, sadece izle)

**Konu bitti sayılır eğer**
- Verilen bir devre için elle kritik yol ve maksimum frekans hesabı
- İki flip-floplu senkronizatör ve testbench'i
- Kendi ALU'nun Yosys `stat` çıktısı ve şeması

**Ödev fikirleri:** Asenkron buton girişini senkronize edip debouncer'a bağlamak.

---

## Konu 7 — Veri yolu + kontrol ayrımı ve bellek
**Önkoşul:** Konu 6 · **Tahmini emek:** ~12 saat

**Ana fikir:** İşlemci, veri yolu (datapath) ve onu yöneten kontrol biriminin birleşimidir. Bu ayrımı küçük bir örnekte kuruyorsun ve belleği Verilog'da modellemeyi öğreniyorsun.

**Konular**
- ASM/ASMD diyagramları; datapath ve controller ayrımı
- Boru hattının ana fikri (sadece sezgi)
- RAM ve ROM modelleme, senkron okuma, `$readmemh` ile dosyadan yükleme
- Adres genişliği, bayt ve kelime adresleme

**Kaynaklar:** KS-B14, KS-B15, KS-B19, KS-B20; Mano – Bellek ve RTL tasarım bölümleri

**Konu bitti sayılır eğer**
- ASMD ile tasarlanmış ardışık çarpıcı: datapath ve kontrol FSM'i ayrı modüller
- `$readmemh` ile yüklenen 1 KB ROM ve 1 KB RAM modülü + testbench

**Ödev fikirleri:** Bayt yazma maskeli (byte enable) 32 bitlik RAM.

---

## Konu 8 — Verilog'u sağlamlaştırma ve SystemVerilog
**Önkoşul:** Konu 7 · **Tahmini emek:** ~12 saat

**Ana fikir:** Mimari konulara geçmeden önce kod kalitesini oturtuyoruz. Temiz, okunabilir ve lint uyarısız RTL, raporda ve jüri karşısında ciddi fark yaratır.

**Konular**
- Parametreler, `generate`, `localparam`
- Sentezlenebilir ve sentezlenemez yapılar
- `verilator --lint-only` uyarılarını anlama ve temizleme
- SystemVerilog kolaylıkları: `logic`, `always_ff`, `always_comb`, `enum`, `typedef`, `struct`
- Kodlama kuralları: isimlendirme, reset stratejisi, tek saat alanı
- Makefile ile simülasyonu tek komuta bağlama

**Kaynaklar:** Kelleci – Verilog bölümleri; KS-B49

**Konu bitti sayılır eğer**
- Önceki tüm modüller lint uyarısız
- Register file ve FSM'in SystemVerilog sürümleri
- `docs/kodlama_kurallari.md`: kendi yazdığın kodlama kuralları
- `make sim MODUL=alu` gibi tek komutla simülasyon

**Ödev fikirleri:** Parametrik FIFO (UART'ta kullanılacak).

---

## Konu T1 — Modül 1 tekrarı
**Önkoşul:** Konu 8 · **Tahmini emek:** ~6 saat

**Ana fikir:** Modül 2'deki işlemci tasarımı Modül 1'in her konusunu kullanır. Burada eksik kalan bir şey ileride çok daha pahalıya patlar.

**Konular**
- Hata defterindeki açık maddelerin her biri için kısa alıştırma
- **Boş sayfa testi:** Notlara bakmadan register file ve bir FSM'i sıfırdan yeniden yazmak
- Modül 1 kapsamlı mini sınavı

**Konu bitti sayılır eğer**
- Boş sayfa testi başarılı
- Modül sınavında hata defterinden gelen soruların çoğu doğru

---

# MODÜL 2 — MİMARİ VE RISC-V

## Konu 9 — Bilgisayar mimarisine giriş ve RISC-V komut kümesi
**Önkoşul:** T1 · **Tahmini emek:** ~12 saat

**Ana fikir:** Mikrodenetleyicinin çekirdeği RISC-V komutlarını çalıştırır. Hazır bir çekirdek kullansan bile hangi komutu nasıl çalıştırdığını bilmeden onu SoC'a bağlayamaz, hata ayıklayamazsın.

**Konular**
- Bilgisayarın katmanları: yazılım, ISA, mikromimari, devre
- Başarım denklemi: yürütme zamanı = komut sayısı × CPI × saat periyodu
- ISA kavramı; RISC ve CISC
- RV32I: 32 register, komut formatları (R, I, S, B, U, J), anlık değer kodlama
- RISC-V araç zinciri ve Ripes simülatörü kurulumu

**Kaynaklar:** KS-B42, KS-B46, KS-B47, KS-B48, KS-B57, KS-B58, KS-B59

**Konu bitti sayılır eğer**
- Ripes'ta kendi yazdığın 5 assembly programı: toplam, dizideki en büyük eleman, Fibonacci, bellek kopyalama, döngüyle çarpma
- 10 komutun makine kodunu elle çözme ve Ripes ile doğrulama

**Ödev fikirleri:** Komut formatlarının kendi özet tablosu.

---

## Konu 10 — Sözde komutlar, prosedürler, yığıt, C ile ilişki
**Önkoşul:** Konu 9 · **Tahmini emek:** ~10 saat

**Ana fikir:** Yarışmada çekirdeğe C programı yükleyeceksin. Derleyicinin C'yi nasıl assembly'ye çevirdiğini, fonksiyon çağrılarının yığıtı nasıl kullandığını bilmezsen boot kodunu ve linker script'i anlayamazsın.

**Konular**
- Sözde komutlar (`li`, `mv`, `call`, `ret`)
- Fonksiyon çağırma kuralları (ABI)
- Yığıt ve bellek düzeni: `.text`, `.data`, `.bss`, yığıt, heap
- `riscv32-unknown-elf-gcc -S` ile C'den assembly üretme; `objdump` ile inceleme

**Kaynaklar:** KS-B60, KS-B61

**Konu bitti sayılır eğer**
- Özyinelemeli bir C fonksiyonunun derlenmiş assembly'sinin satır satır açıklaması
- Kendi ABI register tablon

**Ödev fikirleri:** Assembly'de dizi sıralayan fonksiyon ve onu çağıran ana program.

---

## Konu 11 — Tek çevrimli işlemci (1): veri yolu
**Önkoşul:** Konu 10 · **Tahmini emek:** ~15 saat

**Ana fikir:** Hazır çekirdeği gerçekten anlamanın en iyi yolu küçüğünü kendin kurmaktır. ALU ve register file'ını birleştirip bir işlemcinin veri yolunu oluşturuyorsun.

**Konular**
- Tek çevrimli RV32I veri yolu: PC, komut belleği, register file, ALU, veri belleği
- Anlık değer üreteci, dallanma birimi, sonraki PC hesabı
- Ana kontrol birimi ve ALU kontrolü

**Kaynaklar:** KS-B63, KS-B64

**Konu bitti sayılır eğer**
- Anlık değer üreteci, dallanma birimi ve kontrol birimi, her biri testbench'iyle
- Veri yolunun Mermaid blok diyagramı

**Ödev fikirleri:** Veri yolunun üst modülünün bağlantıları.

---

## Konu 12 — Tek çevrimli işlemci (2): program çalıştırma
**Önkoşul:** Konu 11 · **Tahmini emek:** ~15 saat

**Ana fikir:** İlk kez kendi tasarladığın bir donanım, derleyicinin ürettiği bir programı çalıştıracak. Programın en önemli kilometre taşlarından biri.

**Konular**
- Entegrasyon ve hata ayıklama
- Programı hex dosyasına çevirip komut belleğine yükleme
- Her komut için küçük test programları
- Çok çevrimli işlemcinin ana fikri

**Kaynaklar:** KS-B65

**Konu bitti sayılır eğer**
- Tek çevrimli RV32I alt kümesi (R, I, load/store, branch, `jal`, `jalr`, `lui`) Konu 9'daki programları çalıştırıyor
- Program sonucu testbench tarafından otomatik kontrol ediliyor

**Ödev fikirleri:** Eksik komutları tamamlamak; bulduğun bir hatanın hikayesini yazmak.

---

## Konu 13 — Boru hattı, tehlikeler ve çekirdek seçimi
**Önkoşul:** Konu 12 · **Tahmini emek:** ~12 saat

**Ana fikir:** Hazır çekirdeklerin çoğu boru hatlıdır. Neden hızlı olduğunu ve hangi sorunları getirdiğini bilmek, çekirdeği seçerken ve performansı raporlarken gerekli.

**Konular**
- 5 aşamalı boru hattı ve boru hattı diyagramı
- Veri tehlikesi (forwarding, stall), kontrol tehlikesi (flush)
- CPI'nin boru hattında nasıl değiştiği
- **Hazır çekirdek araştırması:** Şartname belirli bir çekirdek veriyorsa onu, vermiyorsa PicoRV32, Ibex, SERV gibi seçenekleri karşılaştırma

**Kaynaklar:** KS-B66, KS-B67; çekirdeklerin dokümanları (İng.)

**Konu bitti sayılır eğer**
- Verilen bir kod parçası için boru hattı diyagramı ve tehlike analizi
- `docs/cekirdek_secimi.md`: karşılaştırma ve gerekçeli seçim (**senin yazdığın**)

**Ödev fikirleri:** Seçilen çekirdeğin portlarını ve bellek arayüzünü açıklamak.

---

## Konu 14 — Bellek hiyerarşisi, kesmeler, mikrodenetleyici mimarisi
**Önkoşul:** Konu 13 · **Tahmini emek:** ~10 saat

**Ana fikir:** İşlemciden mikrodenetleyiciye geçiyoruz. Bir mikrodenetleyiciyi işlemciden ayıran şey çevre birimleri, bellek düzeni ve kesmelerdir.

**Konular**
- Bellek hiyerarşisi ve önbelleğin ana fikri
- Mikrodenetleyici ile mikroişlemci farkı; SoC kavramı
- RISC-V istisna ve kesme mekanizması: `mtvec`, `mepc`, `mcause`, `mstatus`, `mie`
- Bellek eşlemeli giriş/çıkış (memory-mapped I/O)
- (İsteğe bağlı) BTK – STM32 Temel: çevre birimini kullanıcı gözüyle görmek için ilk bölümler

**Kaynaklar:** KS-B68, KS-B69, KS-B72

**Konu bitti sayılır eğer**
- Seçilen çekirdeğin bus arayüzü ve kesme girişlerini gösteren blok diyagramı
- Bir kesmenin baştan sona akış diyagramı (çevre birimi → çekirdek → ISR → dönüş)

**Ödev fikirleri:** SoC'un ilk bellek haritası taslağı.

---

## Konu T2 — Modül 2 tekrarı
**Önkoşul:** Konu 14 · **Tahmini emek:** ~6 saat

**Konular**
- Hata defterindeki açık maddeler
- **Boş sayfa testi:** Bir komutun tek çevrimli veri yolundaki yolunu notsuz çizmek; bir assembly fonksiyonunu notsuz yazmak
- Modül 2 kapsamlı mini sınavı

**Konu bitti sayılır eğer**
- Boş sayfa testi başarılı
- Modül sınavı başarılı

---

# MODÜL 3 — SoC TASARIMI

Bu modülde her yeni modül için **cocotb testleri** de yazılır (doğrulama paralel yürür). Gömülü C kodu Konu 17'den itibaren her konuya eklenir.

## Konu 15 — SoC mimarisi ve tasarım planı
**Önkoşul:** T2 · **Tahmini emek:** ~12 saat

**Ana fikir:** Kod yazmaya başlamadan önce ne tasarlayacağını, nasıl doğrulayacağını yazıya dökmek. Bu, yarışmanın Ön Tasarım Raporu'nun (ÖTR) da özüdür. Yarışma döneminde değilsen bu doküman kendi tasarım planın olur.

**Konular**
- Şartnameyi satır satır okuma ve gereksinim listesi çıkarma
- Bus seçimi (Wishbone, APB, AXI4-Lite) ve gerekçesi
- Bellek haritası, çevre birimleri listesi, kesme planı
- Doğrulama planı taslağı
- Geçmiş yılların ÖTR örneklerini inceleme

**Kaynaklar:** KS-B39, KS-B80, KS-B82; TÜTEL yarışma eğitimleri; şartname

**Konu bitti sayılır eğer**
- `docs/tasarim_plani.md`: mimari, bellek haritası, blok diyagramları, doğrulama planı
- Planın bir insan tarafından okunması (hoca, danışman veya geçmiş yarışmacı)

**Ödev fikirleri:** Gelen geri bildirimlere göre düzeltme; planı 5 dakikada anlatma provası.

---

## Konu 16 — Bus protokolü ve GPIO
**Önkoşul:** Konu 15 · **Tahmini emek:** ~15 saat

**Ana fikir:** Bus, SoC'un sinir sistemidir. Bir kez doğru bus slave'i yazabilirsen her yeni çevre birimi aynı şablonu tekrarlar.

**Konular**
- Seçilen bus'ın sinyalleri ve el sıkışma (handshake) mantığı
- Master, slave, adres çözücü, interconnect
- Bellek eşlemeli register bloğu: okuma-yazma, salt okunur, yazınca temizlenen register'lar
- Bus fonksiyonel modeli (BFM)
- cocotb'ye giriş: Python ile test yazmak

**Kaynaklar:** KS-B80, KS-B82 (AXI ile, kavramlar aynı); bus spesifikasyonu (İng., sadece sinyal tablosu)

**Konu bitti sayılır eğer**
- GPIO çevre birimi: yön, çıkış ve giriş register'ları + bus slave arayüzü
- GPIO'yu bus üzerinden test eden cocotb testi
- Bus el sıkışmasının WaveDrom zamanlama diyagramı

**Ödev fikirleri:** Adres çözücü ve 2 slave'li küçük interconnect.

---

## Konu 17 — Çekirdek entegrasyonu ve boot
**Önkoşul:** Konu 16 · **Tahmini emek:** ~15 saat

**Ana fikir:** Tüm parçalar ilk kez birleşiyor: çekirdek, bellek ve GPIO. Ve ilk kez kendi derlediğin C programı kendi SoC'unda çalışıyor.

**Konular**
- Çekirdeği, ROM'u ve RAM'i bus'a bağlama
- Reset vektörü ve boot süreci
- Linker script; başlangıç kodu (crt0)
- C'den hex dosyasına: derleme → `objcopy` → `$readmemh`
- Bare-metal C ile register erişimi: `volatile` ve pointer

**Kaynaklar:** KS-B84, KS-B86

**Konu bitti sayılır eğer**
- Simülasyonda C programı GPIO çıkışında desen üretiyor
- `sw/` altında linker script, crt0 ve GPIO sürücüsü (**senin yazdığın**)

**Ödev fikirleri:** GPIO girişini okuyup çıkışa yansıtan C programı.

---

## Konu 18 — UART
**Önkoşul:** Konu 17 · **Tahmini emek:** ~15 saat

**Ana fikir:** UART, mikrodenetleyicinin dış dünyayla konuştuğu en temel yol. Hem hata ayıklamada hem demoda en çok kullanacağın çevre birimi.

**Konular**
- UART çerçevesi: başlangıç, veri, eşlik, bitiş bitleri
- TX ve RX FSM'leri; alıcıda örnekleme (oversampling)
- Baud hızı üretimi (Konu 5'teki sayaç) ve FIFO (Konu 8'deki FIFO)
- UART register haritası ve C sürücüsü

**Kaynaklar:** KS-B31 (VHDL ile, mantık aynı)

**Konu bitti sayılır eğer**
- UART çevre birimi (TX + RX + FIFO + bus arayüzü) ve cocotb testi
- Simülasyonda C programı UART'tan "Merhaba" basıyor

**Ödev fikirleri:** Gelen karakteri geri gönderen (echo) program.

---

## Konu 19 — Timer, PWM ve kesme
**Önkoşul:** Konu 18 · **Tahmini emek:** ~12 saat

**Ana fikir:** Gerçek mikrodenetleyici programları kesmelerle çalışır. Timer kesmesi, işlemcinin beklemeden zamanı takip etmesini sağlar.

**Konular**
- Timer: sayaç, karşılaştırma register'ı, kesme üretimi
- PWM: görev oranı ve kullanım alanları
- Kesme denetleyicisi (çekirdeğe göre: basit IRQ hattı veya CLINT/PLIC mantığı)
- C'de kesme servis rutini (ISR), `mtvec` ayarı

**Kaynaklar:** KS-B72 (tekrar); çekirdeğin kesme dokümanı (İng.)

**Konu bitti sayılır eğer**
- Timer + PWM çevre birimi ve cocotb testleri
- Simülasyonda timer kesmesiyle periyodik GPIO değiştiren C programı

**Ödev fikirleri:** PWM ile LED parlaklığı değiştiren program.

---

## Konu 20 — SPI ve I2C
**Önkoşul:** Konu 19 · **Tahmini emek:** ~12 saat

**Ana fikir:** Sensörler ve harici bellekler genellikle SPI veya I2C ile bağlanır. Şartname hangilerini istiyorsa ona öncelik ver.

**Konular**
- SPI: master, saat polaritesi ve fazı (mod 0-3)
- I2C: açık-drenaj hat, başlangıç/bitiş koşulu, adresleme, ACK
- Her biri için FSM ve register haritası

**Kaynaklar:** KS-B35

**Konu bitti sayılır eğer**
- SPI master çevre birimi ve cocotb testi
- I2C master (şartname istiyorsa) veya FSM tasarım dokümanı

**Ödev fikirleri:** SPI üzerinden harici bellek modeline yazıp okuyan C programı.

---

## Konu 21 — Doğrulama sistematiği
**Önkoşul:** Konu 20 (Konu 16'dan beri paralel yürüyor) · **Tahmini emek:** ~12 saat

**Ana fikir:** Jürinin her raporda sorduğu soru: "Bunu nasıl doğruladınız?" Dağınık testleri sistematik bir doğrulama ortamına dönüştürüyorsun.

**Konular**
- Doğrulama planı: özellik listesi, test listesi, kapsama hedefleri
- Yönlendirilmiş ve kısıtlı rastgele test
- Kod kapsaması ve fonksiyonel kapsama
- SystemVerilog Assertions (SVA) ile temel kontroller
- Çekirdek uyumluluk testleri (riscv-tests veya riscv-arch-test)
- GitHub Actions ile her commit'te testlerin çalışması

**Kaynaklar:** KS-B27, KS-B30, KS-B32; cocotb dokümantasyonu (İng.)

**Konu bitti sayılır eğer**
- `docs/dogrulama_plani.md` (**senin yazdığın**)
- Tüm testler tek komutla çalışıyor ve GitHub Actions'ta yeşil
- Kapsama raporu

**Ödev fikirleri:** Kapsamanın en düşük olduğu modül için ek testler.

---

## Konu 22 — FPGA prototipleme
**Önkoşul:** Konu 21 · **Tahmini emek:** ~12 saat

**Ana fikir:** Mikrodenetleyici kategorisinde finalde demo yapılıyor. Tasarımının gerçek donanımda çalıştığını göstermenin yolu FPGA.

**Konular**
- FPGA iç yapısı: LUT, flip-flop, blok RAM, DSP, saat kaynakları
- Araç akışı (kartına göre Vivado veya Yosys + nextpnr)
- Pin ve zamanlama kısıtları; zamanlama raporu okuma
- PLL ile saat üretimi; saat alanları arası geçiş (CDC)

**Kaynaklar:** KS-B5 (tekrar), KS-B36, KS-B37, KS-B38; Kelleci – Vivado uygulamaları

**Konu bitti sayılır eğer**
- SoC FPGA için sentezlendi, zamanlama raporu temiz
- Kartta GPIO ve UART çalışıyor

**Not:** FPGA kartın yoksa Verilator ile hızlı simülasyon yapılır ve kart temini bu konuya gelmeden planlanır.

**Ödev fikirleri:** UART'ın kartta bilgisayarla konuşması.

---

## Konu 23 — Demo ve performans ölçümü
**Önkoşul:** Konu 22 · **Tahmini emek:** ~8 saat

**Ana fikir:** Demo, jüriye birkaç dakikada "tasarımımız çalışıyor" demenin yolu. İyi bir demo önceden planlanır ve prova edilir.

**Konular**
- Kart üzerinde hata ayıklama: dahili mantık analizörü (ILA) veya UART konsolu
- Demo senaryosu: hangi program, hangi çevre birimleri
- Performans: saat frekansı, kaynak kullanımı (LUT, FF, BRAM)

**Konu bitti sayılır eğer**
- UART konsolundan komut alıp çevre birimlerini kullanan demo programı
- FPGA kaynak kullanımı ve frekans tablosu
- 1-2 dakikalık demo videosu

---

## Konu T3 — Modül 3 tekrarı
**Önkoşul:** Konu 23 · **Tahmini emek:** ~6 saat

**Konular**
- Hata defterindeki açık maddeler
- **Boş sayfa testi:** Notsuz bir bus slave register bloğu yazmak; reset'ten `main`'e kadar olanları notsuz anlatmak
- Modül 3 kapsamlı mini sınavı

**Konu bitti sayılır eğer**
- Boş sayfa testi başarılı: notsuz yazılan bus slave register bloğu testbench'i geçiyor
- Reset'ten `main`'e kadar olan akış notsuz ve eksiksiz anlatıldı
- Modül 3 sınavında hata defterinden gelen soruların çoğu doğru

---

# MODÜL 4 — ASIC VE RAPORLAR

## Konu 24 — ASIC akışına giriş
**Önkoşul:** T3 · **Tahmini emek:** ~10 saat

**Ana fikir:** "Çip tasarımı"nı "FPGA projesi"nden ayıran şey fiziksel tasarımdır. RTL'in nasıl gerçek bir çip çizimine (GDS) dönüştüğünü küçük bir modülle görüyorsun.

**Konular**
- ASIC ile FPGA farkı; standart hücre, PDK (SKY130)
- Açık kaynak akış: Yosys, OpenROAD, OpenLane; yarışmanın sağladığı akışa uyum
- OpenLane kurulumu (WSL2/Docker, birlikte kurulacak)
- Küçük bir modülü (ALU) akıştan geçirme

**Kaynaklar:** KS-B93 – KS-B100; TÜTEL – OpenLane demosu

**Konu bitti sayılır eğer**
- ALU'nun GDS çıktısı ve KLayout'ta görüntüsü
- Akışın her adımını anlatan kendi notun

---

## Konu 25 — Fiziksel tasarım adımları ve raporlar
**Önkoşul:** Konu 24 · **Tahmini emek:** ~12 saat

**Ana fikir:** Akışı çalıştırmak kolay, raporlarını okumak zordur. Zamanlama, alan ve güç sonuçlarını yorumlayabilmek gerekiyor.

**Konular**
- Sentez raporu, STA, SDC kısıtları, setup/hold ihlallerini düzeltme
- Floorplan, yerleştirme, saat ağacı sentezi (CTS), yönlendirme
- Sign-off: DRC ve LVS
- Bellek makroları (SRAM) ve I/O

**Kaynaklar:** KS-B101 – KS-B109

**Konu bitti sayılır eğer**
- SoC'un bir alt modülü (ör. UART) temiz DRC/LVS ile GDS
- Zamanlama, alan ve güç sonuçlarının yorumlu tablosu

---

## Konu 26 — Tam akış ve sonuçların toplanması
**Önkoşul:** Konu 25 · **Tahmini emek:** ~12 saat

**Ana fikir:** Şartnamenin istediği kapsamda fiziksel tasarım ve rapora girecek tüm sonuçların tek yerde toplanması.

**Konular**
- Şartnamenin istediği kapsamda (tüm SoC veya belirli bölüm) fiziksel tasarım
- Tüm testlerin son kez çalıştırılması
- Sonuç tabloları: test özeti, kapsama, FPGA kaynakları, ASIC alan/frekans/güç

**Konu bitti sayılır eğer**
- Rapora girecek tüm şekil ve tablolar `docs/raporlar/sekiller/` altında
- Tasarım kodu etiketlendi (`git tag v1.0`)

---

## Konu 27 — Yarışma raporları ve sunum
**Önkoşul:** ÖTR kısmı için Konu 15, DTR ve sunum kısmı için Konu 26 · **Tahmini emek:** rapora göre

**Ana fikir:** Yarışmada değerlendirilen şey yaptığın iş kadar onu nasıl anlattığındır.

Bu konu iki parçada işlenir. ÖTR kısmı Konu 15'ten hemen sonra, DTR ve sunum kısmı Konu 26'dan sonra yapılır. Yarışmaya katılmadığın bir dönemde bu konu atlanabilir; tasarım planı ve sonuç tabloları zaten Konu 15 ve 26'da hazırlanmış olur.

**Konular**
- ÖTR: `docs/tasarim_plani.md` üzerinden, şartnamenin rapor şablonuna göre
- DTR: ÖTR'den bu yana değişenler, detaylı mimari, doğrulama, FPGA ve ASIC sonuçları
- Final sunumu ve soru-cevap provası
- Her raporun teslimden önce bir insan tarafından okunması

**Konu bitti sayılır eğer**

*ÖTR kısmı*
- ÖTR şartnamenin rapor şablonuna ve sayfa sınırına uygun
- ÖTR teslimden önce bir insan tarafından okundu ve geri bildirimler işlendi
- ÖTR zamanında teslim edildi, PDF'i `docs/raporlar/` altında

*DTR ve sunum kısmı*
- DTR şartnamenin rapor şablonuna uygun ve Konu 26'daki tüm sonuç tablolarını içeriyor
- DTR teslimden önce bir insan tarafından okundu
- DTR zamanında teslim edildi, PDF'i `docs/raporlar/` altında
- Final sunumu (finale kalınırsa) en az iki kez prova edildi, olası jüri soruları için cevap listesi hazır

---

## Yarışma kontrol noktaları

Program bir yarışma yılına bağlı değil. Belirli bir yılın yarışmasına katılmak istediğinde Claude'a sor; ilerlemene ve kalan konulara bakıp yetişip yetişemeyeceğini birlikte hesaplarız.

**Sıradaki yarışma TEKNOFEST 2027.** 2027 takvimi henüz açıklanmadı. Aşağıdaki tarihler 2026 yarışmasında gerçekleşen tarihlerdir ve 2027 için sadece tahmin olarak kullanılmalıdır. Kesin tarihler için [yarışma sayfasını](https://www.teknofest.org/en/competitions/chip-design-competition) kontrol et; 2027 şartnamesi çıkınca bu tablo güncellenecek.

| Yarışma adımı | 2026'da gerçekleşen | 2027 için tahmin | O tarihte nerede olmalısın? |
|---|---|---|---|
| Başvuru | 15 Ocak – 28 Şubat | Ocak – Şubat 2027 | En az Konu 8 bitmiş; takım ve danışman belli |
| Ön Tasarım Raporu (ÖTR) | 16 Mart | Mart 2027 ortası | Konu 15 ve Konu 27'nin ÖTR kısmı bitmiş |
| Detay Tasarım Raporu (DTR) | 15 Haziran | Haziran 2027 ortası | Konu 26 ve Konu 27'nin DTR kısmı bitmiş |
| Finalist açıklanması, final | Temmuz – Eylül | Temmuz – Eylül 2027 | Konu 27'nin sunum kısmı |

**Bir uyarı:** ÖTR ile DTR arası yaklaşık 3 ay. Bu sürede Konu 16-26 bitmeli (~150 saat, haftada ~12 saat). Bu yüzden bir yılın yarışmasına girmeye karar verdiğinde ÖTR'ye Konu 15'i bitirmiş olarak girmek yetmez; mümkünse Konu 16-17'ye de başlamış olmak iyi olur.
