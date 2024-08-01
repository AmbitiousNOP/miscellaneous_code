#!/usr/bin/env python

fruits = ['watermelon', 'apple', 'mango', 'kiwi', 'apricot', 'lemon', 'guava']

# Creating a list from an iterable without using a list comprehensions
results_a = []
for fruit in fruits:
    results_a.append(fruit.upper())

# Creating the list using a list comprehension instead of a explicit for loop
results_b = [  fruit.upper() for fruit in fruits   ]
results_b2 = [fr   for fr in fruits if len(fr) > 4]

# The following list comprehension uses an if to filter out
# fruits that do not start with th eletter 'a'.
results_c = [fruit for fruit in fruits if fruit.startswith('a')]

print("results_a:", " ".join(results_a))
print("results_b:", " ".join(results_b))
print("results_c:", " ".join(results_c))


values = [2, 42, 18, 92, "boom", ['a', 'b', 'c']]

# list comprehension doubles each value
doubles = [value * 2 for value in values]


print("doubles:", end=' ')
for doubled in doubles:
    print(doubled, end=' ')
print()
