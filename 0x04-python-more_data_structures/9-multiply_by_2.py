#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if isinstance(a_dictionary, dict):
        new_dict = {}
        for inkkey, keyvalue in a_dictionary.items():
            if isinstance(keyvalue, int):
                new_dict[inkkey] = keyvalue * 2
    return new_dict
