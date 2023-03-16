"""
Jatka ohjelmaa kirjoittamalla Auto-luokkaan kiihdytä-metodi, joka saa parametrinaan nopeuden muutoksen (km/h).
Jos nopeuden muutos on negatiivinen, auto hidastaa. Metodin on muutettava auto-olion nopeus-ominaisuuden arvoa.
Auton nopeus ei saa kasvaa huippunopeutta suuremmaksi eikä alentua nollaa pienemmäksi.

Jatka pääohjelmaa siten, että auton nopeutta nostetaan ensin +30 km/h, sitten +70 km/h ja lopuksi +50 km/h.
Tulosta tämän jälkeen auton nopeus. Tee sitten hätäjarrutus määräämällä nopeuden muutos -200 km/h ja tulosta uusi nopeus.
Kuljettua matkaa ei tarvitse vielä päivittää.
"""
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
    def __str__(self):
        return f""" 
        Auton rekisteritunnus: {self.license}.
        Auton huippunopeus: {self.topSpeed} km/h.
        Auton tämänhetkinen nopeus: {self.currentSpeed} km/h.
        Kuljettu matka autolla on: {self.travelled} km."""

#Main program begins
car1 = Car("ABC-123",142)
car1.accelerate(30)
car1.accelerate(70)
car1.accelerate(50)

print(f"Auton nopeus kiihdyttämisen jälkeen on: {car1.currentSpeed} km/h")

car1.accelerate(-200)
print(f"Hätäjarrutuksen jälkeen auton vauhti on: {car1.currentSpeed} km/h")