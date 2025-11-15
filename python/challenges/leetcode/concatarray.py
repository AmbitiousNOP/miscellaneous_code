"""
Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

Specifically, ans is the concatenation of two nums arrays.
"""

# my solution
def getConcatenation(nums):
    return nums + nums


# top leet code solution (apparerntly faster?)
def getConcatenation(nums):
    return nums * nums