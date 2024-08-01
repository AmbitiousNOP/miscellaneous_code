#!/usr/bin/env python
import asyncio
import signal
from random import randrange
from async_tasks import sleeper


def main():
    loop = asyncio.get_event_loop()

    loop.add_signal_handler(signal.SIGINT, asyncio.create_task,
                            shutdown(loop))

    loop.create_task(sleeper(1))
    loop.create_task(sleeper(2))

    loop.run_forever()


async def shutdown(loop):
    print("Beginning graceful shutdown")
    tasks = [t for t in asyncio.all_tasks(loop)
             if t is not asyncio.current_task(loop)]

    for task in tasks:
        task.cancel()
    # Allowing exceptions to bubble will cause the program to
    # hang forever, as nothing handles the exceptions nor stops
    # the loop
    await asyncio.gather(*tasks, return_exceptions=True)
    loop.stop()


if __name__ == '__main__':
    main()
