#!/usr/bin/env python
import asyncio
import time

def main():
    asyncio.run(lazy_print('Hello World'))


async def lazy_print(msg):
    time.sleep(3)
    print(msg)


if __name__ == '__main__':
    main()
