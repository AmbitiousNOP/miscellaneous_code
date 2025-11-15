#!/usr/bin/env python
from typing import Tuple, Generator, Any


def fullname_combos(first_names: Tuple[str, ...],
                    last_names: Tuple[str, ...]) -> Generator[str, None, None]:
    # Join the first and last names using a generator expression
    yield from (' '.join([first_name, last_name])
                for first_name in first_names
                for last_name in last_names)


def coroutine() -> Generator[None, Any, None]:
    while True:
        # Assigning to yield makes it coroutine, not generator
        value_received = yield
        print('value_consumed:', value_received)


for name in fullname_combos(("Joe", "Diane"), ("Smith", "Williams", "Jones")):
    print(name)


c = coroutine()  # Create instance of coroutine
next(c)  # Prime (start) the coroutine

for letter in "alpha", "beta", 'gamma', 99, 45.3:
    c.send(letter)  # Send in data

fn = fullname_combos(('bob', 'sue'), ('alan', 'joe', 'mary'))
for name in fn:
    print(name)

print()