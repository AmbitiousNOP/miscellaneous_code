#!/usr/bin/env python
class Singleton(type):  # Define metaclass (must inherit from type)
    _instances = {}     # Define dict to hold list of instances

    # Use __call__(), because __new__() is too early in class creation
    def __call__(cls, *args, **kwargs):
        # Check to see if an instance of this class already exists
        if cls not in cls._instances:
            # If instance doesn't exist, create instance and add to dict
            cls._instances[cls] = super().__call__(*args, **kwargs)

        # Always returns the first (and only) instance created.
        return cls._instances[cls]


class ThingA(metaclass=Singleton):   # Create classes using the metaclass
    pass


class ThingB(metaclass=Singleton):   # Create classes using the metaclass
    pass
