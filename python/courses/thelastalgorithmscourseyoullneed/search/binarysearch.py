import math

def bin_search(arr, n):
    low = 0 
    high = len(arr)

    while(low < high):
        mid_point = math.floor(low + (high - low) / 2)
        value = arr[mid_point]
        
        if value == n:
            return True
        elif value > n:
            high = mid_point
        elif value < n:
            low = mid_point + 1
    
    return False


print(bin_search([1,2,3,4,5,6,7,8,9,10], n=8))
print(bin_search([1,2,3,4,5,6,7,8,9,10], n=10))
print(bin_search([1,2,3,4,5,6,7,8,9,10], n=1))
print(bin_search([1,2,3,4,5,6,7,8,9,10], n=4))
print(bin_search([1,2,3,4,5,6,7,8,9,10], n=5))
print(bin_search([1,2,3,4,5,6,7,8,9,10], n=20))