# Modified after checking out the file using Git.
"""2D geometric dimension and area computation functions."""

import math


def rectangle_area(length: float, width: float) -> float:
    """Calculate and return the area of a rectangle."""
    if length < 0 or width < 0:
        raise ValueError("Dimensions must be non-negative.")
    return float(length * width)


def rectangle_perimeter(length: float, width: float) -> float:
    """Calculate and return the perimeter of a rectangle."""
    if length < 0 or width < 0:
        raise ValueError("Dimensions must be non-negative.")
    return float(2 * (length + width))


def circle_area(radius: float) -> float:
    """Calculate and return the area of a circle."""
    if radius < 0:
        raise ValueError("Radius must be non-negative.")
    return float(math.pi * (radius ** 2))


def circle_perimeter(radius: float) -> float:
    """Calculate and return the circumference (perimeter) of a circle."""
    if radius < 0:
        raise ValueError("Radius must be non-negative.")
    return float(2 * math.pi * radius)
