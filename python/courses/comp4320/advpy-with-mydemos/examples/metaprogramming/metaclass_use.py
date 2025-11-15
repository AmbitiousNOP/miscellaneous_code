#!/usr/bin/env python
import metaclass_generic


def main():
    m1 = A()
    m2 = B()
    m3 = A()
    m4 = B()
    print("animal: {} id: {}".format(A.animal, B.id))


class MyBase():
    pass


class A(MyBase, metaclass=metaclass_generic.Meta):
    id = 5

    def __init__(self):
        print("In class A __init__()")


class B(MyBase, metaclass=metaclass_generic.Meta):
    animal = 'wombat'

    def __init__(self):
        print("In class B __init__()")


if __name__ == '__main__':
    main()
