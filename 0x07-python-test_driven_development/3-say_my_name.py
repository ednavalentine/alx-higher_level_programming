#!/usr/bin/python3
"""Prints My name is first name last name"""


def say_my_name(first_name, last_name=""):
    """Check to see if the first and last name are strings"""
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
