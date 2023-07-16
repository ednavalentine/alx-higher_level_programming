#!/usr/bin/python3
def no_c(my_string):
    res = ""
    for ink in my_string:
        if ink not in ('c', 'C'):
            res += ink
    return res
