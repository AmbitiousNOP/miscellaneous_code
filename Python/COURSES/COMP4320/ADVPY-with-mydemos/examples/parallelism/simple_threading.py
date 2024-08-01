#!usr/bin/env python
import threading


def main():
    t = threading.Thread(target=childs_work, args=(1, 2))
    t.start()
    print("Inside Parent Thread\n")
    t.join()
    print()

def childs_work(alpha, bravo):
   
    print("Inside Child Thread:", alpha + bravo, "\n")


if __name__ == '__main__':
    main()
