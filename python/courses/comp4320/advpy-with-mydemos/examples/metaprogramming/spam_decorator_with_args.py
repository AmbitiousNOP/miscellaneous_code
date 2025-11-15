#!/usr/bin/env python
def spam(a, b):             # Decorator function takes parameters
    def wrapper(old_func):  # Wrapper function wraps original function
        def new_func():     # Typcially invokes the original function
            return f"{a * old_func()} and {b} eggs"
        return new_func
    return wrapper
