import unittest
from circles import circle_area
from math import pi

'''
To run the tests, enter the directory of the tests.

Specifically run test_cirlces:
$ python3 -m unittest test_cirlces

Run any test in the directory:
$ python3 -m unittest
'''
class TestCircleArea(unittest.TestCase):
    def test_area(self):
        # test radius >= 0
        self.assertAlmostEqual(circle_area(1), pi)
        self.assertAlmostEqual(circle_area(0), 0)
        self.assertAlmostEqual(circle_area(2.1), pi * 2.1**2)
    
    def test_values(self):
        # test correct value errors are raised
        self.assertRaises(ValueError, circle_area, -2)
    
    def test_types(self):
        # test correct type errors are raised
        self.assertRaises(TypeError, circle_area, "2")
        self.assertRaises(TypeError, circle_area, [2, 3])
        self.assertRaises(TypeError, circle_area, 3+5j)
        self.assertRaises(TypeError, circle_area, True)
        self.assertRaises(TypeError, circle_area, {2:0, 4:9})