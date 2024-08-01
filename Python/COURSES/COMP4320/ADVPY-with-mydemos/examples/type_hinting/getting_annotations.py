#!/usr/bin/env python


def regular_hints(times: int = 1, *args: str, **kwargs: int) -> str:
    pass


# Although weird looking, this is perfectly valid Python code.
def weird_hints(word: len, times: 0 = 1) -> 'unk':
    pass


# The __annotations__ dictionary stores the key and value of each annotation.
print(regular_hints.__annotations__, weird_hints.__annotations__, sep='\n')

__name__
