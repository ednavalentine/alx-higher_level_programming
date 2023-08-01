#!/usr/bin/python3
"""Printing a square"""


class Square:
    """using __init__ to make the size validation"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """property to access and retrive the private attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """Checking to see if size is an int & greater than 0


        Parameter:
        size (int): area of the square
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """finding the area of a square"""
        return (self.__size * self.__size)

    def my_print(self):
        """Prints in stdout the square with # character"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
