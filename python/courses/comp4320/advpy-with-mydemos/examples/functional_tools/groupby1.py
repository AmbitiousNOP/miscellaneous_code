
import itertools

numbers = [1, 1, 1, 3, 3, 2, 2, 2, 1, 1]

# group all values by number
for (key,group) in itertools.groupby(numbers):
	print (key,list(group))
print()


nums = [ ('a', 1), ('a', 2), ('a', 4), ('b', 4), ('b', 5), ('c', 4), ('b', 4), ('c', 5)]
# won't work unsorted by the chosen key
key_func = lambda x: x[0]
for key, group in itertools.groupby(nums, key_func):
    print(f'{key} : {list(group)}')
    
print('*' * 30)

nums.sort()
key_func = lambda x: x[0]
for key, group in itertools.groupby(nums, key_func):
    print(f'{key} : {list(group)}')
