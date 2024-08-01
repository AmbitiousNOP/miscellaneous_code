#!/usr/bin/env python
r = range(1, 4)
i = iter(r)
print(f"Type of 'r':{type(r)}      Type of 'i':{type(i)}\n")

print("While loop:", end=" ")
while True:  # Explicitly testing for StopIteration to know when to stop.
    try:
        print(next(i), end=" ")
    except StopIteration:  # iterable is depleted, code should stop iterating
        break

i = iter(range(1, 4))
print("\tFor loop:", end=" ")
for value in i:            # For loop implicitly calls next() and
    print(value, end=" ")  # automatically stops and handles exception quietly
print()
