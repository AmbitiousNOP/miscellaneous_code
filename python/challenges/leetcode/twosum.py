"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""


# my solution
def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)):            
            if (nums[i] + nums[j] == target) and (i != j):
                return [i, j]
                

print(twoSum(nums=[3,2,4], target=6))


# top leetcode solution
def twoSum(num, target):
    map = {}
    for i in range(len(num)):
        if num[i] not in map:
            map[target - num[i]] = i + 1
        else:
            return map[num[i]] -1 , i
    
    return -1, -1