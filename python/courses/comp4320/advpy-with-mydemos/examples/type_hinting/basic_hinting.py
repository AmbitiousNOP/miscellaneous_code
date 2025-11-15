#!/usr/bin/env python
"""Basic type hinting example"""


first_name: str              # declare first_name as being of type str
last_name: str = "Doe"      # declare alst_name as str with initial value

number: int = 99            # declare and initialize number as an int

data: list = [5, 6, 7]       # declare and initialize data as a list

first_name = 1234
# While the following are valid Python statements
# they violate the intent of the hinting.

# value is not the intended type of str
number = "This is not a number"
key_values: dict = ["these", "are", "not", "key", "value", "pairs"]

print(first_name, last_name, number, data, key_values, sep=" | ")
print()
print(f'{last_name + number}')  # Type hinting suggests this cannot happen
