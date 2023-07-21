#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or not roman_string:
        return 0
    roman_numbers = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000}
    res = 0
    prevalue = 0
    for ink in roman_string[::-1]:
        value = roman_numbers[ink]
        if value < prevalue:
            res -= value
        else:
            res += value
        prevalue = value
    return res
