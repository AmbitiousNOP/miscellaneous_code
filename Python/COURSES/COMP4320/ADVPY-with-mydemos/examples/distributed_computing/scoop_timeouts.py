#!/usr/bin/env python
from scoop import futures, shared


def main():
    shared.setConst('value', 17)
    print(sum(futures.map(add_to, range(1000))))


def add_to(x):
    try:
        val = shared.getConst('value', timeout=5)
        return x + val
    except TimeoutError:
        return 0


if __name__ == '__main__':
    main():
