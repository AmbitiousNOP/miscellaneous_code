'''
Given an integer array nums, 
return an array answer such that answer[i] 
is equal to the product of all the elements 
of nums except nums[i].

The product of any prefix or suffix of nums 
is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) 
time and without using the division operation.
'''

def productExceptSelf(nums: list[int]) -> list[int]:
    # loop through the list
    # take list[:i] + list[i+1:] and get the product
    # append that to a list
    dict = {}

    for i in nums:
        # i = idx, j = elem
        # key = elem, value = list of numbers in list except j
        dict[i] =  [x for x in nums if x!= i]
    
    if str(dict.values()) == "dict_values([[]])":
        return [0]
    

    prod = 1 
    for i in dict.values():
        for j in i:
            prod *= j
        prod = 1

    print(dict)

    return [i for i in dict.values()]


#print(productExceptSelf([0,0]))
print(productExceptSelf([0,4,0]))
#print(productExceptSelf([1,2,3,4]))