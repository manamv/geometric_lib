import unittest
from rectangle import area, perimeter 

class RectangleTestCase(unittest.TestCase):
    """
    Unit tests for rectangle geometry functions.
    
    Tests cover basic functionality, edge cases, and error handling
    for area and perimeter calculations.
    """
    
    def test_area_zero_mul(self):
        """Test area calculation when one side is zero."""
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_area_square_mul(self):
        """Test area calculation for a square (equal sides)."""
        res = area(10, 10)
        self.assertEqual(res, 100)
    
    def test_area_normal(self):
        """Test normal area calculation with different sides."""
        res = area(5, 7)
        self.assertEqual(res, 35)
    
    def test_area_negative(self):
        """Test area calculation with negative side length."""
        res = area(-5, 3)
        self.assertEqual(res, -15)
    
    def test_perimeter_normal(self):
        """Test normal perimeter calculation."""
        res = perimeter(5, 7)
        self.assertEqual(res, 24)
    
    def test_perimeter_zero(self):
        """Test perimeter calculation with zero side."""
        res = perimeter(0, 10)
        self.assertEqual(res, 20)
    
    def test_perimeter_square(self):
        """Test perimeter calculation for a square."""
        res = perimeter(10, 10)
        self.assertEqual(res, 40)
    
    def test_perimeter_negative(self):
        """Test perimeter calculation with negative side length."""
        res = perimeter(-5, 3)
        self.assertEqual(res, -4)
