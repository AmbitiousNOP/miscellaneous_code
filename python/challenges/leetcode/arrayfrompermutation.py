"""
Given a zero-based permutation nums (0-indexed), build an array ans of the same length where ans[i] = nums[nums[i]] for each 0 <= i < nums.length and return it.
"""

from typing import List

# my solution (rum time 279ms)
def buildArray(nums: List[int]) -> List[int]:
    return [nums[num] for num in nums]

print(buildArray([0,2,1,5,3,4]))
# output [0,1,2,4,5,3]

# top leetcode solution (run time 360ms)
def buildArray(self, nums: List[int]) -> List[int]:
    q = len(nums)
    for i,c in enumerate(nums):
        nums[i] += q * (nums[c] % q)
    for i,_ in enumerate(nums):
        nums[i] //= q
    return nums

