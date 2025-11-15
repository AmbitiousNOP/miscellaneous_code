#!usr/bin/env python
import threading
import pdb


def main():
    pdb.set_trace()
    t = threading.Thread(target=childs_work, args=(1, 2))
    t.start()
    print("Inside Parent Thread\n")
    t.join()


def childs_work(alpha, bravo):
    pdb.set_trace()
    print("Inside Child Thread:", alpha + bravo, "\n")


if __name__ == '__main__':
    main()
