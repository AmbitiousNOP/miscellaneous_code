#!/usr/bin/env python
from random import randint
from scoop import futures


def main():
    data = [randint(-1000, 1000) for _ in range(1000)]
    serial = list(map(abs, data))
    parallel = list(futures.map(abs, data))

    assert serial == parallel


if __name__ == '__main__':
    main()
