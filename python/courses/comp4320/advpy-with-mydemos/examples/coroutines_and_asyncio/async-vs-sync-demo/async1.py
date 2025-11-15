#!/usr/bin/env python3
# countasync.py
#take note of what looks different than
# if you were to define the functions with 
# just def and time.sleep()

# **** **********************
# The order of this output is the heart of async IO  
# **** **********************

# time.sleep is BLOCKING.. everything stops until sleep is over
# vs async await asyncio.sleep which is NON-BLOCKING - yields to
# processor for other tasks to process
#*** ************************
import asyncio

async def count():
    print("One")
    await asyncio.sleep(1)
    print("Two")

async def main():
    await asyncio.gather(count(), count(), count())

if __name__ == "__main__":
    import time
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
