#!/usr/bin/env python
def spam(old_func):  # Wraps one function in another and returns it
    def new_func():
        return f"{old_func()} and eggs"
    return new_func
