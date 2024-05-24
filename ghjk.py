def rute():
    rute = {
        1: {"route": "Jakarta - Bandung", "price": 100000},
        2: {"route": "Jakarta - Surabaya", "price": 150000},
        3: {"route": "Jakarta - Yogyakarta", "price": 130000},
        4: {"route": "Jakarta - Lampung", "price": 2500000},
        5: {"route": "Jakarta - Padang", "price": 500000},
        6: {"route": "Jakarta - Purwokerto", "price": 1500000},
    }
    print("Rute yang tersedia: ")
    for key, value in rute.items():
        print(f"{key}. {value['route']} (IDR {value['price']})")
    return rute

def waktu_keberangkatan(rute_id):
    jadwal= {
        1: ["08:00", "12:00", "16:00"],
        2: ["09:00", "13:00", "17:00"],
        3: ["07:00", "11:00", "15:00"],
        4: ['08:15', '22:48', '04:27'],
        5: ['00:09', '17:05', '20:18'],
        6: ['03:44', '12:50', '15:00'],
    }
    print("Jadwal Tersedia:")
    for i,jadwal in enumerate(waktu_keberangkatan[rute_id], start=1):
        print(f"{i}. {jadwal}")
    return jadwal[rute_id]

nama = input('masukkan nama anda: ')