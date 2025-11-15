from typing import Union
def grep(needle: str):
    '''Only emits lines of text that contain x'''
    haystack : Union[str, None] = None
    while True:
        haystack  = yield haystack

        if needle not in haystack:
            haystack = None


def sed(pattern: str, replacement: str):
    '''Replace any lines containing pattern with replacement'''
    result: Union[str, None] = None
    while True:
        result = yield result

        if pattern in result:
            result = replacement


search = grep('white')
replace = sed('snow', 'rain')
next(search)
next(replace)
with open('mary.txt') as file:
  for line in file:
    found = search.send(line)
    if found:
        line = replace.send(line)

        print(line)
