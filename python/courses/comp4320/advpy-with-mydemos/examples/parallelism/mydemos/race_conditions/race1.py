#!usr/bin/env python
# race1.py

# race condition
from threading import Thread
from time import sleep


counter = 0


def increase(by):
    global counter

    local_counter = counter
    local_counter += by

    sleep(0.1)

    counter = local_counter
    print(f'counter={counter}')


# create threads
t1 = Thread(target=increase, args=(10,))
t2 = Thread(target=increase, args=(20,))

# start the threads
t1.start()
t2.start()


# wait for the threads to complete
t1.join()
t2.join()


print(f'The final counter is {counter}')

'''
output

Expect various output results since both thrads access shared data at same time and last one that finishs
is the one that updates shared data last

If the thread t1 completes before the thread t2, you’ll see the following output:
        counter=10
        counter=20
        The counter is 20 
Otherwise, you’ll see the following output:
        counter=20
        counter=10
        The final counter is 10     
        
Run multiple times to seee different resutls

FIX: to prevent Race Conditions use threading.lock

'''