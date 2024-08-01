#!/usr/bin/env python
import pickle
from pprint import pprint

airports = {'RDU': 'Raleigh-Durham', 'IAD': 'Dulles', 'MGW': 'Morgantown',
            'EWR': 'Newark', 'LAX': 'Los Angeles', 'ORD': 'Chicago'}

colors = ['red', 'blue', 'green', 'yellow', 'black', 'white', 'orange']

lucky_number, lucky_day = 13, "Thursday"

# list of objects
data = [airports, colors, lucky_number, lucky_day]

# open pickle file for writing in binary mode
with open('pickled_data.pickle', 'wb') as pic_out:
    for obj in data:
        pickle.dump(obj, pic_out)  # serialize data structures to pickle file

# open pickle file for reading in binary mode
with open('pickled_data.pickle', 'rb') as pic_in:
    while True:  # Don't necessarily know how many things to read
        try:
            # de-serialize pickle file back into data structures
            pickled_data = pickle.load(pic_in)
            print(type(pickled_data))
            pprint(pickled_data)
            print()
        except EOFError:
            # raised when no data remains to be reading
            # use this as an indicator to stop calling load()
            break
