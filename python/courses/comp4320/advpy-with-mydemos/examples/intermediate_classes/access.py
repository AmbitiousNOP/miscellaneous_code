#!/usr/bin/env python
class Access():
    def public_method(self):
        print("assigning 5 to attribute a")
        self.a = 5

    def _private_method(self):   # private!
        print("assigning 25 to attribute _b")
        self._b = 25

    def __mangled_method(self):
        print("assigning 99 to attribute __c")
        self.__c = 99
