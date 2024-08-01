#!/usr/bin/env python
class First:
    # The type Second is not yet available to python, so it must be
    # forward-declared using a string
    def process(self, item: 'Second') -> str:
        pass


class Second:
    # The type First is available to python, so it can just reference
    # the First symbol directly
    def create(self, data: First) -> str:
        pass

f1 = First()
f1.process(Second())
