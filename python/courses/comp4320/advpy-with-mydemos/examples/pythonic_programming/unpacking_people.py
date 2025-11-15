#!/usr/bin/env python3


# A list of 3-element tuples
people = [
    ('Melinda', 'Gates', 'Gates Foundation'),
    ('Steve', 'Jobs', 'Apple'),
    ('Larry', 'Wall', 'Perl'),
    ('Paul', 'Allen', 'Microsoft'),
    ('Larry', 'Ellison', 'Oracle'),
    ('Bill', 'Gates', 'Microsoft'),
    ('Mark', 'Zuckerberg', 'Facebook'),
    ('Sergey', 'Brin', 'Google'),
    ('Larry', 'Page', 'Google'),
    ('Linus', 'Torvalds', 'Linux')
]

# The for loop unpacks each tuple into the three variables.
# Even though only two fo the three are needed
for first_name, last_name, _ in people:
    print(first_name, last_name)

print('\n' * 3)
for person in people:
    print(person[0], person[1], person[2])
