'''
Given an integer array nums and an integer k, 
return the k most frequent elements. 
You may return the answer in any order.
'''

def topKFrequent(nums: list[int], k: int) -> list[int]:
    # make a hash map where
    # key = an elem from nums
    # value = num of appearances
    #dict = {}

    # loop through list 
    # turn into a set to get all unique values 
    # call count(dict[key]) in order to set the number of appearances 
    #for i in set(nums):
    #    dict[i] = nums.count(i)

    # could create a list of values as [key,value] and sort by value
    # then print the range of k by slicing the list
    freq = []
    for i in set(nums):
        freq.append([i,nums.count(i)])

    # return the dict values ordered
    freq.sort(key=lambda nested: nested[1], reverse=True)
    return [i[0] for i in freq[:k]]

#topKFrequent(nums = [1,1,1,2,2,3], k = 2)
#topKFrequent(nums = [1], k = 1)
print(topKFrequent(nums = [4,1,-1,2,-1,2,3], k = 2))

