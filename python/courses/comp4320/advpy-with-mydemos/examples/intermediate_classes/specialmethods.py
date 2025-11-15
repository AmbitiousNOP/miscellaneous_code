#!/usr/bin/env python


class Special():

    def __init__(self, value):  # invoked every time Special() is called
        self._value = str(value)

    def __add__(self, other):  # called when the '+' operator is used
        return self._value + other._value

    def __mul__(self, num):  # called when the '*' operator is used
        return ''.join((self._value for i in range(num)))
        #return self._value * num

    def __str__(self):  # called when the str() constructor is called is used
        return self._value.upper()

    def __eq__(self, other):  # called when the '==' operator is used
        return self._value == other._value


if __name__ == '__main__':
    s = Special('spam')       # invokes Special.__init__
    t = Special('eggs')
    u = Special('spam')
    v = Special(5)           # invokes Special.__init__
    w = Special(22)

    print("s + s", s + s)    # invokes Special.__add__(s, s)
    print("s + t", s + t)    # invokes Special.__add__(s, t)
    print("t + t", t + t)
    print("s * 10", s * 10)  # invokes Special.__mult__(s, 10)
    print("t * 3", t * 3)

    # invokes Special.__str__(s) and pecial.__str__(t)
    print("str(s)={}  str(t)={}".format(s, str(t)))

    print("id(s)={} id(t)={} id(u)={}".format(id(s), id(t), id(u)))
    print("s == s", s == s)  # invokes Special.__eq__(s, s)
    print("s == t", s == t)  # invokes Special.__eq__(s, t)
    print("s == u", s == u)
    print("v + v", v + v)
    print("v + w", v + w)
    print("w + w", w + w)
    print("v * 10", v * 10)
    print("w * 3", w * 3)
