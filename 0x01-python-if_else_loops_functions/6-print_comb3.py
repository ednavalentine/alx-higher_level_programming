#!/usr/bin/python3
for dif in range(10):
    for diff in range(dif+1, 10):
        if dif == 0:
            print("{:02d}, ".format(diff), end="")
        else:
            print("{:02d}, ".format(dif * 10 + diff), end="")
