#!usr/bin/env python
from multiprocessing import Process, Pipe


def main():
    parent, child = Pipe()
    p = Process(target=quack, args=(child,))
    p.start()
    print(parent.recv())                    # Receiving a picklable object
    p.join()


def quack(conn):
    conn.send(['quack', 'quack', 'honk'])   # Sending a picklable object
    conn.close()


if __name__ == '__main__':
    main()
