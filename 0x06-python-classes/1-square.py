#!/usr/bin/python3
"""Write a class Square with size as a private attribute"""


class Square:
    """Using __init__ to make size a private attribute with self"""
    def __init__(self, size):
        """added __ to size to make it private"""
        self.__size = size
