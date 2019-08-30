import unittest
from functions import analyze_pesel



if __name__ == "__main__":
    unittest.main()

03211949001
03291983500 19.09.2003

# zad 2


def analyze_pesel(pesel):
    weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    weight_index = 0
    digits_sum = 0
    for digit in pesel[:-1]:
        digits_sum += int(digit) * weights[weight_index]
        weight_index += 1
    pesel_modulo = digits_sum % 10
    validate = 10 - pesel_modulo
    if validate == 10:
        validate = 0
    gender = "male" if int(pesel[-2]) % 2 == 0 else "female"
    birth_date = datetime(int("19" + pesel[0:2]), int(pesel[2:4]),int(pesel[4:6]))
    result = {
        "pesel": pesel,
        "valid": validate == int(pesel[-1]),
        "gender": gender,
        "birth_date": birth_date
    }
    return result


class AnalyzePeselTests(unittest.TestCase):
    def test_validate_pesel(self):
        self.assertTrue(analyze_pesel('03211949001')['valid']), {
        "pesel": "03211949001",
        "valid": True,
        "gender": 'female',
        #"birth_date": datetime.datetime(2003, 01,19)
    })


class AnalyzePeselTests(unittest.TestCase):
    def test_validate_pesel(self):
        self.assertEqual(analyze_pesel('03211949001'), {
        "pesel": "03211949001",
        "valid": True,
        "gender": 'female',
        #"birth_date": datetime.datetime(2003, 01,19)
    })
