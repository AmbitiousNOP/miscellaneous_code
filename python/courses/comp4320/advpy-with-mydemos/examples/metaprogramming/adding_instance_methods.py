#!/usr/bin/env python
from types import MethodType


def main():
    d1 = Dog()                  # Create instance of Dog
    setattr(Dog, "bark", bark)  # Binds function as an instance method
    d2 = Dog()                  # Define another instance of Dog
    d1.bark()                   # New method can be called from either instance
    d2.bark()

    # Add function to instance after passing it through MethodType()
    setattr(d1, "wagtail", MethodType(wag, d1))
    d1.wagtail()      # Call instance method
    try:
        d2.wag()  # Instance method not available - only bound to d1
    except AttributeError as err:
        print(err)


class Dog():  # Define Dog type
    pass


def bark(self):  # Define (unbound) function
    print("Woof! woof!")


def wag(self):  # Create another unbound function
    print("Wagging...")


if __name__ == '__main__':
    main()
