<?php
class Pojazd {
    protected $marka;
    protected $model;
    protected $przebieg;
    protected $predkoscSrednia;
    protected $czasPrzebiegu;
    protected $typPojazdu;

    public function __construct($marka, $model, $predkoscSrednia, $typPojazdu) {
        $this->marka = $marka;
        $this->model = $model;
        $this->przebieg = 0.0;
        $this->predkoscSrednia = $predkoscSrednia;
        $this->czasPrzebiegu = 0.0;
        $this->typPojazdu = $typPojazdu;
    }

    public function jedz($kilometry) {
        $this->przebieg += $kilometry;
        $czas = $kilometry / $this->predkoscSrednia;
        $this->czasPrzebiegu += $czas;
        echo "{$this->typPojazdu} {$this->marka} {$this->model} przejechał(a) {$kilometry} km w " . number_format($czas, 2) . " godzin.\n";
    }

    public function opis() {
        echo "Typ pojazdu: {$this->typPojazdu}, Marka: {$this->marka}, Model: {$this->model}, Przebieg: " . number_format($this->przebieg, 2) . " km, Średnia prędkość: {$this->predkoscSrednia} km/h, Czas podróży: " . number_format($this->czasPrzebiegu, 2) . " godzin.\n";
    }
}

class Samochod extends Pojazd {
    public function __construct($marka, $model) {
        parent::__construct($marka, $model, 80.0, "Samochód");
    }
}

class Rower extends Pojazd {
    public function __construct($marka, $model) {
        parent::__construct($marka, $model, 20.0, "Rower");
    }
}

class Motocykl extends Pojazd {
    public function __construct($marka, $model) {
        parent::__construct($marka, $model, 100.0, "Motocykl");
    }
}

// Przykładowe użycie
$pojazdy = [
    new Samochod("Toyota", "Corolla"),
    new Rower("Merida", "Crossway"),
    new Motocykl("Harley Davidson", "Sportster")
];

foreach ($pojazdy as $pojazd) {
    $pojazd->opis();
}

echo "\nPrzejechanie 20 km przez każdy pojazd:\n";
foreach ($pojazdy as $pojazd) {
    $pojazd->jedz(20.0);
}

echo "\nPo podróży:\n";
foreach ($pojazdy as $pojazd) {
    $pojazd->opis();
}
?>
