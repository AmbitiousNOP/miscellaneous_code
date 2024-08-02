"""
Write a script which will count number of files with each extension in a file tree.
● It should take the initial directory as a command line argument, and then display the total number of
files with each distinct file extension that it finds.
● Files with no extension should be skipped. Use a Counter object to do the counting.
"""

from os import listdir, path
from os.path import isfile, join
import sys
from collections import Counter

file_types = {}

directory = sys.argv[1]

counts = Counter()
for f in listdir(directory):
    if isfile(join(directory, f)):
        _, file_extension = path.splitext(directory+f)
        counts[file_extension] += 1


for item, count in counts.items():
    print(item, count)
