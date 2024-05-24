# print("              <<========== Pembelian Tiket BUS ===========>>")
# print()
# print("                  <<========== Kota Tujuan ===========>>     ")
# def cetak():
#     print("              ===============================================")
# cetak()

# def rute_tersedia():
#     rute = {
#         1: {"||   KODE    ==  Jadwal Keberangkatan  ==  Destinasi ==      Harga    ||"},
#         2: {"||   EE01B   ==       19.20 WIB        ==  SURABAYA  ==  Rp.350.000.- ||"},
#         3: {"||   EE04C   ==       19.35 WIB        ==  PURWOKERTO==  Rp.250.000.- ||"},
#         4: {"||   FEG01B  ==       20.20 WIB        ==  JAKARTA   ==  Rp.450.000.- ||"},
#         5: {"||   GH24J   ==       21.50 WIB        ==  LAMPUNG   ==  Rp.500.000.- ||"},
#         6: {"||   BK23D   ==       22.45 WIB        ==  RIAU      ==  Rp.800.000.- ||"},
#     }
#     print("Rute tersedia:")
#     for key, value in rute.items():
#         print(f"{key}. {value['route']} (IDR {value['price']})")
#     return rute
# print()
# #input data
# nama = input("Masukkan Nama Anda: ")
# no = int(input("No Hp: "))
# kode = str(input("Masukkan KODE Pemesanan: "))
# Jumlah_pembelian = int(input("Jumlah pembelian tiket: "))
# def tiket_BUS():
#     if kode=="EE01B":
#          Tujuan = "SURABAYA"
#          harga =  350000 
#     elif kode=="EE04C":
#         Tujuan = "PURWOKERTO"
#         harga =  250000 
#     elif kode=="FEG01B":
#         Tujuan = "JAKARTA"
#         harga =  450000 
#     elif kode=="GH24J":
#         Tujuan = "LAMPUNG"
#         harga =  500000 
#     elif kode=="BK23D":
#         Tujuan = "RIAU"
#         harga =  800000
#     else:
#          Tujuan = "Tidak tersedia"
#          harga =  0
         
# confirm = input("Konfirmasi pemesanan? (ya/tidak): ").lower()
#     if confirm == "ya":
#                  print("Pemesanan dikonfirmasi. Terima kasih atas pembelian Anda!")
#     elif confirm == "tidak":
#                  print("Pemesanan dibatalkan.")
#     else:
#                  print("Pilihan tidak valid.")
#     except ValueError:
#          print("Input tidak valid, silakan coba lagi.")
    
    # cetak()
    # print("Nama pembeli: ", nama)
    # print("No Hp: ", no )
    # print("Kode pemesanan pembeli: ", kode)
    # print("Kota tujuan: ", Tujuan)
    # print("Harga tiket: ", harga)
    # print("Jumlah pembelian Tiket: ", Jumlah_pembelian)
    # cetak()

# if Jumlah_pembelian>=3:
#     potongan = (Jumlah_pembelian*harga)*0.1
# else:
#     potongan=0
# total_potongan = (Jumlah_pembelian*harga)-potongan
# print("Total potongan yang di dapat: ", potongan)
# print("Total bayar : ", total_potongan)
# bayar = int(input("Jumlah pembayaran: "))
# kembalian = (bayar-total_potongan)
# print("uang kembalian: ",kembalian)
  
 


def display_routes():
    rute = {
        1: {"route": "Jakarta - Bandung", "price": 100000},
        2: {"route": "Jakarta - Surabaya", "price": 150000},
        3: {"route": "Jakarta - Yogyakarta", "price": 130000},
        4: {"route": "Jakarta - Lampung", "price": 2500000},
        5: {"route": "Jakarta - Padang", "price": 500000},
        6: {"route": "Jakarta - Purwokerto", "price": 1500000},
    }
    print("Rute Tersedia:")
    for key, value in rute.items():
        print(f"{key}. {value['route']} (IDR {value['price']})")
    return rute

def display_schedules(route_id):
    schedules = {
        1: ["08:00", "12:00", "16:00"],
        2: ["09:00", "13:00", "17:00"],
        3: ["07:00", "11:00", "15:00"],
        4: ['08:15', '22:48', '04:27'],
        5: ['00:09', '17:05', '20:18'],
        6: ['03:44', '12:50', '15:00'],
    }
    print("Jadwal Tersedia:")
    for i, schedule in enumerate(schedules[route_id], start=1):
        print(f"{i}. {schedule}")
    return schedules[route_id]

def book_ticket():
    rute = display_routes()
    try:
        route_id = int(input("Pilih rute berdasarkan nomor: "))
        if route_id not in rute:
            print("Pilihan rute tidak valid.")
            return

        schedules = display_schedules(route_id)
        schedule_choice = int(input("Pilih jadwal berdasarkan nomor: "))
        if schedule_choice not in range(1, len(schedules) + 1):
            print("Pilihan jadwal tidak valid.")
            return

        quantity = int(input("Masukkan jumlah tiket: "))
        if quantity <= 0:
            print("Jumlah tiket tidak valid.")
            return

        total_price = rute[route_id]["price"] * quantity

        print("\nRingkasan Pemesanan:")
        print(f"Rute: {rute[route_id]['route']}")
        print(f"Jadwal: {schedules[schedule_choice - 1]}")
        print(f"Jumlah Tiket: {quantity}")
        print(f"Total Harga: IDR {total_price}")

        confirm = input("Konfirmasi pemesanan? (ya/tidak): ").lower()
        if confirm == "ya":
            print("Pemesanan dikonfirmasi. Terima kasih atas pembelian Anda!")
        elif confirm == "tidak":
            print("Pemesanan dibatalkan.")
        else:
            print("Pilihan tidak valid.")
    except ValueError:
        input("Input tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    book_ticket()


