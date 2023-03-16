"""
Nyt ohjelmoidaan autokilpailu. Uuden auton kuljettu matka alustetaan automaattisesti nollaksi.
Tee pääohjelman alussa lista, joka koostuu kymmenestä toistorakenteella luodusta auto-oliosta.
Jokaisen auton huippunopeus arvotaan 100 km/h ja 200 km/h väliltä. Rekisteritunnus luodaan seuraavasti "ABC-1", "ABC-2" jne.

Sitten kilpailu alkaa. Kilpailun aikana tehdään tunnin välein seuraavat toimenpiteet:
    Jokaisen auton nopeutta muutetaan siten, että nopeuden muutos arvotaan väliltä -10 ja +15 km/h väliltä. Tämä tehdään kutsumalla kiihdytä-metodia.
    Kaikkia autoja käsketään liikkumaan yhden tunnin ajan. Tämä tehdään kutsumalla kulje-metodia.
    Kilpailu jatkuu, kunnes jokin autoista on edennyt vähintään 10000 kilometriä.
    Lopuksi tulostetaan kunkin auton kaikki ominaisuudet selkeäksi taulukoksi muotoiltuna.
"""
import random
from prettytable import PrettyTable

class Car:
    def __init__(self, license, topSpeed, currentSpeed = 0, travelled = 0):
        self.license = license
        self.topSpeed = topSpeed
        self.currentSpeed = currentSpeed
        self.travelled = travelled
    def accelerate(self, change):
        self.currentSpeed += change
        if self.currentSpeed >= self.topSpeed:
            self.currentSpeed = self.topSpeed
        elif self.currentSpeed <= 0:
            self.currentSpeed = 0
    def drive(self, hours):
        self.travelled += self.currentSpeed * hours
        return self.travelled
    def __str__(self):
        return f""" 
        Auton rekisteritunnus: {self.license}.
        Auton huippunopeus: {self.topSpeed} km/h.
        Auton tämänhetkinen nopeus: {self.currentSpeed} km/h.
        Kuljettu matka autolla on: {self.travelled} km."""

#Main program begins
all_cars = []
race_leader = 0
table = PrettyTable()

for i in range(1,11):
    all_cars.append(Car("ABC-" + str(i), random.randint(100, 200)))

while race_leader < 10000:
    for car in all_cars:
        car.accelerate(random.randint(-10, 15))
        car.drive(1)
        if car.travelled > race_leader:
            race_leader = car.travelled

table.field_names = ["Rekisteritunnus", "Huippunopeus", "Nykyinen nopeus", "Kuljettu matka"]
for car in all_cars:
    table.add_row([car.license, car.topSpeed, car.currentSpeed, car.travelled])
print(table)