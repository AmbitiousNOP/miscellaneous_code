#!/usr/bin/env python
import random
import threading
import queue
import time


class LockList(list):  # Extend list to be lockable (not required for append)
    lock = threading.Lock()

    def __enter__(self):
        self.lock.acquire()
        return self

    def __exit__(self, exc, type, traceback):
        self.lock.release()


class RandomWord():  # Define callable class to generate words
    def __init__(self):
        with open('../data/words.txt') as WORDS:
            self._words = [word.strip() for word in WORDS]

    def __call__(self):
        return random.choice(self._words)


class Worker(threading.Thread):  # Define worker thread
    def __init__(self, name, q, results):  # Initialize the thread
        super().__init__()
        self.name = name
        self.q = q
        self.results = results

    def run(self):  # Invoked when it is time to run thread
        while True:
            try:
                word = self.q.get(block=False)  # Get next item from queue
                with self.results as out:  # Acquire lock and release when done
                    out.append(f'{self.name}-{word.upper()}')

            except queue.Empty:  # Raised when queue becomes empty
                break
