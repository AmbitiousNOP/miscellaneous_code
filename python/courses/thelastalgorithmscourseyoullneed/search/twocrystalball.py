"""
Given two crystal balls that will break if dropped from high enough
distance, determine the exact spot in which it will break in the most
optimized way
"""
import math

# O(sqrt(n))
def two_crystal_balls(breaks):
    jump_amount = math.floor(math.sqrt(len(breaks)))
    i = jump_amount

    while(i < len(breaks)):
        if (breaks[i]):
            break
        i += jump_amount
    
    i -= jump_amount
    j = 0
    while (j < jump_amount) & (i < len(breaks)) :
        if breaks[i]:
            return i
        
        j += 1
        i += 1
    
    return False




print(two_crystal_balls([False,False,False,True,True,True]))
