import unittest
import math
from circle import area, perimeter

class CircleTestCase(unittest.TestCase):
    """
    Unit tests for circle geometry functions.

    Tests cover basic functionality, edge cases, and error handling
    for area and perimeter calculations.
    """
    
    def test_area_normal(self):
        """Test normal area calculation."""
        res = area(5)
        expected = math.pi * 25
        self.assertAlmostEqual(res, expected)
    
    def test_area_zero(self):
        """Test area calculation with zero radius."""
        res = area(0)
        self.assertEqual(res, 0)
    
    def test_area_negative(self):
        """Test area calculation with negative radius."""
        res = area(-5)
        expected = math.pi * 25
        self.assertAlmostEqual(res, expected)
    
    def test_area_float(self):
        """Test area calculation with floating point radius."""
        res = area(2.5)
        expected = math.pi * 6.25
        self.assertAlmostEqual(res, expected)
    
    def test_area_small_value(self):
        """Test area calculation with very small radius."""
        res = area(0.001)
        expected = math.pi * 0.000001
        self.assertAlmostEqual(res, expected, places=10)
    
    def test_perimeter_normal(self):
        """Test normal perimeter calculation."""
        res = perimeter(5)
        expected = 2 * math.pi * 5
        self.assertAlmostEqual(res, expected)
    
    def test_perimeter_zero(self):
        """Test perimeter calculation with zero radius."""
        res = perimeter(0)
        self.assertEqual(res, 0)
    
    def test_perimeter_negative(self):
        """Test perimeter calculation with negative radius."""
        res = perimeter(-5)
        expected = 2 * math.pi * -5
        self.assertAlmostEqual(res, expected)
    
    def test_perimeter_float(self):
        """Test perimeter calculation with floating point radius."""
        res = perimeter(2.5)
        expected = 2 * math.pi * 2.5
        self.assertAlmostEqual(res, expected)
    
    def test_perimeter_large_value(self):
        """Test perimeter calculation with large radius."""
        res = perimeter(1000)
        expected = 2 * math.pi * 1000
        self.assertAlmostEqual(res, expected)
    
    def test_math_pi_usage(self):
        """Verify that math.pi is used correctly."""
        self.assertTrue(math.isclose(area(1), math.pi))
        self.assertTrue(math.isclose(perimeter(1), 2 * math.pi))
