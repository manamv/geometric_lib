# def area(a, h): 
#     '''takes the modulus of the base (side) a and the modulus of the height h, drawn to this base of the triangle, returns its area'''
#     return a * h / 2 

# def perimeter(a, b, c): 
#     '''takes the nodules of sides of a triangle a, b, c, returns its perimeter'''
#     return a + b + c 



def area(a: float, h: float) -> float:
    """
    Calculate the area of a triangle.
    
    Takes the length of the base and the height drawn to this base.
    
    Parameters
    ----------
    a : float
        Length of the triangle's base
    h : float
        Height drawn to the base
    
    Returns
    -------
    float
        Area of the triangle: a * h / 2
    """
    return a * h / 2


def perimeter(a: float, b: float, c: float) -> float:
    """
    Calculate the perimeter of a triangle.
    
    Takes the lengths of three sides of a triangle.
    
    Parameters
    ----------
    a : float
        Length of the first side
    b : float
        Length of the second side
    c : float
        Length of the third side
    
    Returns
    -------
    float
        Perimeter of the triangle: a + b + c
    """
    return a + b + c