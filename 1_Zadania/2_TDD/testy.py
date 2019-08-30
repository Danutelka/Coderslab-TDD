import unittest
import hashlib
from code import hash_password

class HashPasswordTestCase(unittest.TestCase):
    def test_function_usage(self):
        hash_password('haslo123')
        
    def test_password_min_length(self):
        self.assertIsNone(hash_password('H4$lo'))
        self.assertIsNotNone(hash_password('H4$lo43'))

    def test_password_min_one_uppercase_letter(self):
        self.assertIsNone(hash_password('h4$lo43'))
        self.assertIsNotNone(hash_password('H4$lo43'))

    def test_password_min_one_lowercase_letter(self):
        self.assertIsNone(hash_password('H4$LO43'))
        self.assertIsNotNone(hash_password('H4$lo43'))

    def test_password_min_one_digit(self):
        self.assertIsNone(hash_password('HD$LoAB'))
        self.assertIsNotNone(hash_password('H4$lo43'))

    def test_password_min_one_special_character(self):
        self.assertIsNone(hash_password('HDRLoA5'))
        self.assertIsNotNone(hash_password('H4$lo43'))

    def test_password_hash_correctness(self):
        m = hashlib.md5()
        m.update(b'H4$lo43')
        self.assertEqual(hash_password('H4$lo43'), m.hexdigest())

if __name__ == "__main__":
    unittest.main()