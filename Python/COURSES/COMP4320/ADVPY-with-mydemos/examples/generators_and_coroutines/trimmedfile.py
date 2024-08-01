#!/usr/bin/env python
class TrimmedFile:
    '''Trims trailing white space read from each line of a file.'''
    def __init__(self, file_name):
        '''file_name - name of file to open for reading'''
        self._file_in = open(file_name)
        #self.lines = open(file_name).readlines()

    # __iter__ returns the iterator (i.e., object that implements __next__)
    def __iter__(self):
        '''Returns self as iterator object'''
        return self

    # __next__ returns next value
    def __next__(self):
        '''Returns each line of text read with trailing whitespace removed'''
        line = self._file_in.readline()

        # When no more values to provide, raise StopIteration
        if line == '':
            raise StopIteration

        return line.rstrip()  # Return next value


if __name__ == '__main__':
    trimmed = TrimmedFile(r'..\data\mary.txt')  # Create instance of generator
    for line in trimmed:
        print(line)  # Line is now trimmed
