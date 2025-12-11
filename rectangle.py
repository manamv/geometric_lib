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
