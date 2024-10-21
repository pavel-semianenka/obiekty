
# Porównanie obiektowości w różnych językach programowania

## Opis projektu

Aplikacja **Porównanie obiektowości** to narzędzie, które pozwala użytkownikom porównać kluczowe pojęcia i przykłady implementacji programowania obiektowego (OOP) w różnych językach programowania. Dzięki graficznemu interfejsowi użytkownika (GUI) stworzonemu w oparciu o bibliotekę **Tkinter**, użytkownik może przeglądać przykłady kodów oraz informacje o OOP w wybranych językach programowania.

## Funkcje aplikacji
- **Kluczowe pojęcia obiektowości**: Prezentuje podstawowe zagadnienia programowania obiektowego, takie jak klasa, obiekt, enkapsulacja, dziedziczenie i polimorfizm.
- **Zalety programowania obiektowego**: Wyjaśnia korzyści wynikające z podejścia obiektowego w programowaniu, m.in. modularność, wielokrotne użycie kodu i łatwość w debugowaniu.
- **Przykłady kodów**: Użytkownik może przeglądać przykłady implementacji OOP w językach takich jak: C++, C#, Python, Java, Rust, PHP, JavaScript.
- **Interaktywność**: Użytkownik może wybierać z list rozwijanych dwa różne języki programowania i porównywać je równocześnie w osobnych panelach.

## Wymagania
- **Python**: Aplikacja wymaga zainstalowanego Pythona w wersji 3.x.
- **Tkinter**: Biblioteka GUI Tkinter, zazwyczaj instalowana domyślnie z Pythonem.
- **Pliki z przykładami kodów**: Pliki `cpp_example.cpp`, `csharp_example.cs`, `python_example.py`, `javascript_example.js`, `php_example.php`, `java_example.java`, `rust_example.rs`, które zawierają przykłady kodów dla poszczególnych języków.

## Instalacja

1. Skopiuj repozytorium na swój komputer:
   ```bash
   git clone https://github.com/uzytkownik/oop-comparison.git
   cd oop-comparison
   ```

2. Upewnij się, że masz zainstalowanego Pythona oraz Tkinter:
   ```bash
   python --version
   ```

3. Uruchom aplikację:
   ```bash
   python main.py
   ```

## Instrukcja użytkowania

1. Po uruchomieniu aplikacji, na górze okna zobaczysz kluczowe pojęcia i zalety obiektowości.
2. W dolnej części okna znajdują się dwa panele, po lewej i prawej stronie, w których można wybrać języki programowania z rozwijanych list.
3. Po wybraniu języka, w odpowiednim panelu pojawi się opis OOP dla tego języka oraz przykład kodu.
4. Użytkownik może łatwo porównać dwa języki obok siebie, zmieniając wybory w listach rozwijanych.

## Struktura projektu

```
obiekty/
│
├── cpp_example.cpp         # Przykład kodu w C++
├── csharp_example.cs       # Przykład kodu w C#
├── python_example.py       # Przykład kodu w Pythonie
├── javascript_example.js   # Przykład kodu w JavaScript
├── php_example.php         # Przykład kodu w PHP
├── java_example.java       # Przykład kodu w Javie
├── rust_example.rs         # Przykład kodu w Rust
├── main.py                 # Główny plik aplikacji
└── README.md               # Dokumentacja projektu
```

## Rozwój

W przyszłości planowane są następujące usprawnienia:
- Dodanie obsługi większej liczby języków programowania.
- Możliwość porównania dodatkowych aspektów obiektowości, takich jak zarządzanie pamięcią, czy wsparcie dla paradygmatów funkcyjnych.

## Licencja

Projekt dostępny na licencji MIT.

---

Dziękujemy za korzystanie z aplikacji **Porównanie obiektowości**!
