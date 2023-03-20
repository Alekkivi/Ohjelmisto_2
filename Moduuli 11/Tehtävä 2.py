"""
Kirjoita aiemmin laatimallesi Auto-luokalle aliluokat Sähköauto ja Polttomoottoriauto.
Sähköautolla on ominaisuutena akkukapasiteetti kilowattitunteina. Polttomoottoriauton ominaisuutena on bensatankin koko litroina.
Kirjoita aliluokille alustajat.
Esimerkiksi sähköauton alustaja saa parametreinaan rekisteritunnuksen, huippunopeuden ja akkukapasiteetin.
Se kutsuu yliluokan alustajaa kahden ensin mainitun asettamiseksi sekä asettaa oman kapasiteettinsa.

Kirjoita pääohjelma, jossa luot yhden sähköauton (ABC-15, 180 km/h, 52.5 kWh) ja yhden polttomoottoriauton (ACD-123, 165 km/h, 32.3 l).
Aseta kummallekin autolle haluamasi nopeus, käske autoja ajamaan kolmen tunnin verran ja tulosta autojen matkamittarilukemat. """


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


class ElectricCar(Car):
    def __init__(self, license, topSpeed, battery_capacity):
        super().__init__(license, topSpeed)
        self.battery_capacity = battery_capacity


class PetrolCar(Car):
    def __init__(self, license, topSpeed, petrol_capacity):
        super().__init__(license, topSpeed)
        self.battery_capacity = petrol_capacity


Ev = ElectricCar("ABC-15", 180, 52.5)
Pv = PetrolCar("ACD-123", 165, 32.3)

Ev.accelerate(180)
Ev.drive(3)

Pv.accelerate(165)
Pv.drive(3)

print("\n{:<10} | {:<10} |".format("Rekisteritunnus", "Kuljettu matka "))
print("{:^15} | {:^15} |".format(Ev.license, f"{Ev.travelled} km"))
print("{:^15} | {:^15} |".format(Pv.license, f"{Pv.travelled} km"))