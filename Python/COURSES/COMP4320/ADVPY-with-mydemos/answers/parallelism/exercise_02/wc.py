#!/usr/bin/env python

from os import walk
from sys import argv
from pathlib import Path


def tree(start):
    files, lines, words, chars = 0, 0, 0, 0
    for path, _, filenames in walk(start):
        files += len(filenames)
        for fname in filenames:
            try:
                with open(Path(path) / fname) as fh:
                    for line in fh:
                        lines += 1
                        words += len(line.split())
                        chars += len(line)
            except UnicodeDecodeError:
                pass
    return files, lines, words, chars


if __name__ == '__main__':
    if len(argv) == 2:
        results = tree(argv[1])
        print(f'Files {results[0]}\n'
              f'Lines {results[1]}\n'
              f'Words {results[2]}\n'
              f'Chars {results[3]}\n')
