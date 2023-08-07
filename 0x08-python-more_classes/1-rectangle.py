#!/usr/bin/python3
"""Definition of class Rectangle"""


class Rectangle:
    """intializting the class"""
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def height(self):
        """property to access and retrive the attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Checking if height is an int and greater than 0


        Parameter:
        height (int): height of rectangle
        """
        try:
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            if value < 0:
                raise TypeError("height must be >= 0")
            self.__height = value
        except (TypeError, ValueError) as e:
            raise TypeError(e)

    @property
    def width(self):
        """property to access and retrive the attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Checking if width is an int and greater than 0


        Parameter:
        width(int): width of rectangle
        """
        try:
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be >= 0")
            self.__width = value
        except (TypeError, ValueError) as e:
            raise TypeError(e)
