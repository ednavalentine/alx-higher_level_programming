#!/usr/bin/python3
def uniq_add(my_list=[]):
    inkint = set()
    for ink in my_list:
        if isinstance(ink, int):
            inkint.add(ink)
    sum_inkint = sum(inkint)
    return sum_inkint
