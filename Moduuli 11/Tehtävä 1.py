"""
Toteuta seuraava luokkahierarkia Python-kielellä: Julkaisu voi olla kirja tai lehti. Jokaisella julkaisulla on nimi.
Kirjalla on lisäksi kirjoittaja ja sivumäärä, kun taas lehdellä on päätoimittaja.
Kirjoita luokkiin myös tarvittavat alustajat. Tee aliluokkiin metodi tulosta_tiedot, joka tudostaa kyseisen julkaisun kaikki tiedot.
Luo pääohjelmassa julkaisut Aku Ankka (päätoimittaja Aki Hyyppä) ja Hytti n:o 6 (kirjailija Rosa Liksom, 200 sivua).
Tulosta molempien julkaisujen kaikki tiedot toteuttamiesi metodien avulla.
"""


class Julkaisu:
    def __init__(self, julkaisun_nimi):
        self.julkaisun_nimi = julkaisun_nimi


class Kirja(Julkaisu):
    def __init__(self, julkaisun_nimi, kirjoittaja, sivumäärä):
        self.kirjoittaja = kirjoittaja
        self.sivumäärä = sivumäärä
        super().__init__(julkaisun_nimi)

    def tulosta_tiedot(self):
        print(f"Kirjan {self.julkaisun_nimi} on kirjoittanut {self.kirjoittaja} ja siinä on {self.sivumäärä} sivua")


class Lehti(Julkaisu):
    def __init__(self, julkaisun_nimi, päätoimittaja):
        self.päätoimittaja = päätoimittaja
        super().__init__(julkaisun_nimi)

    def tulosta_tiedot(self):
        print(f"{self.julkaisun_nimi} lehden päätoimittaja on {self.päätoimittaja}")

k = Kirja("Hytti n:o 6", "Rosa Liksom", 200)
l = Lehti("Aku Ankka", "Aki hyyppä")

k.tulosta_tiedot()
l.tulosta_tiedot()