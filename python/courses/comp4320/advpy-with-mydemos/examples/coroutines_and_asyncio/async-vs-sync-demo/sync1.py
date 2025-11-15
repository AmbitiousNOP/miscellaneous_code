#!/usr/bin/env python3
# countsync.py

#*** ************************
#  there is a slight but critical change in order and execution time

# time.sleep is BLOCKING.. everything stops until sleep is over
# vs async await asyncio.sleep which is NON-BLOCKING - yields to
# processor for other tasks to process
#*** ************************
import time

def count():
    print("One")
    time.sleep(1)
    print("Two")

def main():
    for _ in range(3):
        count()

if __name__ == "__main__":
    s = time.perf_counter()
    main()
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")