#!/usr/bin/python3
"""This module provides an integer addition function.

It accepts integers or floats and raises TypeError for other values.
Float values are converted to integers before addition.
The public function is add_integer.
"""


def add_integer(a, b=98):
    """Return the integer addition of a and b.

    Floats are cast to integers before addition.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
