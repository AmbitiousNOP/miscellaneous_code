#!/usr/bin/env python


animals = ['OWL', 'Badger', 'cat', 'Tiger', 'Wombat', 'GORILLA', 'AARDVARK']
# Create a dictionary with key/value pairs derived from an iterable
result = { a.lower(): len(a) for a in animals  }
print(result)
print()
fmt = "Key:{:10} : Value:{}"
for animal, num_chars in result.items():
    print(fmt.format(animal, num_chars))
