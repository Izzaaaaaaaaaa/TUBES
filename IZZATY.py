print("              <<========== Pembelian Tiket BUS ===========>>")
print()
print("                  <<========== Kota Tujuan ===========>>     ")
def cetak():
    print("              ===============================================")
cetak()
print("||   KODE    ==  Jadwal Keberangkatan  ==  Destinasi ==      Harga    ||")
print("||   EE01B   ==       19.20 WIB        ==  SURABAYA  ==  Rp.350.000.- ||")
print("||   EE04C   ==       19.35 WIB        ==  PURWOKERTO==  Rp.250.000.- ||")
print("||   FEG01B  ==       20.20 WIB        ==  JAKARTA   ==  Rp.450.000.- ||")
print("||   GH24J   ==       21.50 WIB        ==  LAMPUNG   ==  Rp.500.000.- ||")
print("||   BK23D   ==       22.45 WIB        ==  RIAU      ==  Rp.800.000.- ||")
print()
#input data
nama = input("Masukkan Nama Anda: ")
no = int(input("No Hp: "))
kode = str(input("Masukkan KODE Pemesanan: "))
Jumlah_pembelian = int(input("Jumlah pembelian tiket: "))

if kode=="EE01B":
    Tujuan = "SURABAYA"
    harga =  350000 
    Tujuan = "PURWOKERTO"
    harga =  250000 
elif kode=="FEG01B":
    Tujuan = "JAKARTA"
    harga =  450000 
elif kode=="GH24J":
    Tujuan = "LAMPUNG"
    harga =  500000 
elif kode=="BK23D":
    Tujuan = "RIAU"
    harga =  800000
else:
    Tujuan = "Tidak tersedia"
    harga =  0
    
cetak()
print("Nama pembeli: ", nama)
print("No Hp: ", no )
print("Kode pemesanan pembeli: ", kode)
print("Kota tujuan: ", Tujuan)
print("Harga tiket: ", harga)
print("Jumlah pembelian Tiket: ", Jumlah_pembelian)
cetak()

if Jumlah_pembelian>=3:
    potongan = (Jumlah_pembelian*harga)*0.1
else:
    potongan=0
total_potongan = (Jumlah_pembelian*harga)-potongan
print("Total potongan yang di dapat: ", potongan)
print("Total bayar : ", total_potongan)
bayar = int(input("Jumlah pembayaran: "))
kembalian = (bayar-total_potongan)
print("uang kembalian: ",kembalian)
  
 


