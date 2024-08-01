from typing import Union, Generator, Any, List

def grep(needle : str) -> Generator[None, str, None]:
    '''Only emits lines of text that contain x'''
    haystack = None
    while True:
        haystack = yield haystack

        if needle not in haystack:
            haystack = None


def sed(pattern :str, replacement: str) -> Generator[None, str, None]:
    '''Replace any lines containing pattern with replacement'''
    result = None
    while True:
        result = yield result

        if pattern in result:
            result = replacement


search = grep('foo')
replace = sed('bar', 'baz')
next(search)
next(replace)
with open('mary.txt') as file:
    for line in file:
        found = search.send(line)
        if found:
            line = replace.send(line)

            print(line)
