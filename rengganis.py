# pembuatan variabel
nama_pemesan = []
nama_bus = []
kode_bus = []
nama_kelas = []
harga = []

# pengkondisian dan perulangan
jumlah_pesanan = int(input("masukkan jumlah pesanan tiket :"))
for i in range (jumlah_pesanan) :
    print("pesanan ke-", i+1)
nama_pemesan.append(input("masukkan nama pemesan : "))