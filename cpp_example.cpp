#include <iostream>
#include <string>
#include <iomanip>
#include <vector>

using namespace std;

// Klasa bazowa Pojazd
class Pojazd {
protected:
    string marka;
    string model;
    double przebieg;          // Przebieg w km
    double predkoscSrednia;   // Prędkość średnia w km/h
    double czasPrzebiegu;     // Czas w godzinach
    const string TYP_POJAZDU;

public:
    // Konstruktor klasy Pojazd
    Pojazd(string m, string mod, double predkosc, string typ)
        : marka(m), model(mod), przebieg(0.0), predkoscSrednia(predkosc), czasPrzebiegu(0.0), TYP_POJAZDU(typ) {}

    // Metoda do przejechania określonego dystansu
    virtual void jedz(double kilometry) {
        przebieg += kilometry;
        double czas = kilometry / predkoscSrednia; // Obliczenie czasu podróży
        czasPrzebiegu += czas;

        cout << TYP_POJAZDU << " " << marka << " " << model << " przejechał(a) "
             << kilometry << " km w " << fixed << setprecision(2) << czas << " godzin." << endl;
    }

    // Metoda do wyświetlenia szczegółów pojazdu
    virtual void opis() const {
        cout << "Typ pojazdu: " << TYP_POJAZDU << ", Marka: " << marka << ", Model: " << model
             << ", Przebieg: " << fixed << setprecision(2) << przebieg << " km, Średnia prędkość: "
             << predkoscSrednia << " km/h, Całkowity czas podróży: " << czasPrzebiegu << " godzin." << endl;
    }

    virtual ~Pojazd() = default; // Wirtualny destruktor
};

// Klasa pochodna Samochod
class Samochod : public Pojazd {
public:
    Samochod(string m, string mod) : Pojazd(m, mod, 80.0, "Samochód") {} // Prędkość średnia: 80 km/h
};

// Klasa pochodna Rower
class Rower : public Pojazd {
public:
    Rower(string m, string mod) : Pojazd(m, mod, 20.0, "Rower") {} // Prędkość średnia: 20 km/h
};

// Klasa pochodna Motocykl
class Motocykl : public Pojazd {
public:
    Motocykl(string m, string mod) : Pojazd(m, mod, 100.0, "Motocykl") {} // Prędkość średnia: 100 km/h
};

int main() {
    // Tworzenie obiektów klasy Samochod, Rower i Motocykl
    Samochod mojeAuto("Toyota", "Corolla");
    Rower mojRower("Merida", "Crossway");
    Motocykl mojMotocykl("Harley Davidson", "Sportster");

    // Wektor wskaźników do obiektów klasy Pojazd
    vector<Pojazd*> pojazdy = { &mojeAuto, &mojRower, &mojMotocykl };

    // Wyświetlenie szczegółów przed podróżą
    for (const auto& pojazd : pojazdy) {
        pojazd->opis();
    }

    // Każdy pojazd przejeżdża 20 km
    cout << "\nPrzejechanie 20 km przez każdy pojazd:\n";
    for (auto& pojazd : pojazdy) {
        pojazd->jedz(20.0);
    }

    // Wyświetlenie szczegółów po podróży
    cout << "\nPo podróży:\n";
    for (const auto& pojazd : pojazdy) {
        pojazd->opis();
    }

    return 0;
}
