#!/usr/bin/env python
from typing import Tuple


def process(record: Tuple[str, int, float]) -> None:  # Expects a three-tuple
    pass

process(('a', 23, 34.4))
process((23, 'a', 34.4))
process(('a','b', 34))