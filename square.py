# def area(a):
#     '''takes the module of side of square a, returns its area'''
#     return a * a


# def perimeter(a):
#     '''takes the module of side of square a, returns its perimeter'''
#     return 4 * a




def area(a: float) -> float:
    """
    Calculate the area of a square.
    
    Takes the length of a side and returns the area of the square.
    
    Parameters
    ----------
    a : float
        Length of the square's side
    
    Returns
    -------
    float
        Area of the square: a * a
    """
    return a * a


def perimeter(a: float) -> float:
    """
    Calculate the perimeter of a square.
    
    Takes the length of a side and returns the perimeter of the square.
    
    Parameters
    ----------
    a : float
        Length of the square's side
    
    Returns
    -------
    float
        Perimeter of the square: 4 * a
    """
    return 4 * a