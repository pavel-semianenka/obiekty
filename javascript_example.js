class Pojazd {
    constructor(marka, model, predkoscSrednia, typPojazdu) {
        this.marka = marka;
        this.model = model;
        this.przebieg = 0.0;
        this.predkoscSrednia = predkoscSrednia;
        this.czasPrzebiegu = 0.0;
        this.typPojazdu = typPojazdu;
    }

    jedz(kilometry) {
        this.przebieg += kilometry;
        const czas = kilometry / this.predkoscSrednia;
        this.czasPrzebiegu += czas;
        console.log(`${this.typPojazdu} ${this.marka} ${this.model} przejechał(a) ${kilometry} km w ${czas.toFixed(2)} godzin.`);
    }

    opis() {
        console.log(`Typ pojazdu: ${this.typPojazdu}, Marka: ${this.marka}, Model: ${this.model}, Przebieg: ${this.przebieg.toFixed(2)} km, Średnia prędkość: ${this.predkoscSrednia} km/h, Czas podróży: ${this.czasPrzebiegu.toFixed(2)} godzin.`);
    }
}

class Samochod extends Pojazd {
    constructor(marka, model) {
        super(marka, model, 80.0, "Samochód");
    }
}

class Rower extends Pojazd {
    constructor(marka, model) {
        super(marka, model, 20.0, "Rower");
    }
}

class Motocykl extends Pojazd {
    constructor(marka, model) {
        super(marka, model, 100.0, "Motocykl");
    }
}

const pojazdy = [
    new Samochod("Toyota", "Corolla"),
    new Rower("Merida", "Crossway"),
    new Motocykl("Harley Davidson", "Sportster")
];

pojazdy.forEach(pojazd => pojazd.opis());

console.log("\nPrzejechanie 20 km przez każdy pojazd:");
pojazdy.forEach(pojazd => pojazd.jedz(20));

console.log("\nPo podróży:");
pojazdy.forEach(pojazd => pojazd.opis());
