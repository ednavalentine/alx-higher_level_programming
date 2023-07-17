#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return None
    else:
        for ink in reversed(my_list):
            print(str.format("{:d}", ink))
