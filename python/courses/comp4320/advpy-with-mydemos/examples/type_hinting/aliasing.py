#!/usr/bin/env python
from typing import Tuple, Generator, Any
Names = Tuple[str, ...]                     # Create an alias named Name
GenA = Generator[str, None, None]           # Create an alias named GenA
GenB = Generator[None, Any, None]           # Create an alias named GenB


def fullname_combos(first_names: Names, last_names: Names) -> GenA:
    # Join the first and last names using a generator expression
    yield from (' '.join([first_name, last_name])
                for first_name in first_names
                for last_name in last_names)


def coroutine() -> GenB:
    while True:
        # Assigning to yield makes it coroutine, not generator
        value_received = yield
        print('value_consumed:', value_received)
