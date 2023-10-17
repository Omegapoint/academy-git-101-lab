#!/usr/bin/env python

import unittest
import calc


class TestCalc(unittest.TestCase):

    def test_add_numbers(self):
        self.assertEqual(calc.add([1, 1]), 2)
        self.assertEqual(calc.add([1, 2, 3, 4]), 10)
    
    def test_add_one_number(self):
        self.assertEqual(calc.add([1]), 1)
        self.assertEqual(calc.add([99]), 99)

    def test_multiply_numbers(self):
        self.assertEqual(calc.multiply([2, 2]), 4)
        self.assertEqual(calc.multiply([1, 2, 3, 4]), 24)
    
    def test_multiply_one_number(self):
        self.assertEqual(calc.multiply([1]), 1)
        self.assertEqual(calc.multiply([99]), 99)

    def test_divide_numbers(self):
        self.assertEqual(calc.divide([4, 2]), 2.0)
        self.assertEqual(calc.divide([9, 3]), 3.0)

    def test_division_by_zero(self):
        with self.assertRaises(ValueError):
            calc.divide([4, 0])

    def test_divide_with_one_number(self):
        with self.assertRaises(ValueError):
            calc.divide([4])

    def test_divide_with_three_numbers(self):
        with self.assertRaises(ValueError):
            calc.divide([4, 2, 1])
    
    def test_subtract_numbers(self):
        self.assertEqual(calc.subtract([4, 2]), 2)
        self.assertEqual(calc.subtract([10, 2, 3]), 5)
    
    def test_subtract_one_number(self):
        self.assertEqual(calc.subtract([1]), 1)
        self.assertEqual(calc.subtract([99]), 99)

    def test_exponentiate_numbers(self):
        self.assertEqual(calc.expo([2, 2]), 4)
        self.assertEqual(calc.expo([3, 3]), 27)

    def test_exponentiate_non_integer(self):
        self.assertEqual(calc.expo([4, 0.5]), 2)

    def test_exponentiate_negative_number(self):
        self.assertEqual(calc.expo([2, -3]), 0.125)

    def test_exponentiate_with_one_number(self):
        with self.assertRaises(ValueError):
            calc.expo([2])

    def test_exponentiate_with_three_numbers(self):
        with self.assertRaises(ValueError):
            calc.expo([2, 3, 4])

    def test_square_number(self):
        self.assertEqual(calc.square([2]), 4.0)
        self.assertEqual(calc.square([4]), 16.0)

    def test_calc_square_root(self):
        self.assertEqual(calc.sqrt([4]), 2)
        self.assertEqual(calc.sqrt([8]), 2.8284271247461903)

if __name__ == '__main__':
    unittest.main()
# comment
# comment
#a
