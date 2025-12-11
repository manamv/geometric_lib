import math


def area(r: float) -> float:
    """
    Calculate the area of a circle.
    
    Takes the radius of a circle and returns its area.
    
    Parameters
    ----------
    r : float
        Radius of the circle
    
    Returns
    -------
    float
        Area of the circle: π × r²
    """
    return math.pi * r * r


def perimeter(r: float) -> float:
    """
    Calculate the perimeter (circumference) of a circle.
    
    Takes the radius of a circle and returns its perimeter.
    
    Parameters
    ----------
    r : float
        Radius of the circle
    
    Returns
    -------
    float
        Perimeter of the circle: 2 × π × r
    """
    return 2 * math.pi * r
