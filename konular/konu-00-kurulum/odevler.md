# Konu 0 — Ödevler

Her dersin sonunda Claude buraya yeni bir ödev ekler. Bir sonraki dersin başında kontrol edilir.

---

## Ödev 1 — 2026-11-25

**Görev:**
1. `tb/tb_and_kapisi.v` 12. satırdaki eski açıklamayı koda uygun hâle getir.
2. XOR kapısını yaz: `rtl/xor_kapisi.v` ve `tb/tb_xor_kapisi.v`. Beklenen değerler testbench'e doğruluk tablosundan yazılsın (`^` işareti testbench'te kullanılmasın).

**Bitti sayılır eğer:**
- [ ] `tb_xor_kapisi` simülasyonda `TEST GECTI` yazıyor
- [ ] Testbench'te `^` yok; beklenen değerler sabit sayı olarak verilmiş
- [ ] `tb_and_kapisi.v`'deki açıklama satırı kodla uyumlu

**Notsuz sorular:**
1. `assign y = a & b;` satırındaki `assign` neden "bir kez atama" değil de "sürekli bağlantı" anlamına gelir? Bir lehim benzetmesiyle anlat.
2. Testbench'te girişler neden `reg`, çıkış neden `wire`?
3. *(Hata defterinden)* Testbench beklenen değeri tasarımla aynı formülle hesaplarsa hangi hatayı asla yakalayamaz? Bir örnek ver.

**Cevaplarım:**
1.
2.
3.

**Anlatma görevi:** Simülasyon akışını (`iverilog` → `vvp` → `dalga.vcd` → GTKWave) baştan sona, her adımın neden var olduğunu söyleyerek anlat.

**Kontrol sonucu (Claude doldurur):** <geçti / eksik: ...>

---
