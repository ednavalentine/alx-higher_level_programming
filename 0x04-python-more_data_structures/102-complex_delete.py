#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if isinstance(a_dictionary, dict):
        delkey = [key for key, val in a_dictionary.items() if val == value]
        for key in delkey:
            del a_dictionary[key]
    return a_dictionary
