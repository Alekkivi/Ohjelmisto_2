"""
Laajenna ohjelmaa siten, että mukana on kulje-metodi, joka saa parametrinaan tuntimäärän.
Metodi kasvattaa kuljettua matkaa sen verran kuin auto on tasaisella vauhdilla annetussa tuntimäärässä edennyt.
Esimerkki: auto-olion tämänhetkinen kuljettu matka on 2000 km.
Nopeus on 60 km/h. Metodikutsu auto.kulje(1.5) kasvattaa kuljetun matkan lukemaan 2090 km.

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
    def drive(self, hours):
        self.travelled += self.currentSpeed * hours
        return self.travelled
    def __str__(self):
        return f""" 
        Auton rekisteritunnus: {self.license}.
        Auton huippunopeus: {self.topSpeed} km/h.
        Auton tämänhetkinen nopeus: {self.currentSpeed} km/h.
        Kuljettu matka autolla on: {self.travelled} km."""

car1 = Car("ABC-123",142,0,2000)
print(car1)

car1.accelerate(60)
car1.drive(1.5)
print(car1)