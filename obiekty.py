"""
MIT License

Copyright (c) 2024 Pavel Semianenka

This software is released under the MIT License.
https://opensource.org/licenses/MIT

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

    1. The above copyright notice and this permission notice shall be included
       in all copies or substantial portions of the Software.

    2. THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
       OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
       MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
       IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
       CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
       TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
       SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

import tkinter as tk
from tkinter import ttk

# Funkcja do wczytywania przykładu kodu z pliku
def read_code_example(filename):
    try:
        with open(filename, "r", encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return f"Błąd: Plik {filename} nie został znaleziony."


# Wczytujemy zawartość plików z kodami dla języków
cpp_example = read_code_example("cpp_example.cpp")
csharp_example = read_code_example("csharp_example.cs")

# Sekcja "Kluczowe pojęcia obiektowości"
core_oop_concepts = """Kluczowe pojęcia obiektowości:
- **Klasa**: Definicja zbioru atrybutów i metod, które reprezentują obiekt.
- **Obiekt**: Instancja klasy, która posiada cechy i zachowania zdefiniowane w klasie.
- **Enkapsulacja**: Ukrywanie wewnętrznej implementacji i udostępnianie tylko niezbędnych elementów przez interfejs.
- **Dziedziczenie**: Możliwość tworzenia nowych klas na podstawie już istniejących, co umożliwia wielokrotne użycie kodu.
- **Polimorfizm**: Zdolność różnych obiektów do używania tej samej metody, ale z różną implementacją."""

# Sekcja "Zalety obiektowości"
oop_advantages = """Zalety obiektowości:
- **Modularność**: Kod jest podzielony na mniejsze, niezależne moduły, co ułatwia zarządzanie projektem.
- **Wielokrotne użycie kodu**: Możliwość ponownego wykorzystania istniejących klas dzięki dziedziczeniu.
- **Łatwiejsze debugowanie i rozwój**: Enkapsulacja ogranicza bezpośredni dostęp do danych, co zmniejsza ryzyko błędów.
- **Elastyczność**: Polimorfizm umożliwia używanie różnych implementacji bez konieczności zmiany kodu wywołującego."""

info = {
    "C++": f"C++ jest językiem kompilowanym, wspierającym obiektowość przez klasy, dziedziczenie, enkapsulację i polimorfizm. Oferuje silne typowanie oraz złożoną hierarchię klas, co pozwala na efektywne zarządzanie pamięcią i zasobami.\n\nPrzykład kodu w C++:\n\n```cpp\n\n{read_code_example('cpp_example.cpp')}\n```",
    "C#": f"C# to język stworzony przez Microsoft, który jest w pełni obiektowy. Używa on klas i obiektów do reprezentowania danych oraz wspiera silną typizację i dziedziczenie. Oferuje także zaawansowane funkcje, takie jak LINQ i asynchroniczność, co czyni go elastycznym narzędziem do tworzenia aplikacji.\n\nPrzykład kodu w C#:\n\n```csharp\n\n{read_code_example('csharp_example.cs')}\n```",
    "Python": f"Python jest językiem interpretowanym, który ma prostą i zwięzłą składnię. Obsługuje obiektowość przez klasy i obiekty oraz dynamiczne typowanie. Jego elastyczność i bogata biblioteka czynią go idealnym do szybkiego prototypowania i rozwoju aplikacji.\n\nPrzykład kodu w Pythonie:\n\n```python\n\n{read_code_example('python_example.py')}\n```",
    "JavaScript": f"JavaScript jest językiem skryptowym, który obsługuje obiektowość przez prototypy, a nie klasy. Wspiera obiektowe podejście, chociaż różni się od tradycyjnych języków obiektowych, takich jak C++ czy Java. Jego zdolność do łączenia programowania obiektowego z funkcjonalnym czyni go bardzo wszechstronnym.\n\nPrzykład kodu w JavaScript:\n\n```javascript\n\n{read_code_example('javascript_example.js')}\n```",
    "PHP": f"PHP jest językiem skryptowym, który wspiera programowanie obiektowe od wersji 5.0. Umożliwia tworzenie klas, obiektów oraz używanie mechanizmów dziedziczenia i polimorfizmu. PHP jest szczególnie popularny w tworzeniu aplikacji webowych, co wyróżnia go na tle innych języków obiektowych.\n\nPrzykład kodu w PHP:\n\n```php\n\n{read_code_example('php_example.php')}\n```",
    "Java": f"Java jest językiem w pełni obiektowym, w którym wszystko jest obiektem. Kluczową cechą Javy jest dziedziczenie i polimorfizm. Java zapewnia bezpieczne zarządzanie pamięcią przez zbieranie śmieci i wprowadza rygorystyczne zasady dotyczące typów danych.\n\nPrzykład kodu w Javie:\n\n```java\n\n{read_code_example('java_example.java')}\n```",
    "Rust": f"Rust, mimo że nie jest tradycyjnie uważany za w pełni obiektowy, wspiera koncepcje obiektowości, takie jak enkapsulacja i polimorfizm. Jego unikalne podejście do zarządzania pamięcią bez użycia zbierania śmieci oraz silne typowanie sprawiają, że jest idealnym wyborem do tworzenia wydajnych i bezpiecznych aplikacji.\n\nPrzykład kodu w Rust:\n\n```rust\n\n{read_code_example('rust_example.rs')}\n```"
}

# Funkcja do aktualizacji tekstu w panelu na podstawie wybranego języka
def update_text(panel_text, selected_language):
    panel_text.config(state="normal")  # Włącz edycję Text widget
    panel_text.delete(1.0, tk.END)     # Wyczyść poprzednią treść
    panel_text.insert(tk.END, info.get(selected_language, "Brak informacji"))  # Wstaw nowy tekst
    panel_text.config(state="disabled") # Wyłącz edycję

# Tworzymy główne okno aplikacji
root = tk.Tk()
root.title("Porównanie obiektowości")
root.geometry("1280x720")  # Ustawiamy domyślny rozmiar okna na 1280x720
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.rowconfigure(0, weight=1)

# Tworzymy ramkę na górny panel (z kluczowymi pojęciami)
top_panel = tk.Frame(root, padx=10, pady=10)
top_panel.grid(row=0, column=0, columnspan=2, sticky="nsew")
#top_panel.grid_propagate(0)  # Zapobiegaj automatycznemu dostosowywaniu rozmiaru
# Ustaw maksymalną wysokość górnego panelu (przyjmując, że wysokość jednego wiersza to około 20 pikseli)
top_panel.config(height=240)  # Około 12 wierszy po 20 pikseli każdy
root.grid_rowconfigure(0, weight=0)  # Ustawienie wagi, aby panel rozciągał się

# Tworzymy tekstowy widget dla górnego panelu
top_text = tk.Text(top_panel, wrap="word", state="normal", height=12)  # Ustaw wysokość na 12 wierszy
top_text.insert(tk.END, f"{core_oop_concepts}\n\n{oop_advantages}")
top_text.config(state="disabled")
top_text.pack(fill="both", expand=True)

# Tworzymy ramki na lewy i prawy panel
left_panel = tk.Frame(root, padx=10, pady=10)
right_panel = tk.Frame(root, padx=10, pady=10)
left_panel.grid(row=1, column=0, sticky="nsew")
right_panel.grid(row=1, column=1, sticky="nsew")

# Konfiguracja rozszerzalności paneli
root.grid_rowconfigure(1, weight=1)  # Umożliwienie dolnym panelom zajmowania większej przestrzeni

# Ustaw wagę dla kolumn z panelami języków
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# Tworzymy listę wyboru dla lewego i prawego panelu
languages = list(info.keys())

# Lewy panel
left_label = tk.Label(left_panel, text="Wybierz język (lewy panel):")
left_label.pack(anchor="w")
left_choice = ttk.Combobox(left_panel, values=languages, state="readonly")
left_choice.pack(fill="x")
left_text = tk.Text(left_panel, wrap="word", state="disabled", width=40, height=15)
left_text.pack(fill="both", expand=True, pady=10)

# Prawy panel
right_label = tk.Label(right_panel, text="Wybierz język (prawy panel):")
right_label.pack(anchor="w")
right_choice = ttk.Combobox(right_panel, values=languages, state="readonly")
right_choice.pack(fill="x")
right_text = tk.Text(right_panel, wrap="word", state="disabled", width=40, height=15)
right_text.pack(fill="both", expand=True, pady=10)

# Ustawienie domyślnych wyborów w dropdownach i aktualizacja paneli
left_choice.set("C++")
right_choice.set("C#")
update_text(left_text, "C++")
update_text(right_text, "C#")

# Aktualizujemy tekst w panelu przy zmianie wyboru w dropdown
left_choice.bind("<<ComboboxSelected>>", lambda event: update_text(left_text, left_choice.get()))
right_choice.bind("<<ComboboxSelected>>", lambda event: update_text(right_text, right_choice.get()))

# Uruchamiamy główną pętlę aplikacji
root.mainloop()
