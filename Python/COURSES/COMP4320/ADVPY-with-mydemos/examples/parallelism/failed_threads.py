#!/usr/bin/env python3
from threading import Thread

target = 0


def unit():
    global target
    for _ in range(100000):
        target += 1
        target -= 1


def main():
    thread_count = 100
    threads = set()
    for _ in range(thread_count):
        threads.add(Thread(target=unit))
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print('got {}, should be 0'.format(target))


if __name__ == '__main__':
    main()
