#!/usr/bin/env python
import asyncio
from basic_coroutine import lazy_print

def main():
    asyncio.run(serial_sleeper())


async def serial_sleeper():
    print(1)
    await asyncio.sleep(2)
    await lazy_print('In Sleeper')
    await asyncio.sleep(1)
    print(2)


if __name__ == '__main__':
    main()
