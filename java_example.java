class Pojazd {
    protected String marka;
    protected String model;
    protected double przebieg;
    protected double predkoscSrednia;
    protected double czasPrzebiegu;
    protected String typPojazdu;

    public Pojazd(String marka, String model, double predkoscSrednia, String typPojazdu) {
        this.marka = marka;
        this.model = model;
        this.przebieg = 0.0;
        this.predkoscSrednia = predkoscSrednia;
        this.czasPrzebiegu = 0.0;
        this.typPojazdu = typPojazdu;
    }

    public void jedz(double kilometry) {
        przebieg += kilometry;
        double czas = kilometry / predkoscSrednia;
        czasPrzebiegu += czas;
        System.out.printf("%s %s %s przejechał(a) %.2f km w %.2f godzin.%n", typPojazdu, marka, model, kilometry, czas);
    }

    public void opis() {
        System.out.printf("Typ pojazdu: %s, Marka: %s, Model: %s, Przebieg: %.2f km, Średnia prędkość: %.2f km/h, Czas podróży: %.2f godzin.%n",
                typPojazdu, marka, model, przebieg, predkoscSrednia, czasPrzebiegu);
    }
}

class Samochod extends Pojazd {
    public Samochod(String marka, String model) {
        super(marka, model, 80.0, "Samochód");
    }
}

class Rower extends Pojazd {
    public Rower(String marka, String model) {
        super(marka, model, 20.0, "Rower");
    }
}

class Motocykl extends Pojazd {
    public Motocykl(String marka, String model) {
        super(marka, model, 100.0, "Motocykl");
    }
}

public class Main {
    public static void main(String[] args) {
        Pojazd[] pojazdy = {
            new Samochod("Toyota", "Corolla"),
            new Rower("Merida", "Crossway"),
            new Motocykl("Harley Davidson", "Sportster")
        };

        for (Pojazd pojazd : pojazdy) {
            pojazd.opis();
        }

        System.out.println("\nPrzejechanie 20 km przez każdy pojazd:");
        for (Pojazd pojazd : pojazdy) {
            pojazd.jedz(20.0);
        }

        System.out.println("\nPo podróży:");
        for (Pojazd pojazd : pojazdy) {
            pojazd.opis();
        }
    }
}
