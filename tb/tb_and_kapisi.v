`timescale 1ns/1ps

module tb_and_kapisi;
    reg  a;              // testbench'in sürdüğü giriş
    reg  b;              // testbench'in sürdüğü giriş
    wire y;              // DUT'un sürdüğü çıkış
    integer hata = 0;    // bulunan hata sayısı

    // DUT'u bağla
    and_kapisi dut (.a(a), .b(b), .y(y));

    // Verilen (va, vb) girişini uygular, beklenen değeri (va & vb) hesaplar ve karşılaştırır
    task dene;
        input va;
        input vb;
        input beklenen;      // artık dışarıdan, tablodan gelir
        begin
            a = va;
            b = vb;
            #10;
            if (y !== beklenen) begin
                $display("HATA: a=%b b=%b -> y=%b (beklenen %b)", va, vb, y, beklenen);
                hata = hata + 1;
            end else begin
                $display("OK:   a=%b b=%b -> y=%b", va, vb, y);
            end
        end
    endtask


    initial begin
        $dumpfile("sim_build/dalga.vcd");
        $dumpvars(0, tb_and_kapisi);

        dene(0, 0, 0);
        dene(0, 1, 0);
        dene(1, 0, 0);
        dene(1, 1, 1);

        if (hata == 0) $display("TEST GECTI");
        else           $display("TEST KALDI: %0d hata", hata);
        $finish;
    end
endmodule