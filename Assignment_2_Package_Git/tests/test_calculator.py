"""Verification unit tests for geometry_toolkit."""

import math
import unittest

from geometry_toolkit.calculator import (
    circle_area,
    circle_perimeter,
    rectangle_area,
    rectangle_perimeter,
)


class TestGeometryToolkit(unittest.TestCase):
    def test_rectangle_area(self):
        self.assertEqual(rectangle_area(5, 3), 15.0)
        self.assertEqual(rectangle_area(1, 1), 1.0)
        self.assertEqual(rectangle_area(0, 10), 0.0)

    def test_rectangle_perimeter(self):
        self.assertEqual(rectangle_perimeter(5, 3), 16.0)
        self.assertEqual(rectangle_perimeter(1, 1), 4.0)

    def test_circle_area(self):
        self.assertAlmostEqual(circle_area(1), math.pi, places=4)
        self.assertAlmostEqual(circle_area(7), 153.93804, places=4)

    def test_circle_perimeter(self):
        self.assertAlmostEqual(circle_perimeter(1), 2 * math.pi, places=4)
        self.assertAlmostEqual(circle_perimeter(7), 43.98229, places=4)

    def test_negative_dimensions_raise_error(self):
        with self.assertRaises(ValueError):
            rectangle_area(-1, 5)
        with self.assertRaises(ValueError):
            circle_area(-5)


if __name__ == "__main__":
    unittest.main()
