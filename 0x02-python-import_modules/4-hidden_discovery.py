#!/usr/bin/python3
import marshal


def print_names_from_pyc(file_path):
    with open(file_path, 'rb') as file:
        magic = file.read(4)
        timestamp = file.read(4)
        code_object = marshal.load(file)
    names = code_object.co_names
    filter_name = sorted(name for name in names if not name.startswith('__'))
    for name in filter_name:
        print(name)


if __name__ == "__main__":
    print_names_from_pyc("hidden_4.pyc")
