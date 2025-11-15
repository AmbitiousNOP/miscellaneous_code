#!/usr/bin/env python


class debugger():                   # class implementing decorator
    function_calls = []

    def __init__(self, func):       # original function passed into decorator
        self._func = func

    def __call__(self, *args, **kwargs):  # __call__() is replacement function
        # add function name and args to saved list
        self.function_calls.append((self._func.__name__, args, kwargs))
        result = self._func(*args, **kwargs)  # call the original function
        return result  # return result of calling original function

    @classmethod
    def get_calls(cls):  # define method to get saved function call information
        return cls.function_calls
