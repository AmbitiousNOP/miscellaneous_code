#!usr/bin/env python
import os

# ***************************
# os.fork() is not available on WINDOWS
# **************************** 

def main():
    print("Process ID:", os.getpid())
    print("*" * 30)
    returned_pid = os.fork()        # 2 processes running after fork() call
    
    if returned_pid != 0:
        print_info("parent (original)", returned_pid)
    else:
        print_info("child (new one)", returned_pid)


def print_info(msg, returned_pid):
    fmt = "Inside {} process\n\tIt's pid is:{}\n\tIt received: {} from fork()"
    print(fmt.format(msg, os.getpid(), returned_pid))
    print()


if __name__ == '__main__':
    main()
