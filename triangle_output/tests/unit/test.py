import unittest

from app import compute_perimeter, compute_area

class TestOutput(unittest.TestCase):
    def test_perimeter(self):
        result = compute_perimeter([3,4,5])
        self.assertEqual(result, 12.0)
    
    def test_area(self):
        result = compute_area([3,4,5])
        self.assertEqual(result, 6.0)
    
    
    if __name__ == '__main__':
        unittest.main()