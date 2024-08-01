#!/usr/bin/env python
from multiprocessing import Process, Queue
from datetime import datetime


def main():
    line = Queue()
    procs = [Process(target=append, args=(line,)),
             Process(target=append, args=(line,)),
             Process(target=remove, args=(line,)),
             Process(target=remove, args=(line,))]

    for p in procs:
        p.start()

    for p in procs:
        p.join()
    print("All child processes have completed their work")


def append(q):
    date = datetime.now()
    print('Sending', date)
    q.put(date)


def remove(q):
    item = q.get()
    print('Got', item)


if __name__ == '__main__':
    main()
