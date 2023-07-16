#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list_res = []
    for number in my_list:
        list_res.append(number % 2 == 0)
    return list_res
