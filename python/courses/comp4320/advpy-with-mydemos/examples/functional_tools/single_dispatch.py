#!/usr/bin/env python
from functools import singledispatch
from io import TextIOWrapper


def main():
    mary_in = open('../../data/mary.txt')  # open a file and get a file object
    for x in [mary_in, '../../data/mary.txt', b'../../data/mary.txt', 52]:
        try:
            # correct single dispatch handler will automatically be called
            with xopen(x) as file_in:
                result = file_in.read()
            print(f"Length: {len(result)}")
        except TypeError as err:
            print('ERROR:', err)

    print('-' * 60)
    print(xopen.dispatch(str), "\n")  # show handler function for str
    for arg_type, func in xopen.registry.items():   # show functions for each registered type
        print(arg_type, func) 

@singledispatch
def xopen(source, mode="r"):  # generic function that is actually called
    raise TypeError("Invalid arg: must be file, str, or bytes, not",
                    type(source).__name__)


@xopen.register(TextIOWrapper)  # handler for text files
def xopen_file(fileobj):
    return fileobj


@xopen.register(str)  # handler for string type
def xopen_str(str, mode="r"):
    return open(str, mode)


@xopen.register(bytes)  # handler for bytes type
def xopen_bytes(bytes, mode="r"):
    return open(bytes.decode(), mode)


if __name__ == '__main__':
    main()
