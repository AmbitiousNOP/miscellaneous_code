#!/usr/bin/env python3
import threading

target = 0
lock = threading.Lock()


def unit():
    for _ in range(10000):
        count_up()
        count_down()


def count_up():
    global target
    with lock:
        target += 1


def count_down():
    global target
    with lock:
        target -= 1


def main():
    thread_count = 100
    threads = set()
    for _ in range(thread_count):
        threads.add(threading.Thread(target=unit))
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print('got {}, should be 0'.format(target))


if __name__ == '__main__':
    main()
