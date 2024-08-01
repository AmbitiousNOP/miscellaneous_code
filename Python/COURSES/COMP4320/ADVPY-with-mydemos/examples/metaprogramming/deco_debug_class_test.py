#!/usr/bin/env python
from deco_debug_class import debugger


def main():
    hello('hello', 'world')  # call replacement function
    print()

    hello('hi', 'Earth')
    print()

    hello('greetings')

    bark("woof", repeat=3)
    bark("yip", repeat=4)
    bark("arf")

    hello('hey', 'girl')

    print('-' * 60)

    # display function call info from class
    for i, info in enumerate(debugger.get_calls(), 1):
        print(f"{i:2}. {info[0]:10} {str(info[1]):20} {str(info[2]):20}")


@debugger  # apply debugger to function
def hello(greeting, whom="world"):
    print("{}, {}".format(greeting, whom))


@debugger  # apply debugger to function
def bark(bark_word, *, repeat=2):
    print("{0}! ".format(bark_word) * repeat)


if __name__ == '__main__':
    main()
