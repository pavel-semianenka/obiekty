using System;
using System.Collections.Generic;

public class Pojazd
{
    protected string Marka { get; set; }
    protected string Model { get; set; }
    protected double Przebieg { get; set; }
    protected double PredkoscSrednia { get; set; }
    protected double CzasPrzebiegu { get; set; }
    protected string TypPojazdu { get; }

    public Pojazd(string marka, string model, double predkoscSrednia, string typPojazdu)
    {
        Marka = marka;
        Model = model;
        Przebieg = 0.0;
        PredkoscSrednia = predkoscSrednia;
        CzasPrzebiegu = 0.0;
        TypPojazdu = typPojazdu;
    }

    public virtual void Jedz(double kilometry)
    {
        Przebieg += kilometry;
        double czas = kilometry / PredkoscSrednia;
        CzasPrzebiegu += czas;
        Console.WriteLine($"{TypPojazdu} {Marka} {Model} przejechał(a) {kilometry} km w {czas:F2} godzin.");
    }

    public virtual void Opis()
    {
        Console.WriteLine($"Typ pojazdu: {TypPojazdu}, Marka: {Marka}, Model: {Model}, Przebieg: {Przebieg:F2} km, Średnia prędkość: {PredkoscSrednia} km/h, Czas podróży: {CzasPrzebiegu:F2} godzin.");
    }
}

public class Samochod : Pojazd
{
    public Samochod(string marka, string model) : base(marka, model, 80.0, "Samochód") { }
}

public class Rower : Pojazd
{
    public Rower(string marka, string model) : base(marka, model, 20.0, "Rower") { }
}

public class Motocykl : Pojazd
{
    public Motocykl(string marka, string model) : base(marka, model, 100.0, "Motocykl") { }
}

class Program
{
    static void Main()
    {
        List<Pojazd> pojazdy = new List<Pojazd>
        {
            new Samochod("Toyota", "Corolla"),
            new Rower("Merida", "Crossway"),
            new Motocykl("Harley Davidson", "Sportster")
        };

        foreach (var pojazd in pojazdy)
        {
            pojazd.Opis();
        }

        Console.WriteLine("\nPrzejechanie 20 km przez każdy pojazd:");
        foreach (var pojazd in pojazdy)
        {
            pojazd.Jedz(20.0);
        }

        Console.WriteLine("\nPo podróży:");
        foreach (var pojazd in pojazdy)
        {
            pojazd.Opis();
        }
    }
}
