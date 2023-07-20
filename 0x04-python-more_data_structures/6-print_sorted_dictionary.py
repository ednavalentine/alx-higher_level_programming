#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sortkey = sorted(a_dictionary.keys())
    for inkkey in sortkey:
        print(f"{inkkey}: {a_dictionary[inkkey]}")
