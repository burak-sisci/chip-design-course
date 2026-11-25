// Öğretim örneği: degil_kapisi için testbench.
`timescale 1ns/1ps

module tb_degil_kapisi;
    reg  a;              // testbench'in sürdüğü giriş: değeri biz atarız
    wire y;              // DUT'un sürdüğü çıkış: biz sadece okuruz
    integer hata = 0;    // bulunan hata sayısı

    // DUT'u "sokete tak": pinleri adıyla bağla
    degil_kapisi dut (.a(a), .y(y));

    initial begin
        $dumpfile("sim_build/dalga_degil.vcd");
        $dumpvars(0, tb_degil_kapisi);

        a = 0; #10;
        if (y !== 1'b1) begin $display("HATA: a=0 iken y=%b", y); hata = hata + 1; end

        a = 1; #10;
        if (y !== 1'b0) begin $display("HATA: a=1 iken y=%b", y); hata = hata + 1; end

        if (hata == 0) $display("TEST GECTI");
        else           $display("TEST KALDI: %0d hata", hata);
        $finish;
    end
endmodule
