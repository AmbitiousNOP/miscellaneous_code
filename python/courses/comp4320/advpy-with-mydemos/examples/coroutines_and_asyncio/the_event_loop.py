#!/usr/bin/env python
import asyncio
from basic_coroutine import lazy_print
import time

def main():
    loop = asyncio.get_event_loop()

    loop.run_until_complete(lazy_print('Hello World'))
   
    print("done")

if __name__ == '__main__':
    main()
