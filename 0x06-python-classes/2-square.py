#!/usr/bin/python3
"""Size valiation of class Square"""


class Square:
    """adding __init__ to create the validation for size"""
    def __init__(self, size=0):
        """Checking to see if size is an int


        Parameters:
        size (int): value of size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
