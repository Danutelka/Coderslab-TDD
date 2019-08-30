import unittest
#import functions wtedy functions.div wywołanie
from functions import div, analyze_pesel
import datetime

class DivFunctionTest(unittest.TestCase):
    def test_div_by_zero(self):
        self.assertRaises(ZeroDivisionError, div, 5, 0)
    def test_div_four_by_two(self):
        self.assertEqual(div('4','2'), 2)
    def test_str_nymber(self):
        self.assertEqual(div('4','2'), 2)
    def test_div_float(self):
        self.assertEqual(div(4,2.5), 1.6)
    #def test_literka(self):
        #self.assertRaises(TypeError, div, 'a', 2)

class AnalyzePeselTests(unittest.TestCase):
    def test_validate_pesel(self):
        self.assertTrue(analyze_pesel('03211949001')['valid'])
    def test_valid_pesel_gender(self):
        self.assertEqual(analyze_pesel('03211949001')['gender'], 'female')
    def test_pesel(self):
        self.assertEqual(analyze_pesel('03211949001')['pesel'], '03211949001')  
    #def test_birth_date(self):
        #self.assertEqual(analyze_pesel('03211949001')['birth_date'], datetime.datetime[2003, 01, 19])


if __name__ == "__main__":
    unittest.main()