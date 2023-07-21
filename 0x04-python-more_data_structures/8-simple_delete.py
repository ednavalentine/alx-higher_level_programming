#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if isinstance(a_dictionary, dict) and isinstance(key, str):
        if key in a_dictionary:
            del a_dictionary[key]
    return a_dictionary
