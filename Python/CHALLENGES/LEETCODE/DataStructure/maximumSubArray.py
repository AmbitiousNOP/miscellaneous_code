"""
Given an integer array nums, find the
subarray which has the largest sum and return its sum.
"""

def maxSubArray(nums: list[int]) -> int:
    # given [-1, 5, 4, -1, 7, 8]
    # -1 + 5
    #    + 4
    #    + -1
    # and so on
    # then do
    # 5 + 4
    #   + -1

    # create a highest sum value
    maxSum = []
    # as a higher value is found... replace maxSum
   
    for i,j in enumerate(nums):
        itr = 0
        while itr != len(nums):
            print(f"list = {nums[:len(nums)-itr]}")
            if (sum(nums[:len(nums)-itr]) > sum(maxSum)) or (len(maxSum) == 0):
                maxSum = nums[:len(nums)-itr]
            itr += 1
            if itr == len(nums):
                print(f"removing {nums.remove(nums[0])}")
                break
    #print(sum(maxSum))




#maxSubArray([5,4,-1,7,8])
#maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
#maxSubArray([1])
#maxSubArray([-1])
#maxSubArray([-2,1])
