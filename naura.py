print("hai")

print("1")

import requests

def get_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    
    if data["cod"] == 200:
        weather_info = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"]
        }
        return weather_info
    else:
        return None

def main():
    api_key = "b38e44bf4e06efed339e24a25829706e"
    city = input("Masukkan nama kota: ")
    
    weather = get_weather(api_key, city)
    if weather:
        print(f"Cuaca di {weather['city']} saat ini:")
        print(f"Temperatur: {weather['temperature']}°C")
        print(f"Deskripsi: {weather['description']}")
        print(f"Kelembaban: {weather['humidity']}%")
        print(f"Kecepatan Angin: {weather['wind_speed']} m/s")
    else:
        print("Kota tidak ditemukan atau terjadi kesalahan dalam mengambil data cuaca.")

if __name__ == "__main__":
    main()
