"""Sample Python geometry toolkit package for FOSS assignment."""

from .calculator import (
    circle_area,
    circle_perimeter,
    rectangle_area,
    rectangle_perimeter,
)

__version__ = "0.2.0"
__all__ = [
    "rectangle_area",
    "rectangle_perimeter",
    "circle_area",
    "circle_perimeter",
]
