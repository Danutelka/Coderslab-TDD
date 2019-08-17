<img alt="Logo" src="http://coderslab.pl/svg/logo-coderslab.svg" width="400">

# Testy jednostkowe

### Zadanie 1 &ndash; rozwiązywane z wykładowcą.

Zapoznaj się z plikiem **functions.py**, znajdziesz w nim funkcję `div(a, b)`, która zwraca iloraz argumentów a i b.

1. Napisz testy jednostkowe, które przetestują tę funkcję:
    * sprawdź, czy funkcja dopuszcza dzielenie przez zero,
    * sprawdź, czy parametry przyjmowane przez funkcję to wyłącznie liczby.

2. W zależnosci od wyników testów, popraw funkcję `div()`.

---

### Zadanie 2.

W pliku **functions.py** znajduje się funkcja `analyze_pesel()`. Funkcja ta przyjmuje jeden parametr: numer PESEL, a zwraca słownik z następującymi kluczami:

* "pesel": wejściowy numer,
* "gender": płeć zakodowaną w numerze (male / female),
* "birth_date": datę urodzenia zakodowaną w numerze,
* "valid": czy numer jest poprawny.

Niestety – funkcja została napisana przez wyjątkowo niechlujnego programistę. Napisz testy jednostkowe, które sprawdzą, czy funkcja poprawnie
waliduje numery i czy zwraca poprawne dane. Pamiętaj, by przetestować numery osób urodzonych po 31 grudnia 1999 roku. Popraw ewentualne błędy.

#### Jeśli potrzebujesz pomocy, zajrzyj tutaj:

* https://pl.wikipedia.org/wiki/PESEL#Numer_PESEL – zasady walidacji numeru PESEL,
* http://pesel.felis-net.com – generator przykładowych numerów PESEL.
