#!/usr/bin/env python
import asyncio


def main():
    loop = asyncio.get_event_loop()

    loop.call_later(6, print, 0, 'BOOM')
    loop.call_later(5, print, 1)
    loop.call_later(4, print, 2)
    loop.call_later(3, print, 3)
    loop.call_soon(print, 'Starting countdown!')

    loop.run_forever()


if __name__ == '__main__':
    main()
