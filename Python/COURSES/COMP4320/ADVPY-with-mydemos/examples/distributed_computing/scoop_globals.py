#!/usr/bin/env python
from scoop import futures, shared


def main():
    shared.setConst('value', 17)
    print(sum(futures.map(add_to, range(10))))


def add_to(x):
    val = shared.getConst('value')
    return x + val


if __name__ == '__main__':
    main()
