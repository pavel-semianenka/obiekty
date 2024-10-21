class Pojazd:
    def __init__(self, marka, model, predkosc_srednia, typ_pojazdu):
        self.marka = marka
        self.model = model
        self.przebieg = 0.0
        self.predkosc_srednia = predkosc_srednia
        self.czas_przebiegu = 0.0
        self.typ_pojazdu = typ_pojazdu

    def jedz(self, kilometry):
        self.przebieg += kilometry
        czas = kilometry / self.predkosc_srednia
        self.czas_przebiegu += czas
        print(f"{self.typ_pojazdu} {self.marka} {self.model} przejechał(a) {kilometry} km w {czas:.2f} godzin.")

    def opis(self):
        print(f"Typ pojazdu: {self.typ_pojazdu}, Marka: {self.marka}, Model: {self.model}, Przebieg: {self.przebieg:.2f} km, Średnia prędkość: {self.predkosc_srednia} km/h, Czas podróży: {self.czas_przebiegu:.2f} godzin.")


class Samochod(Pojazd):
    def __init__(self, marka, model):
        super().__init__(marka, model, 80.0, "Samochód")


class Rower(Pojazd):
    def __init__(self, marka, model):
        super().__init__(marka, model, 20.0, "Rower")


class Motocykl(Pojazd):
    def __init__(self, marka, model):
        super().__init__(marka, model, 100.0, "Motocykl")


if __name__ == "__main__":
    pojazdy = [
        Samochod("Toyota", "Corolla"),
        Rower("Merida", "Crossway"),
        Motocykl("Harley Davidson", "Sportster")
    ]

    for pojazd in pojazdy:
        pojazd.opis()

    print("\nPrzejechanie 20 km przez każdy pojazd:")
    for pojazd in pojazdy:
        pojazd.jedz(20.0)

    print("\nPo podróży:")
    for pojazd in pojazdy:
        pojazd.opis()
