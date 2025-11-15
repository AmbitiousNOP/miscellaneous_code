#!/usr/bin/env python
from time import time
from threading import Thread


def main():
    threads, TOTAL = 2, 100000000

    t = [Thread(target=count, args=(TOTAL//threads,)) for _ in range(threads)]

    start = time()
    for item in t:
        item.start()
    for item in t:
        item.join()
    end = time()

    print('{} threads: {}s'.format(threads, end - start))


def count(n):
    while n > 1:
        n -= 1


if __name__ == '__main__':
    main()
