#!/usr/bin/python3
import hidden_4


if __name__ == "__main__":
    namez = dir(hidden_4)
    sort_names = sorted(name for name in namez if not name.startswith("__"))
    for name in sort_names:
        print(name)
