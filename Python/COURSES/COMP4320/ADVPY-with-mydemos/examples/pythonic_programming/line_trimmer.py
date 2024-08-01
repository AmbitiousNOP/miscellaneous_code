#!/usr/bin/env python


def trimmed(file_name):
    with open(file_name) as file_in:
        for line in file_in:
            # existence of a 'yield' causes function to return a generator
            yield line.rstrip()
    print(file_in.closed)

# gen = trimmed('../../data/mary.txt')
# print(type(gen))
# line = next(gen)
# print(line)
# line = next(gen)
# print(line)
# line = next(gen)
# print(line)
# line = next(gen)
# print(line)
# line = next(gen)
# print(line)

# looping over the a generator object returned by trimmed()
for trimmed_line in trimmed('../../data/mary.txt'):
    #if len(trimmed_line)> 15: break
    print(trimmed_line)
    

    
