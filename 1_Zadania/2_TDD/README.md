<img alt="Logo" src="http://coderslab.pl/svg/logo-coderslab.svg" width="400">

# Test-driven development

### Zadanie 1 &ndash; rozwiązywane z wykładowcą.

Napisz, używając techniki TDD, funkcję o nazwie **calculate_vat**. Funkcja ma przyjmować cenę i stawkę VAT, a 
zwracać kwotę podatku.


---

### Zadanie 2.

Napisz, używając techniki TDD, funkcję o nazwie **hash_password**. Funkcja ma przyjmować hasło (w postaci zwykłego napisu), a 
zwrcacać hasz MD5 tegoż hasła. 

**Wymagania:**

* hasło ma mieć minimum 7 znaków,
* powinno zawierać:
    * przynajmniej jedną wielką literę,
    * przynajmniej jedną małą literę,
    * przynajmniej jedną cyfrę,
    * przynajmniej jeden znak specjalny z zakresu:
    `!@#$%^&*()_+-={}[]|\:";'<>?,./"`,
* funkcja ma zwrócić hasło zahaszowane przy użyciu algorytmu MD5 (sprawdź moduł **hashlib** w bibliotece standardowej),
* jeśli któryś z warunków hasła (długość, obecność odpowiednich znaków) nie został spełniony, funkcja ma zwrócić `None`.

**Hint:** może pomóc Ci funkcja `any()` (https://docs.python.org/3/library/functions.html#any).

### Zadanie 3.

Wyobraź sobie, że Twój klient, dla którego pisałeś funkcję w poprzednim zadaniu, zażądał zmiany w kodzie: hasło musi mieć przynajmniej 8 znaków. Zgodnie z zasadą TDD, popraw najpierw testy, a potem kod programu.
