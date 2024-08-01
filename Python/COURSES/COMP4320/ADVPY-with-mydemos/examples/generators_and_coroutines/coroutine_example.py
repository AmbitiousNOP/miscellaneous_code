#!/usr/bin/env python
def coroutine():  # Define coroutine function
    while True:
        # Assigning to yield makes it coroutine, not generator
        value_received = yield
        print('value_consumed:', value_received)
