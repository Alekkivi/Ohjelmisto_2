"""
Tutustu avoimeen OpenWeather-säärajapintaan: https://openweathermap.org/api.
Kirjoita ohjelma, joka kysyy käyttäjältä paikkakunnan nimen ja tulostaa sitä vastaavan säätilan tekstin sekä lämpötilan Celsius-asteina.
Perehdy rajapinnan dokumentaatioon riittävästi. Palveluun rekisteröityminen on tarpeen, jotta saat rajapintapyynnöissä tarvittavan API-avaimen (API key).
Selvitä myös, miten saat Kelvin-asteet muunnettua Celsius-asteiksi.

"""
import requests

city_input = input("Etsi kaupungin säätila syöttämällä kaupungin nimi tai lopeta ohjelma painamalla Enter: ")

while city_input != "":
    try:
        response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_input}&units=metric&lang=fi&appid=26840ca243e60b2172fba6a44fddac44").json()
        if response["cod"] == 200:
            response_weather = response['weather'][0]['description']
            response_temperature = response['main']['temp']
            print(f"Kaupungissa {city_input} sää on: {response_weather} ja lämpötila: {response_temperature} Celsius-astetta")
    except requests.exceptions.RequestException as e:
        print("Hakua ei voitu suorittaa")
    city_input = input("\nEtsi kaupungin säätila syöttämällä kaupungin nimi tai lopeta ohjelma painamalla Enter: ")