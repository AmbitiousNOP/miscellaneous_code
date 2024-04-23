"""
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
return the running sum of nums
"""

from typing import List

# my submission (run time 50ms/117ms)
def runningSum(nums: List[int]) -> List[int]:
    return [sum(nums[:i+1]) for i,j in enumerate(nums)]
    

print(runningSum([1,2,3,4]))
print(runningSum([1,1,1,1,1]))
print(runningSum([3,1,2,10,1]))


# top leetcode submission (run time 83ms)
def runningSum(self, nums: List[int]) -> List[int]:
	for i in range(1,len(nums)):
		nums[i] = nums[i-1] + nums[i]
	return nums


