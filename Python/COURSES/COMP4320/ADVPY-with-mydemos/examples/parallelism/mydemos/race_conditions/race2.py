#!usr/bin/env python
# race2.py

# fix race condtion from race1.py

from threading import Thread, Lock
from time import sleep


counter = 0


def increase(by, lock):
    global counter

    lock.acquire()

    local_counter = counter
    local_counter += by

    sleep(0.1)

    counter = local_counter
    print(f'counter={counter}')

    lock.release()


lock = Lock()

# create threads
t1 = Thread(target=increase, args=(10, lock))
t2 = Thread(target=increase, args=(20, lock))

# start the threads
t1.start()
t2.start()


# wait for the threads to complete
t1.join()
t2.join()


print(f'The final counter is {counter}')

'''
output

race conditions resolved now. no more simultaneous shared data collisons

    counter=10
    counter=30
    The final counter is 30

'''