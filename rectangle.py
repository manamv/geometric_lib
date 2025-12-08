# def area(a, b): 
#     '''takes the modules of the perpendicular sides of the rectangle a (height), b (width), returns its area'''
#     return a * b 

# def perimeter(a, b): 
#     '''takes the modules of different sides of rectangle a, b, returns its perimeter'''
#     return 2 * (a + b)


# import unittest

# class RectangleTestCase(unittest.TestCase):
#     def test_zero_mul(self):
#         res = area(10, 0)
#         self.assertEqual(res, 0)

#     def test_square_mul(self):
#         res = area(10, 10)
#         self.assertEqual(res, 100)




def area(a: float, b: float) -> float:
    """
    Calculate the area of a rectangle.
    
    Takes the lengths of two perpendicular sides (height and width) 
    and returns the area of the rectangle.
    
    Parameters
    ----------
    a : float
        Length of the first side (height)
    b : float
        Length of the second side (width)
    
    Returns
    -------
    float
        Area of the rectangle: a * b
    """
    return a * b


def perimeter(a: float, b: float) -> float:
    """
    Calculate the perimeter of a rectangle.
    
    Takes the lengths of two different sides and returns 
    the perimeter of the rectangle.
    
    Parameters
    ----------
    a : float
        Length of the first side
    b : float
        Length of the second side
    
    Returns
    -------
    float
        Perimeter of the rectangle: 2 * (a + b)
    """
    return 2 * (a + b)