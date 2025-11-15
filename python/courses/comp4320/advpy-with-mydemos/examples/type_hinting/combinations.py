#!/usr/bin/env python
from typing import Tuple, List


def fullname_combos(first_names: Tuple[str, ...],
                    last_names: Tuple[str, ...]) -> List[str]:
    # Join the first and last names using a nested list comprehension
    return [' '.join([first_name, last_name])            
                for first_name in first_names
                        for last_name in last_names
            ]

fnames = fullname_combos(("Joe", "Diane"), ("Smith", "Williams", "Johnson"))
print(fullname_combos(("Joe", "Diane"), ("Smith", "Williams", "Johnson")))

        