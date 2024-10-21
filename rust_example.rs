struct Pojazd {
    marka: String,
    model: String,
    przebieg: f64,
    predkosc_srednia: f64,
    czas_przebiegu: f64,
    typ_pojazdu: String,
}

impl Pojazd {
    fn new(marka: &str, model: &str, predkosc_srednia: f64, typ_pojazdu: &str) -> Self {
        Self {
            marka: marka.to_string(),
            model: model.to_string(),
            przebieg: 0.0,
            predkosc_srednia,
            czas_przebiegu: 0.0,
            typ_pojazdu: typ_pojazdu.to_string(),
        }
    }

    fn jedz(&mut self, kilometry: f64) {
        self.przebieg += kilometry;
        let czas = kilometry / self.predkosc_srednia;
        self.czas_przebiegu += czas;
        println!("{} {} {} przejechał(a) {:.2} km w {:.2} godzin.", self.typ_pojazdu, self.marka, self.model, kilometry, czas);
    }

    fn opis(&self) {
        println!("Typ pojazdu: {}, Marka: {}, Model: {}, Przebieg: {:.2} km, Średnia prędkość: {:.2} km/h, Czas podróży: {:.2} godzin.",
                 self.typ_pojazdu, self.marka, self.model, self.przebieg, self.predkosc_srednia, self.czas_przebiegu);
    }
}

struct Samochod(Pojazd);
struct Rower(Pojazd);
struct Motocykl(Pojazd);

impl Samochod {
    fn new(marka: &str, model: &str) -> Self {
        Samochod(Pojazd::new(marka, model, 80.0, "Samochód"))
    }
}

impl Rower {
    fn new(marka: &str, model: &str) -> Self {
        Rower(Pojazd::new(marka, model, 20.0, "Rower"))
    }
}

impl Motocykl {
    fn new(marka: &str, model: &str) -> Self {
        Motocykl(Pojazd::new(marka, model, 100.0, "Motocykl"))
    }
}

fn main() {
    let mut pojazdy: Vec<Box<dyn std::any::Any>> = vec![
        Box::new(Samochod::new("Toyota", "Corolla")),
        Box::new(Rower::new("Merida", "Crossway")),
        Box::new(Motocykl::new("Harley Davidson", "Sportster")),
    ];

    for pojazd in &mut pojazdy {
        if let Some(pojazd) = pojazd.downcast_mut::<Samochod>() {
            pojazd.0.opis();
        } else if let Some
