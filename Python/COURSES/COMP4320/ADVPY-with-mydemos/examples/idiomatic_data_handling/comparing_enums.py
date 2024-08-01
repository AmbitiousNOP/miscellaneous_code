#!/usr/bin/env python
from enum import Enum, auto


class Color(Enum):
    WHITE = auto()
    RED = auto()
    GREEN = auto()
    BLUE = auto()
    ORANGE = auto()


class Direction(Enum):
    NORTH = auto()
    EAST = auto()
    SOUTH = auto()
    WEST = auto()


def main():
    fmt = "{:>6}:{:<10}"
    for color in Color:
        print(fmt.format(color.name, color.value), end="")
    print()
    for direction in Direction:
        print(fmt.format(direction.name, direction.value), end="")
    print('\n')

    # Compare different Enum's that have the same ValueError
    print("Equal" if Color.WHITE == Direction.NORTH else "Not Equal")


if __name__ == '__main__':
    main()
