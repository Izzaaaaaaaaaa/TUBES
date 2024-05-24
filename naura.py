def display_routes():
    routes = {
        1: {"route": "Jakarta - Bandung", "price": 100000},
        2: {"route": "Jakarta - Surabaya", "price": 150000},
        3: {"route": "Jakarta - Yogyakarta", "price": 130000},
        4: {"route": "Jakarta - Lampung", "price": 2500000},
        5: {"route": "Jakarta - Padang", "price": 500000},
        6: {"route": "Jakarta - Purwokerto", "price": 150000},
    }
    print("Rute yang Tersedia:")
    for key, value in routes.items():
        print(f"{key}. {value['route']} (IDR {value['price']})")
    return routes

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
    routes = display_routes()
    try:
        route_id = int(input("Pilih rute berdasarkan nomor: "))
        if route_id not in routes:
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

        total_price = routes[route_id]["price"] * quantity

        print("\nRingkasan Pemesanan:")
        print(f"Rute: {routes[route_id]['route']}")
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
        print("Input tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    book_ticket()

