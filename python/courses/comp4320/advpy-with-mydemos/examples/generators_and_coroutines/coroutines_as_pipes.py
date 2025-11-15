#!/usr/bin/env python

def segment_a(pipe=None):  # Define coroutine function
    if pipe:
        next(pipe)  # prime the coroutine
    while True:
        # Assigning to yield makes it coroutine, not generator
        value_received = yield
        print('value_consumed by segment_a:', value_received)
        # convert what it consumes to title case version
        all_title_case = [value.title() for value in value_received]
        print('processed result of segment_a:', all_title_case)
        if pipe:  # pipe it to next coroutine
            pipe.send(all_title_case)


def segment_b(pipe=None):  # Define coroutine function
    if pipe:
        next(pipe)  # prime the coroutine
    while True:
        # Assigning to yield makes it coroutine, not generator
        value_received = yield
        print('value_consumed by segment_b:', value_received)
        sorted_result = sorted(value_received)     # sort what it consumes
        print('processed result of segment_b:', sorted_result)
        if pipe:                                   # pipe it to next coroutine
            pipe.send(sorted_result)


pipe = segment_a()  # Create instance of coroutine
next(pipe)  # Prime (start) the coroutine

for letter in "alpha", "beta", 'gamma':
    pipe.send(letter)  # Send in data
print()

# Create instance of coroutine, by piping it to another coroutine
pipe = segment_a(segment_b())
next(pipe)  # Prime (start) the coroutine

for letter in "alpha", "beta", 'gamma':
    pipe.send(letter)  # Send in data
print()
