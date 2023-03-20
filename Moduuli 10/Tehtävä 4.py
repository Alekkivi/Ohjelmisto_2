"""
Tehtävä on jatkoa aiemmalle autokilpailutehtävälle.
Kirjoita Kilpailu-luokka, jolla on ominaisuuksina kilpailun nimi, pituus kilometreinä ja osallistuvien autojen lista.
Luokassa on alustaja, joka saa parametreinaan nimen, kilometrimäärän ja autolistan ja asettaa ne ominaisuuksille arvoiksi.

Luokassa on seuraavat metodit:
    - tunti_kuluu, joka toteuttaa aiemmassa autokilpailutehtävässä mainitut tunnin välein tehtävät toimenpiteet
     eli arpoo kunkin auton nopeuden muutoksen ja kutsuu kullekin autolle kulje-metodia.

    - tulosta_tilanne, joka tulostaa kaikkien autojen sen hetkiset tiedot selkeäksi taulukoksi muotoiltuna.

    - kilpailu_ohi, joka palauttaa True, jos jokin autoista on maalissa eli se on ajanut vähintään kilpailun kokonaiskilometrimäärän.
      Muussa tapauksessa palautetaan False.

Kirjoita pääohjelma, joka luo 8000 kilometrin kilpailun nimeltä "Suuri romuralli".
Luotavalle kilpailulle annetaan kymmenen auton lista samaan tapaan kuin aiemmassa tehtävässä.
Pääohjelma simuloi kilpailun etenemistä kutsumalla toistorakenteessa tunti_kuluu-metodia,
jonka jälkeen aina tarkistetaan kilpailu_ohi-metodin avulla, onko kilpailu ohi.
Ajantasainen tilanne tulostetaan tulosta tilanne-metodin avulla kymmenen tunnin välein sekä kertaalleen sen jälkeen, kun kilpailu on päättynyt. """

import random

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

class Competition:
    def __init__(self, comp_name, comp_length, car_list):
        self.comp_name = comp_name
        self.comp_length = comp_length
        self.car_list = car_list

    def hour_passes(self):
        for car in self.car_list:
            car.accelerate(random.randint(-10, 15))
            car.drive(1)

    def situation(self):
        print("Kilpailun tilanne:")
        print("{:<10} | {:<10} | {:<10}".format("Rekisteritunnus", "Tämänhetkinen nopeus", "Kuljettu matka "))
        print("-" * 55)
        for car in self.car_list:
            print("{:^15} | {:^20} | {:^14}".format(car.license, f"{car.currentSpeed} km/h", f"{car.travelled} km"))
        print("-" * 55)
        print("\n")

    def competition_over(self):
        for car in self.car_list:
            if car.travelled >= self.comp_length:
                return True
        return False

all_cars = []
cur_hour = 0

for i in range(1,11):
    all_cars.append(Car("ABC-" + str(i), random.randint(100, 200)))

competition = Competition("Suuri romuralli" , 8000, all_cars)

while not competition.competition_over():
    if cur_hour % 10 == 0 and not cur_hour == 0:
        print(f"{competition.comp_name} -kilpailun {cur_hour} tunti lähtee käyntiin nyt!\n")
        competition.situation()
    competition.hour_passes()
    cur_hour += 1
print(f"{competition.comp_name} loppui {cur_hour} tunnin jälkeen\n")
competition.situation()







