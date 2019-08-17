<img alt="Logo" src="http://coderslab.pl/svg/logo-coderslab.svg" width="400">

# TDD - Snippety

> Krótkie kawałki kodu, które pokazują zależności, rozwiązują popularne problemy oraz pokazują jak używać niektórych funkcji.

#### Jak napisać prosty test w Pythonie ?

Klasa użyta do testów powinna dziedziczyć po klasie `TestCase`, znajdującej się w module `unittest`
oraz posiadać publiczne metody zaczynające się od słowa `test`.  

```python
import unittest


class MyFirstTest(unittest.TestCase):
    def test_to_fail(self):
        self.assertTrue(False)  # ten test zawsze wyrzuci błąd...

    def test_to_be_ok(self):
        self.assertEqual(2 * 2, 4)  # ...a ten zawsze przejdzie.

```


#### Jakie rodzaje asercji są najczęściej stosowane?


```python
assertEqual(expected, actual)
assertNotEqual(expected, actual)
assertTrue(value)
assertFalse(value)
assertRaises(exc, fun, *args, **kwargs)
assertRaisesRegex(exc, r, fun, *args, **kwargs)
assertIsNone(value)
assertIsNotNone(value)
```

Pełna lista asercji: 
https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertEqual

#### Jak przygotować fikstury?

* metoda `setUp()`, wywoływana zawsze **przed** wykonaniem każdego testu:

```python
class TestExample1(unittest.TestCase):
    def setUp(self):
        self.padawan = Padawan.objects.create(name="Anakin", year_at_academy=1,
                                              is_active=True)
```

_Przed każdym testem w klasie testowej `TestExample1`, nadaj atrybutowi `padawan` wartość._

* metoda `tearDown()`, wywoływana zawsze **po** wykonaniu każdego testu:

```python
class TestExample1(unittest.TestCase): 
    
    # kontynuacja klasy TestExample1 z poprzedniego przykładu.

    def tearDown(self):
        self.padawan.delete()  # usuwamy padawana z bazy danych
        self.padawan = None    # przypisujemy None do atrybutu
```


#### Jak uruchomić testy?

* jeśli chcemy uruchomić zawierający test jednostkowe moduł o nazwie **test_module1**:

```console
python -m unittest test_module1
```

* jeśli chcemy uruchomić klasę **TestClass** zawartą w module **test_module1**:

```console
python -m unittest test_module1.TestClass
```

* jeśli chcemy uruchomić metodę **test_method()** zawartą w module **test_module1**, w klasie **TestClass**:

```console
python -m unittest test_module1.TestClass.test_method()
```

#### Jak ominąć konkretny test?

Testy omijamy używając dekoratora **@unittest.skip**

* jeśli chcemy bezwarunkowo ominąc test:

```python
@unittest.skip("komunikat")
def test_method_1(self):
    pass
```

* jeśli chcemy ominąć test, jeśli warunek **zostanie** spełniony:

```python
@unittest.skipIf(mylib.__version__ < (2, 0), "Nie wykonuje się w wersji < 2.0")
def test_method_2(self):
    pass
```

* jeśli chcemy ominąć test, jeśli warunek **nie zostanie** spełniony:

```python
@unittest.skipUnless(sys.paltform.startswith("win"), "tylko dla Windows")
def test_method_3(self):
    pass
```

#### Jak testować widoki Django?

Przed przetestowaniem widoku musimy użyć klienta, który "odpyta" nasz serwer i zwróci nam potrzebne dane do testowania. W tym celu
musimy użyć klasy **Client**:

```python
import unittest

from django.test import Client


class TestAcademy(unittest.TestClient):

    def setUp(self):
        """
        W metodzie `setUp()` skonfigurujemy klienta.
        """
        self.client = Client()

    def test_exam_results(self):

        # logujemy się jako admin, czyli mamy dostęp do wszystkiego
        self.client.login(username='yoda', password='Str0ng_is_da_F0rc3')

        # pobieramy wynik egzaminu ze strony
        response = self.client.get('/academy/exams/anakin.skywalker/')

        # testujemy, czy strona nas wpuściła?
        self.assertEqual(response.status_code, 200)
