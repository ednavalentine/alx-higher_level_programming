#!/usr/bin/python3
"""Definition of class Rectangle"""


class Rectangle:
    """intializting the class"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

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
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculating the rectangle's area"""
        return self.__width * self.__height

    def perimeter(self):
        """Calculating the rectangle's perimeter"""
        return 2 * (self.__width + self.__height) \
            if self.__width != 0 and self.__height != 0 else 0

    def rectangle_drawn(self):
        """Checking if the width and height values are strings"""
        rectangle_str = ""
        for ink in range(self.__height):
            for clm in range(self.__width):
                rectangle_str += str(self.print_symbol)
            if self.__width != 0 and ink < (self.__height - 1):
                rectangle_str += "\n"
        return rectangle_str

    def __str__(self):
        """returns rectangle_drawn"""
        return self.rectangle_drawn()

    def __repr__(self):
        """Check for string representation"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Add Bye rectangle when the class Rectangle is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
