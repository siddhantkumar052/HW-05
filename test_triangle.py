"""
Name: Siddhantkumar Maske
Cwid:20006862
Subject: SSW 567
HW 05 - Static Code Analysis
"""
import unittest
from triangle_program import classify_triangle


class Testtriangles(unittest.TestCase):
    'This class contains all the tests for the classify triangle program'

    def test_invalid_input_1(self):
        'This is test case 1'
        self.assertEqual(classify_triangle(3, 4, 0), 'InvalidInput')

    def test_invalid_input_2(self):
        'This is test case 2'
        self.assertEqual(classify_triangle(-1, -4, 5), 'InvalidInput')

    def test_invalid_input_3(self):
        'This is test case 3'
        self.assertNotEqual(classify_triangle(3, 4, 5), 'InvalidInput')

    def test_not_a_triangle_4(self):
        'This is test case 4'
        self.assertEqual(classify_triangle(10, 2, 3), 'NotATriangle')

    def test_not_a_triangle_5(self):
        'This is test case 5'
        self.assertNotEqual(classify_triangle(3, 4, 5), 'NotATriangle')

    def test_not_a_triangle_6(self):
        'This is test case 6'
        self.assertNotEqual(classify_triangle(5, 5, 8), 'NotATriangle')

    def test_right_triangle_7(self):
        'This is test case 7'
        self.assertEqual(classify_triangle(3, 4, 5), 'Right')

    def test_right_triangle_8(self):
        'This is test case 8'
        self.assertNotEqual(classify_triangle(11, 11, 10), 'Right')

    def test_equilateral_triangle_9(self):
        'This is test case 9'
        self.assertEqual(classify_triangle(5, 5, 5), 'Equilateral')

    def test_equilateral_triangle_10(self):
        'This is test case 10'
        self.assertEqual(classify_triangle(4, 4, 4), 'Equilateral')

    def test_equilateral_triangle_11(self):
        'This is test case 11'
        self.assertNotEqual(classify_triangle(4, 8, 10), 'Equilateral')

    def test_isosceles_triangle_12(self):
        'This is test case 12'
        self.assertEqual(classify_triangle(4, 4, 5), 'Isosceles')

    def test_isosceles_triangle_13(self):
        'This is test case 13'
        self.assertEqual(classify_triangle(5, 5, 8), 'Isosceles')

    def test_isosceles_triangle_14(self):
        'This is test case 14'
        self.assertNotEqual(classify_triangle(10, 10, 10), 'Isosceles')

    def test_scalene_triangle_15(self):
        'This is test case 15'
        self.assertEqual(classify_triangle(4, 8, 10), 'Scalene')

    def test_scalene_triangle_16(self):
        'This is test case 16'
        self.assertEqual(classify_triangle(5, 9, 11), 'Scalene')

    def test_scalene_triangle_17(self):
        'This is test case 17'
        self.assertNotEqual(classify_triangle(10, 10, 10), 'Scalene')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
