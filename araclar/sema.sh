#!/usr/bin/env bash
# Kullanim: ./araclar/sema.sh <verilog_dosyasi> <ust_modul_adi>
# Ornek:    ./araclar/sema.sh rtl/alu.v alu
# Cikti:    cizimler/<ust_modul_adi>.svg
#
# Gerekenler: yosys (OSS CAD Suite) ve netlistsvg (npm install -g netlistsvg)

set -euo pipefail

if [ "$#" -ne 2 ]; then
  echo "Kullanim: $0 <verilog_dosyasi> <ust_modul_adi>"
  exit 1
fi

DOSYA="$1"
MODUL="$2"
CIKTI_DIZIN="cizimler"

mkdir -p "$CIKTI_DIZIN"

yosys -q -p "read_verilog -sv $DOSYA; prep -top $MODUL; write_json $CIKTI_DIZIN/$MODUL.json"
netlistsvg "$CIKTI_DIZIN/$MODUL.json" -o "$CIKTI_DIZIN/$MODUL.svg"

echo "Sema olusturuldu: $CIKTI_DIZIN/$MODUL.svg"
