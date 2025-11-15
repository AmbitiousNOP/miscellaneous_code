"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
"""

# my submission (1171ms)
def containsDuplicate(nums: list[int]) -> bool:
    # turn the list into a set and if the length shortens then we know theres duplicates
    if len(set(nums)) != len(nums):
        return True
    else:
        return False

# top leetcode submission (run time 1091 ms)
def containsDuplicate(nums: list[int]) -> bool:
    return len(set(nums)) != len(nums)


print(containsDuplicate([1,2,3,1]))
print(containsDuplicate([1,2,3,4]))
print(containsDuplicate([1,1,1,3,3,4,3,2,4,2]))
