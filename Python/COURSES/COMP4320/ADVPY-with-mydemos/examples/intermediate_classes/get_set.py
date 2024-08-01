#!/usr/bin/env python
class Knight():
    def __init__(self, name):
        self._name = name

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name


if __name__ == '__main__':
    k = Knight("Lancelot")
    print(k.get_name())
