#!/usr/bin/python3
def raise_exception():
    value = 15
    try:
        value += "Hello"
    except TypeError as h:
        raise h
