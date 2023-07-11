#!/usr/bin/python3
def uppercase(str):
    upp_str = ""
    for n in str:
        up_n = chr(ord(n) - 32) if ord(n) >= 97 and ord(n) <= 122 else n
        upp_str += up_n
    print("{}\n".format(upp_str), end="")
