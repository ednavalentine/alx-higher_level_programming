#!/usr/bin/python3
"""Area of the square of class Square"""


class Square:
    """using __init__ to make the size validation"""
    def __init__(self, size=0):
        """Checking to see if size is an int & greater than 0


        Parameter:
        size (int): area of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """finding the area of a square"""
        return (self.__size * self.__size)
