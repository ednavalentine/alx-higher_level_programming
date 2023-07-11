#!/usr/bin/python3
for dif in range(10):
    for diff in range(dif+1, 10):
        if not (dif == 8 and diff == 9):
            print("{:d}{:d}".format(dif, diff), end=", ")
print("{:d}{:d}".format(8, 9))
