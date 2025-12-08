from triangle import area, perimeter
import unittest

class TriangleTestCase(unittest.TestCase):
    """
    Unit tests for triangle geometry functions.
    
    Tests cover basic functionality, edge cases, and error handling
    for area and perimeter calculations.
    """
    
    def test_area_normal(self):
        """Test normal area calculation."""
        res = area(10, 5)
        self.assertEqual(res, 25)
    
    def test_area_zero_base(self):
        """Test area with zero base."""
        res = area(0, 5)
        self.assertEqual(res, 0)
    
    def test_area_zero_height(self):
        """Test area with zero height."""
        res = area(10, 0)
        self.assertEqual(res, 0)
    
    def test_area_float(self):
        """Test area with floating point values."""
        res = area(4.5, 3.2)
        self.assertEqual(res, 7.2)
    
    def test_area_negative(self):
        """Test area with negative values."""
        res = area(-6, 4)
        self.assertEqual(res, -12)
    
    def test_perimeter_normal(self):
        """Test normal perimeter calculation."""
        res = perimeter(3, 4, 5)
        self.assertEqual(res, 12)
    
    def test_perimeter_zero_side(self):
        """Test perimeter with one zero side."""
        res = perimeter(0, 4, 5)
        self.assertEqual(res, 9)
    
    def test_perimeter_all_zero(self):
        """Test perimeter with all sides zero."""
        res = perimeter(0, 0, 0)
        self.assertEqual(res, 0)
    
    def test_perimeter_float(self):
        """Test perimeter with floating point sides."""
        res = perimeter(2.5, 3.5, 4.5)
        self.assertEqual(res, 10.5)
    
    def test_perimeter_negative(self):
        """Test perimeter with negative sides."""
        res = perimeter(-3, -4, -5)
        self.assertEqual(res, -12)
    
    def test_perimeter_equilateral(self):
        """Test perimeter of equilateral triangle."""
        res = perimeter(5, 5, 5)
        self.assertEqual(res, 15)
    
    def test_perimeter_isosceles(self):
        """Test perimeter of isosceles triangle."""
        res = perimeter(5, 5, 3)
        self.assertEqual(res, 13)
