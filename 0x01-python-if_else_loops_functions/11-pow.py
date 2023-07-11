#!/usr/bin/python3
def pow(a, b):
    if b < 0:
        a = 1 / a
        b = abs(b)
    res = 1
    for _ in range(b):
        res *= a
    return res
