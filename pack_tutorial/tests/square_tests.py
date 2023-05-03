# import unittest module
import unittest

# import find_answer module
from packaging_tutorial.example import find_answer

# create a test class that inherits from unittest.TestCase
class TestFindAnswer(unittest.TestCase):

    def test_find_answer_with_positive_numbers(self):
        # use self.assertEqual to check if the expected and actual values are equal
        self.assertEqual(find_answer(2, 3), 25) # (2 + 3) ** 2 = 25
        self.assertEqual(find_answer(5, 7), 144) # (5 + 7) ** 2 = 144

    def test_find_answer_with_negative_numbers(self):
        self.assertEqual(find_answer(-2, -3), 25) # (-2 + -3) ** 2 = 25
        self.assertEqual(find_answer(-5, -7), 144) # (-5 + -7) ** 2 = 144

    def test_find_answer_with_zero(self):
        self.assertEqual(find_answer(0, 0), 0) # (0 + 0) ** 2 = 0
        self.assertEqual(find_answer(0, 5), 25) # (0 + 5) ** 2 = 25
        self.assertEqual(find_answer(5, 0), 25) # (5 + 0) ** 2 = 25

if __name__ == '__main__':
    unittest.main()