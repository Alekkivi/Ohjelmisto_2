"""
Kirjoita Auto-luokka, jonka ominaisuuksina ovat rekisteritunnus, huippunopeus, tämänhetkinen nopeus ja kuljettu matka.
Kirjoita luokkaan alustaja, joka asettaa ominaisuuksista kaksi ensin mainittua parametreina saatuihin arvoihin.
Uuden auton nopeus ja kuljetut matka on asetettava automaattisesti nollaksi.

Kirjoita pääohjelma, jossa luot uuden auton (rekisteritunnus ABC-123, huippunopeus 142 km/h).
Tulosta pääohjelmassa sen jälkeen luodun auton kaikki ominaisuudet.
"""

class Car:
    def __init__(self, license, topSpeed, currentSpeed = 0, travelled = 0):
        self.license = license
        self.topSpeed = topSpeed
        self.currentSpeed = currentSpeed
        self.travelled = travelled
    def __str__(self):
        return f'''
        Auton rekisteritunnus: {self.license}.
        Auton huippunopeus: {self.topSpeed} km/h.
        Auton tämänhetkinen nopeus: {self.currentSpeed} km/h.
        Kuljettu matka autolla on: {self.travelled} km.'''

#Main program begins
car1 = Car("ABC-123",142)
print(car1)