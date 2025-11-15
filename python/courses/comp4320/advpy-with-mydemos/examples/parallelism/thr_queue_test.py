#!/usr/bin/env python
import random
import queue
import time
from thr_queue import RandomWord, Worker, LockList


def main():
    NUM_ITEMS = 25000
    POOL_SIZE = 25

    q = queue.Queue(0)  # Initialize empty queue

    words = RandomWord()
    for i in range(NUM_ITEMS):
        w = words()
        q.put(w)  # Fill the Queue

    start_time = time.ctime()
    output = LockList()

    pool = []
    for i in range(POOL_SIZE):
        w = Worker(f'Worker {chr(i+65)}', q, output)  # Add Thread to Pool
        w.start()  # Start the thread
        pool.append(w)

    for t in pool:
        t.join()  # Wait for thread to finish

    end_time = time.ctime()

    for _ in range(20):
        print(random.choice(output))

    print(start_time)
    print(end_time)


if __name__ == '__main__':
    main()
