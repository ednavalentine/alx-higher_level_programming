#!/usr/bin/python3
"""Adding an integer or float"""


def add_integer(a, b=98):
    """Checking if a, b is int or float"""
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")

    a = int(a) if isinstance(a, float) else a
    b = int(b) if isinstance(b, float) else b

    """Perform the addition"""
    return a + b
