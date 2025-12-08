from square import area, perimeter
import unittest

class SquareTestCase(unittest.TestCase):
    """
    Unit tests for square geometry functions.
    
    Tests cover basic functionality, edge cases, and error handling
    for area and perimeter calculations.
    """
    
    # Tests for area
    def test_area_normal(self):
        """Test normal area calculation."""
        res = area(5)
        self.assertEqual(res, 25)
    
    def test_area_zero(self):
        """Test area with zero side."""
        res = area(0)
        self.assertEqual(res, 0)
    
    def test_area_negative(self):
        """Test area with negative side."""
        res = area(-5)
        self.assertEqual(res, 25)
    
    def test_area_float(self):
        """Test area with floating point side."""
        res = area(2.5)
        self.assertEqual(res, 6.25)
    
    # Tests for perimeter
    def test_perimeter_normal(self):
        """Test normal perimeter calculation."""
        res = perimeter(5)
        self.assertEqual(res, 20)
    
    def test_perimeter_zero(self):
        """Test perimeter with zero side."""
        res = perimeter(0)
        self.assertEqual(res, 0)
    
    def test_perimeter_negative(self):
        """Test perimeter with negative side."""
        res = perimeter(-5)
        self.assertEqual(res, -20)
    
    def test_perimeter_float(self):
        """Test perimeter with floating point side."""
        res = perimeter(2.5)
        self.assertEqual(res, 10.0)
    
    def test_both_functions_same_input(self):
        """Test both functions with the same input."""
        a = 7
        self.assertEqual(area(a), 49)
        self.assertEqual(perimeter(a), 28)
