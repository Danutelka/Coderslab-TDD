import unittest
from kod import buzz_fizz, rok_przestepny, word_wrap

# zad 1
class BuzzFuzzTests(unittest.TestCase):
    def test_min_length(self):
        self.assertIsNone(buzz_fizz(17))
    def test_div_by_zero(self):
        self.assertRaises(ZeroDivisionError, buzz_fizz(0), 0)
    def test_literka(self):
        self.assertRaises(TypeError, buzz_fizz, 'a', 2)

# zad 2
# Napisz funkcję, która przyjmuje liczbę całkowitą (oznaczającą rok) i 
# zwraca True – jeżeli rok jest przestępny, False jeżeli nie. Napisz testy do tej funkcji.

class RokPrzestepnyTests(unittest.TestCase):
    def test_length(self):
        self.assertIsNotNone(rok_przestepny(1250))
    def test_true(self):
        self.assertEqual(rok_przestepny(2020), True)
    def test_false(self):
        self.assertEqual(rok_przestepny(2019), False)
    
# zad 3
# Napisz funkcję word_wrap(string, length), której zadaniem jest skrócić napis do podanej długości 
# (i dodanie na końcu wielokropka). Funkcja ma działać w taki sposób żeby, żadne słowo nigdy nie 
# zostało przecięte. Napisz testy do tej funkcji.

class WordWrapTests(unittest.TestCase):
    def test_to_be_ok(self):
        self.assertEqual(word_wrap("wszyscy mamy żle w głowach, że żyjemy", 3), 'wsz')

if __name__ == "__main__":
    unittest.main()