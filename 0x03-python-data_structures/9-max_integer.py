#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    num_max = my_list[0]
    for number in my_list:
        if number > num_max:
            num_max = number
    return num_max
