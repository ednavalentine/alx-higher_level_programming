#!/usr/bin/python3
import sys


def main():
    argv = sys.argv[1:]
    res = 0

    for arg in argv:
        res += int(arg)
    print(res)


if __name__ == "__main__":
    main()
