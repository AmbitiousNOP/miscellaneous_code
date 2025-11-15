from itertools import takewhile

# function to check whether
# number is even
def even_nos(x):
    return(x % 2 == 0)


# function to test the elements
def test_func(x):	
	print("Testing:", x)
	return(x.isdigit())

#example 1
# iterable (list)
li =[0, 2, 4, 8, 17, 22, 34, 6, 67]
  
# output list
new_li = list(takewhile(even_nos, li))
  
print(new_li)
print(3 * '\n')


#example 2
# using takewhile with for-loop
for i in takewhile(test_func, "11234erdg456"):
	
	print("Output :", i)
	print()
