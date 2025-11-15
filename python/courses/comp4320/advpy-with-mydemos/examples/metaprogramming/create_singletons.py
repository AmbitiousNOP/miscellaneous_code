#!/usr/bin/env python
from metaclass_singleton import ThingA, ThingB


def main():
    # Create multiple instances of each class
    things = [ThingA(), ThingA(), ThingA(), ThingB(), ThingB(), ThingB()]

    for thing in things:
        # No matter how many times class is instantiated, it's same instance
        print(type(thing).__name__, id(thing))


if __name__ == '__main__':
    main()
