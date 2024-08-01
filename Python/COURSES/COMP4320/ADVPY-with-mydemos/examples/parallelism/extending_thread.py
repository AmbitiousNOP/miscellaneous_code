#!/usr/bin/env python
from threading import Thread
import random
import time


def main():
    for i in range(10):
        t = SimpleThread(i)  # Create the thread
        t.start()            # Start the thread

    print("Done.")


class SimpleThread(Thread):
    def __init__(self, num):
        super().__init__()  # Required call to parent class construxtor
        self._threadnum = num

    def run(self):  # The is where the work of the thread is done
        time.sleep(random.randint(1, 3))
        print(f"Hello from thread {self._threadnum}")


if __name__ == '__main__':
    main()
