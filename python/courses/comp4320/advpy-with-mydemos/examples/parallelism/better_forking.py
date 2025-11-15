#!usr/bin/env python
import multiprocessing

def main():
    p = multiprocessing.Process(target=childs_work, args=(1, 2))
    p.start()
    print("Inside Parent Process\n")
    p.join()
    print()

def childs_work(alpha, bravo):    
    print("Inside Child Process:", alpha + bravo, "\n")
 

if __name__ == '__main__':
    main()
