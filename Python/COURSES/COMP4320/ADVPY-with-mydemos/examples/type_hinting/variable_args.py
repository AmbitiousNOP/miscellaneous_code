#!/usr/bin/env python
from typing import Tuple, List


def average(*numbers: float) -> float:
    return sum(numbers)/len(numbers)


print(f'{average(4, 5, 6.2, 7, 8.9):.3f}')
