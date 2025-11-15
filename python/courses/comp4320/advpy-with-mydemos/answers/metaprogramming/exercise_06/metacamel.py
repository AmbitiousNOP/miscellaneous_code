#!/usr/bin/env python
from examples.snakecase import snake_case


class FixCamel(type):

    @classmethod
    def __prepare__(metaclass, name, bases, **kwargs):
        return {'__name__': snake_case(name)}

    def __new__(metaclass, class_name, bases, attrs):
        return super().__new__(metaclass, class_name.upper(), bases, attrs)


class foo(metaclass=FixCamel):
    pass


f = foo()
print(f)
print(type(f).__name__)
print(f)
