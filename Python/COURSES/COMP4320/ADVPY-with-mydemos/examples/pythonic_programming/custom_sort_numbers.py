#!/usr/bin/env python

nums = [800, 80, 1000, 32, 255, 400, 5, 5000]

n1 = sorted(nums)  # Numbers sort from low to high by default
print("Numbers sorted numerically:")
for n in n1:
    print(n, end=' ')
print("\n")

n2 = sorted(nums, key=str)  # Sort numbers as strings instead of numerically
print("Numbers sorted as strings:")
for n in n2:
    print(n, end=' ')
print()

#nums.sort(key=str)