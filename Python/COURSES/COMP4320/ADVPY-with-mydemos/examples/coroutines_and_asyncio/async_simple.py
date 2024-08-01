#!/usr/bin/env python
import asyncio


def main():
    loop = asyncio.get_event_loop()                        # Get the event loop
    loop.run_until_complete(say('hello, async world', 1))  # Runt Coroutine
    loop.close()                                           # Close the loop


async def say(what, when):     # Create coroutine with async
    await asyncio.sleep(when)  # Simulate actual work with sleep
    print(what)                # Business logic goes here


if __name__ == '__main__':
    main()
