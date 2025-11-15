"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.
"""    

# runs in 89ms
def merge_inplace(nums1: list[int], m: int, nums2: list[int], n: int):
    for i,j in enumerate(nums2):
        nums1[m] = j
        m +=1
    nums1.sort()




print(merge_inplace([1,2,3,0,0,0], 3, [2,5,6], 3))