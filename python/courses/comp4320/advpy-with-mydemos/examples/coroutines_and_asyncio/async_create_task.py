#!/usr/bin/env python
import asyncio
from random import randrange


def main():
    loop = asyncio.get_event_loop()

    m1 = monitor(loop.create_task(long_process(1)))
    m2 = monitor(loop.create_task(long_process(2)))
    loop.create_task(m1)
    loop.create_task(m2)

    loop.run_forever()


async def monitor(fut):
    while not fut.done():
        print(f'Waiting for {fut}\n')
        await asyncio.sleep(1)
    print(f'{fut} complete\n')


async def long_process(name):
    print(f'Beginning {name}\n')
    timeout = randrange(2, 10)

    # Simulate a long asynchronous work item
    await asyncio.sleep(timeout)
    print(f'Ending {name}\n')


if __name__ == '__main__':
    main()
