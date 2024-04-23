"""
Given an array of integers nums which is sorted 
in ascending order, and an integer target, write 
a function to search target in nums. If target 
exists, then return its index. Otherwise, return -1.
"""

def binarySearch(nums: list[int], target: int) -> int:
    if target in nums:
        return nums.index(target)
    else:
        return -1
    


def realBinSearch(nums: list[int], target: int) -> int:
    # given [-1,0,3,5,9,12] and target of 9
    # calculate the left most and right most elem in list
    # calculate midway point
    # if mid point is > target move the right most point to current midway
    # if mid point is < target move the left most point to the current midway
    # repeat steps

    l, r = 0, len(nums)-1

    while l <= r:
        mid = l + ((r - l) // 2)    # (l + r) // 2 can lead to overflow
        
        if nums[mid] > target:
                r = mid - 1
        elif nums[mid] < target:
            l = mid + 1
        else:
            return mid
    return -1


print(binarySearch([-1,0,3,5,9,12], 2))


