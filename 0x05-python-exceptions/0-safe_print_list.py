#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    print_elements = 0
    for ink in range(x):
        try:
            print(my_list[ink], end="")
            print_elements += 1
        except IndexError:
            break
    print()
    return print_elements
