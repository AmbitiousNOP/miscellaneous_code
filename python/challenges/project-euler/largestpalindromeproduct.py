"""
A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""
import time

def find_palindrome():
    # create a range from 100 -> 999
    largest = 0
    # start from 999
    for x in reversed(range(100,1000)):
        # start from 999
        for y in reversed(range(100,1000)):
            # check if x*y is a palindrome and if its bigger than largest variable
            if (str(x*y) == (str(x*y)[::-1])) and (int(x*y) >= int(largest)):
                largest = x*y
                break
            else:
                continue
 
    print(largest)

start = time.time()
find_palindrome()
end = time.time()
print(end-start)
