"""
Jatka edellisen tehtävän ohjelmaa siten, että Talo-luokassa on parametriton metodi palohälytys, joka käskee kaikki hissit pohjakerrokseen.
Jatka pääohjelmaa siten, että talossasi tulee palohälytys.
"""

class Hissi:
    def __init__(self,alin_kerros, ylin_kerros, hissin_numero):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.hissin_numero = hissin_numero
        self.nykyinen_kerros = self.alin_kerros

    def kerros_ylös(self):
        if self.nykyinen_kerros < self.ylin_kerros:
            self.nykyinen_kerros += 1

    def kerros_alas(self):
        if self.nykyinen_kerros > self.alin_kerros:
            self.nykyinen_kerros -= 1

    def siirry_kerrokseen(self, kohde_kerros):
        if kohde_kerros > self.ylin_kerros or kohde_kerros < self.alin_kerros:
            print("Tarkista kerroksien määrä")
        while self.nykyinen_kerros != kohde_kerros:
            if self.nykyinen_kerros < kohde_kerros:
                self.kerros_ylös()
            else:
                self.kerros_alas()
        print(f"Hissi {self.hissin_numero} matkusti kerrokseen: {self.nykyinen_kerros}")

class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_lkm):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.hissit = []

        for i in range(1, hissien_lkm + 1):
            self.hissit.append(Hissi(self.alin_kerros, self.ylin_kerros, i))

    def aja_hissiä(self, hissin_nro, kohdekerros):
        for hissi in self.hissit:
            if hissin_nro == hissi.hissin_numero:
                hissi.siirry_kerrokseen(kohdekerros)

    def palohälytys(self):
        for hissi in self.hissit:
            hissi.siirry_kerrokseen(self.alin_kerros)

    def missä_hissit(self):
        for hissi in self.hissit:
            print(f"Hissi {hissi.hissin_numero} on kerroksessa {hissi.nykyinen_kerros}")



talo1 = Talo(1,5,3)
talo1.aja_hissiä(1, 2)
talo1.aja_hissiä(2, 3)
talo1.aja_hissiä(3, 4)
talo1.palohälytys()