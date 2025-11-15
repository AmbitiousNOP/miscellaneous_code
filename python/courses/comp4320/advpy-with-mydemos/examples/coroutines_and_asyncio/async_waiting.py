#!/usr/bin/env python
import asyncio
from random import randrange


def main():
    asyncio.run(upto_first_exception(10))


async def maybe_throw(n):
    throws = randrange(10) < 1
    timeout = randrange(2, 10)

    print(f'[{n}] will throw in {timeout}s: {throws}')
    await asyncio.sleep(timeout)

    if throws:
        raise Exception('Throwing!')
    else:
        return True


async def upto_first_exception(times):
    jobs = [maybe_throw(n) for n in range(times)]

    result = await asyncio.wait(jobs, return_when=asyncio.FIRST_EXCEPTION)
    done, pending = result

    print(f'Ran {len(done)} jobs, leaving {len(pending)}')


if __name__ == '__main__':
    main()
