import unittest
from fractions import Fraction

from app import checker

class TestChecker(unittest.TestCase):
    def test_checker(self):
        result = checker([3,4,5])
        self.assertTrue(result)
        
    def test_checker_fraction(self):
        x = Fraction(5, 13)
        y = Fraction(12, 13)
        z = 1
        result = checker([x,y,z])
        self.assertTrue(result)
    
    def test_checker_zero(self):
        result = checker([0,0,0])
        self.assertFalse(result)
        
    def test_checker_5_items(self):
        result = checker([1,2,3,4,5])
        self.assertFalse(result)
    
    def test_checker_not_a_triangle(self):
        result = checker([8,1,9])
        self.assertFalse(result)
        
    if __name__ == '__main__':
        unittest.main()