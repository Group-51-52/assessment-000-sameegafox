class MyTestCases:
    def test_check_number_odd_number(self):
        number = 3
        assert number % 2 != 0, f"{number} should be odd."

    def test_check_number_even_number(self):
        number = 4
        assert number % 2 == 0, f"{number} should be even."

    def test_check_number_negative_even_number(self):
        number = -2
        assert number % 2 == 0, f"{number} should be negative even."

    def test_check_number_negative_odd_number(self):
        number = -3
        assert number % 2 != 0, f"{number} should be negative odd."

    def test_check_number_neutral(self):
        number = 0
        assert number == 0, f"{number} should be neutral (zero)."

import unittest
from check_number import check_number   # type: ignore

class MyTestCases(unittest.TestCase):
    
    def test_check_number_odd(self):
        self.assertEqual(check_number(3), 'Weird')
        self.assertEqual(check_number(7), 'Weird')

    def test_check_number_even_2_to_5(self):
        self.assertEqual(check_number(2), 'Not Weird')
        self.assertEqual(check_number(4), 'Not Weird')

    def test_check_number_even_6_to_20(self):
        self.assertEqual(check_number(6), 'Weird')
        self.assertEqual(check_number(10), 'Weird')
        self.assertEqual(check_number(20), 'Weird')

    def test_check_number_even_above_20(self):
        self.assertEqual(check_number(22), 'Not Weird')

    def test_check_number_negative(self):
        self.assertEqual(check_number(-2), 'Very Weird')
        self.assertEqual(check_number(-1), 'Extremely Weird')

    def test_check_number_neutral(self):
        self.assertEqual(check_number(0), 'Very Weird')

if __name__ == '__main__':
    unittest.main()
