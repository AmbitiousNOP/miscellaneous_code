#!/usr/bin/env python
class FauxRange:
    def __init__(self, *args):
        self.start = 0
        self.step = 1
        arg_count = len(args)
        if arg_count == 1:
            self.stop = args[0]
        elif arg_count == 2:
            self.start, self.stop = args
        elif arg_count == 3:
            self.start, self.stop, self.step = args
        else:
            raise TypeError(f"FauxRange expected 1 to 3 args, got {arg_count}")
        self.current = self.start

    # __iter__ returns the iterator (i.e., object that implements __next__)
    def __iter__(self):
        '''Returns self as iterator object'''
        return self

    # __next__ returns next value
    def __next__(self):
        if self.current < self.stop:
            current = self.current
            self.current += self.step
            return current
        else:
            raise StopIteration()


if __name__ == '__main__':
    faux = FauxRange(10)  # Create instance of generator
    for value in faux:
        print(value)  # Line is now trimmed
