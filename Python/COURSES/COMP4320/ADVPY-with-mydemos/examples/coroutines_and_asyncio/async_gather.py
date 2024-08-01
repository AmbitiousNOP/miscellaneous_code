#!/usr/bin/env python
import asyncio
from random import randrange


def main():
    asyncio.run(roll_up(10))


async def long_process(name):
    print(f'Beginning {name}')
    timeout = randrange(2, 10)

    # Simulate a long asynchronous work item
    await asyncio.sleep(timeout)
    print(f'Ending {name}')
    return timeout * 1000


async def roll_up(times):
    jobs = [long_process(n) for n in range(times)]
    results = await asyncio.gather(*jobs)
    print(f'Slept a total of {sum(results)}ms across {times} tasks')


if __name__ == '__main__':
    main()
