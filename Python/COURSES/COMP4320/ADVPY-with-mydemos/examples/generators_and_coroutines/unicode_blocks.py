#!/usr/bin/#!/usr/bin/env python
from collections import namedtuple
from enum import Enum

BlockBoundary = namedtuple('BlockBoundary', 'start stop')

class UnicodeBlock(Enum):
    Arrows = BlockBoundary(0x2190, 0x21FF)
    MathematicalOperators = BlockBoundary(0x2200, 0x22FF)
    ControlPictures = BlockBoundary(0x2400, 0x2426)
    EnclosedAlphanumerics = BlockBoundary(0x2460, 0x24FF)
    MiscellaneousSymbols = BlockBoundary(0x2600, 0x26FF)
    SupplementalArrowsA = BlockBoundary(0x27F0, 0x27FF)
    SupplementalArrowsB = BlockBoundary(0x2900, 0x297F)
    Emoticons = BlockBoundary(0x1F600, 0x1F64F)
    MiscSymbolsAndPictographs = BlockBoundary(0x1F300, 0x1F5FF)
    Dominos = BlockBoundary(0x1F030, 0x1F093)

    @property
    def start(self):
        return self.value.start

    @property
    def stop(self):
        return self.value.stop

    def characters(self):
        for unicode_value in range(self.start, self.stop + 1):
            yield chr(unicode_value)
        #return [chr(unicode_value) for unicode_value in range(self.start, self.stop + 1)]

def main():
    characters = UnicodeBlock.Emoticons.characters()
    for char in characters:
        print(char, end=" ")
    print()
    
    characters = UnicodeBlock.Dominos.characters()
    for char in characters:
        print(char, end=" ")
    print()

if __name__ == '__main__':
    main()
