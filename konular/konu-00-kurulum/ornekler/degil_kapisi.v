// Öğretim örneği: NOT (DEĞİL) kapısı.
// Ödevin çözümü değildir; AND kapısını sen yazacaksın.
`timescale 1ns/1ps

module degil_kapisi (
    input  wire a,   // giriş pini
    output wire y    // çıkış pini
);
    assign y = ~a;   // y kablosu her an a'nın tersine bağlı
endmodule
