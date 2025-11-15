#!/usr/bin/env python

class DefaultNone:
    def __get__(self, instance, owner=None):
        if self.name not in instance.__dict__:
            return None
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if value is None:
            raise ValueError("Cannot be None")
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = '__' + name
