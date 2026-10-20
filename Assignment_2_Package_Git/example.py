"""Demonstration runner for foss-geometry-toolkit."""

from geometry_toolkit import (
    circle_area,
    circle_perimeter,
    rectangle_area,
    rectangle_perimeter,
)


def main() -> None:
    # Rectangle calculations (Initial release v0.1.0)
    rect_len, rect_wid = 5.0, 3.0
    print(
        f"Rectangle (Length: {rect_len}, Width: {rect_wid}): "
        f"Area = {rectangle_area(rect_len, rect_wid):.1f}, "
        f"Perimeter = {rectangle_perimeter(rect_len, rect_wid):.1f}"
    )

    # Circle calculations (Added in v0.2.0 after file checkout)
    radius = 7.0
    print(
        f"Circle (Radius: {radius}): "
        f"Area = {circle_area(radius):.2f}, "
        f"Circumference = {circle_perimeter(radius):.2f}"
    )


if __name__ == "__main__":
    main()
