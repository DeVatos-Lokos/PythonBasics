import unittest
import random
from loops import NaturalNumbers

class TestNaturalNumbers(unittest.TestCase):

    def setUp(self):
        self.n = random.randint(0, 50)
        self.natural_numbers = NaturalNumbers()

    def test_get_first_n_for(self):
        first_n = [i for i in range(self.n)]
        self.assertEqual(
            first_n,
            self.natural_numbers.get_first_n_for(self.n)
        )

    def test_get_first_n_while(self):
        first_n = [i for i in range(self.n)]
        self.assertEqual(
            first_n,
            self.natural_numbers.get_first_n_while(self.n)
        )

    def test_get_first_n_pair_for(self):
        first_n = [i for i in range(0, self.n, 2)]
        self.assertEqual(
            first_n,
            self.natural_numbers.get_first_n_pair_for(self.n)
        )

    def test_get_first_n_pair_while(self):
        first_n = [i for i in range(0, self.n, 2)]
        self.assertEqual(
            first_n,
            self.natural_numbers.get_first_n_pair_while(self.n)
        )

    def test_get_factorial_for(self):
        self.assertEqual(
            self.natural_numbers.get_factorial_recursive(self.n),
            self.natural_numbers.get_factorial_for(self.n)
        )

    def test_get_factorial_while(self):
        self.assertEqual(
            self.natural_numbers.get_factorial_recursive(self.n),
            self.natural_numbers.get_factorial_while(self.n)
        )

    def test_get_n_pow_2_for(self):
        first_n = [i ** 2 for i in range(0, self.n)]
        self.assertEqual(
            first_n,
            self.natural_numbers.get_n_pow_2_for(self.n)
        )

    def test_get_n_pow_2_while(self):
        first_n = [i ** 2 for i in range(0, self.n)]
        self.assertEqual(
            first_n,
            self.natural_numbers.get_n_pow_2_while(self.n)
        )
    
    def test_get_n_sum_for(self):
        self.assertEqual(
            self.natural_numbers.get_n_sum_recursive(self.n),
            self.natural_numbers.get_n_sum_for(self.n)
        )

    def test_get_n_sum_while(self):
        self.assertEqual(
            self.natural_numbers.get_n_sum_recursive(self.n),
            self.natural_numbers.get_n_sum_while(self.n)
        )

if __name__ == '__main__':
    unittest.main()
