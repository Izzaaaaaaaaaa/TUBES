def display_routes():
    routes = {
        1: {"route": "Jakarta - Bandung", "price": 100000},
        2: {"route": "Jakarta - Surabaya", "price": 150000},
        3: {"route": "Jakarta - Yogyakarta", "price": 130000},
    }
    print("Rute Tersedia:")
    for key, value in routes.items():
        print(f"{key}. {value['route']} (IDR {value['price']})")
    return routes

def display_schedules(route_id):
    schedules = {
        1: ["08:00", "12:00", "16:00"],
        2: ["09:00", "13:00", "17:00"],
        3: ["07:00", "11:00", "15:00"],
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

# def display_routes():
#     routes = {
#         1: {"route": "Jakarta - Bandung", "price": 100000},
#         2: {"route": "Jakarta - Surabaya", "price": 150000},
#         3: {"route": "Jakarta - Yogyakarta", "price": 130000},
#     }
#     print("Rute Tersedia:")
#     for key, value in routes.items():
#         print(f"{key}. {value['route']} (IDR {value['price']})")
#     return routes

# def display_schedules(route_id):
#     schedules = {
#         1: ["08:00", "12:00", "16:00"],
#         2: ["09:00", "13:00", "17:00"],
#         3: ["07:00", "11:00", "15:00"],
#     }
#     print("Jadwal Tersedia:")
#     for i, schedule in enumerate(schedules[route_id], start=1):
#         print(f"{i}. {schedule}")
#     return schedules[route_id]

# def get_passenger_info(quantity):
#     passengers = []
#     for i in range(quantity):
#         print(f"\nMasukkan data penumpang ke-{i+1}:")
#         name = input("Nama Penumpang: ")
#         nik = input("NIK: ")
#         phone = input("Nomor Telepon: ")
#         email = input("Alamat Email: ")
#         passengers.append({
#             "name": name,
#             "nik": nik,
#             "phone": phone,
#             "email": email
#         })
#     return passengers

# def book_ticket():
#     routes = display_routes()
#     try:
#         route_id = int(input("Pilih rute berdasarkan nomor: "))
#         if route_id not in routes:
#             print("Pilihan rute tidak valid.")
#             return

#         schedules = display_schedules(route_id)
#         schedule_choice = int(input("Pilih jadwal berdasarkan nomor: "))
#         if schedule_choice not in range(1, len(schedules) + 1):
#             print("Pilihan jadwal tidak valid.")
#             return

#         quantity = int(input("Masukkan jumlah tiket: "))
#         if quantity <= 0:
#             print("Jumlah tiket tidak valid.")
#             return

#         total_price = routes[route_id]["price"] * quantity
#         passengers = get_passenger_info(quantity)

#         print("\nRingkasan Pemesanan:")
#         print(f"Rute: {routes[route_id]['route']}")
#         print(f"Jadwal: {schedules[schedule_choice - 1]}")
#         print(f"Jumlah Tiket: {quantity}")
#         print(f"Total Harga: IDR {total_price}")
#         for i, passenger in enumerate(passengers, start=1):
#             print(f"\nData Penumpang {i}:")
#             print(f"Nama: {passenger['name']}")
#             print(f"NIK: {passenger['nik']}")
#             print(f"Nomor Telepon: {passenger['phone']}")
#             print(f"Alamat Email: {passenger['email']}")

#         confirm = input("Konfirmasi pemesanan? (ya/tidak): ").lower()
#         if confirm == "ya":
#             print("Pemesanan dikonfirmasi. Terima kasih atas pembelian Anda!")
#         elif confirm == "tidak":
#             print("Pemesanan dibatalkan.")
#         else:
#             print("Pilihan tidak valid.")
#     except ValueError:
#         print("Input tidak valid, silakan coba lagi.")

# if __name__ == "__main__":
#     book_ticket()


# class BusTicketSystem:
#     def __init__(self):
#         self.routes = {
#             1: {"route": "Jakarta - Bandung", "price": 100000},
#             2: {"route": "Jakarta - Surabaya", "price": 150000},
#             3: {"route": "Jakarta - Yogyakarta", "price": 130000},
#         }
#         self.schedules = {
#             1: {"times": ["08:00", "12:00", "16:00"], "seats": [40, 40, 40]},
#             2: {"times": ["09:00", "13:00", "17:00"], "seats": [40, 40, 40]},
#             3: {"times": ["07:00", "11:00", "15:00"], "seats": [40, 40, 40]},
#         }

#     def display_routes(self):
#         print("Rute Tersedia:")
#         for key, value in self.routes.items():
#             print(f"{key}. {value['route']} (IDR {value['price']})")

#     def display_schedules(self, route_id):
#         print(f"Jadwal Tersedia untuk rute {self.routes[route_id]['route']}:")
#         for i, (time, seats) in enumerate(zip(self.schedules[route_id]["times"], self.schedules[route_id]["seats"]), start=1):
#             print(f"{i}. {time} - Sisa bangku: {seats}")

#     def get_passenger_info(self, quantity):
#         passengers = []
#         for i in range(quantity):
#             print(f"\nMasukkan data penumpang ke-{i+1}:")
#             name = input("Nama Penumpang: ")
#             nik = input("NIK: ")
#             phone = input("Nomor Telepon: ")
#             email = input("Alamat Email: ")
#             passengers.append({
#                 "name": name,
#                 "nik": nik,
#                 "phone": phone,
#                 "email": email
#             })
#         return passengers

#     def book_ticket(self):
#         self.display_routes()
#         try:
#             route_id = int(input("Pilih rute berdasarkan nomor: "))
#             if route_id not in self.routes:
#                 print("Pilihan rute tidak valid.")
#                 return

#             self.display_schedules(route_id)
#             schedule_choice = int(input("Pilih jadwal berdasarkan nomor: "))
#             if schedule_choice not in range(1, len(self.schedules[route_id]["times"]) + 1):
#                 print("Pilihan jadwal tidak valid.")
#                 return

#             quantity = int(input("Masukkan jumlah tiket: "))
#             if quantity <= 0:
#                 print("Jumlah tiket tidak valid.")
#                 return

#             available_seats = self.schedules[route_id]["seats"][schedule_choice - 1]
#             if quantity > available_seats:
#                 print(f"Maaf, hanya tersedia {available_seats} bangku.")
#                 return

#             total_price = self.routes[route_id]["price"] * quantity
#             passengers = self.get_passenger_info(quantity)

#             print("\nRingkasan Pemesanan:")
#             print(f"Rute: {self.routes[route_id]['route']}")
#             print(f"Jadwal: {self.schedules[route_id]['times'][schedule_choice - 1]}")
#             print(f"Jumlah Tiket: {quantity}")
#             print(f"Total Harga: IDR {total_price}")
#             for i, passenger in enumerate(passengers, start=1):
#                 print(f"\nData Penumpang {i}:")
#                 print(f"Nama: {passenger['name']}")
#                 print(f"NIK: {passenger['nik']}")
#                 print(f"Nomor Telepon: {passenger['phone']}")
#                 print(f"Alamat Email: {passenger['email']}")

#             confirm = input("Konfirmasi pemesanan? (ya/tidak): ").lower()
#             if confirm == "ya":
#                 self.schedules[route_id]["seats"][schedule_choice - 1] -= quantity
#                 print("Pemesanan dikonfirmasi. Terima kasih atas pembelian Anda!")
#             elif confirm == "tidak":
#                 print("Pemesanan dibatalkan.")
#             else:
#                 print("Pilihan tidak valid.")
#         except ValueError:
#             print("Input tidak valid, silakan coba lagi.")

# if __name__ == "__main__":
#     system = BusTicketSystem()
#     system.book_ticket()

