#!/usr/bin/env python
import asyncio
from random import randrange


def main():
    loop = asyncio.get_event_loop()
    loop.create_task(sleeper(1))
    loop.create_task(sleeper(2))
    loop.run_forever()


async def sleeper(n):
    while True:
        timeout = randrange(10)
        print(f'[{n}] Sleeping for {timeout}s')
        await asyncio.sleep(timeout)
        print(f'[{n}] Done sleeping for {timeout}s')


if __name__ == '__main__':
    main()
