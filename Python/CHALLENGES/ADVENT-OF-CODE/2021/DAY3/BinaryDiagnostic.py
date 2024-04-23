"""
Find the gamma rate
Find the epsilon rate

Multiply both to get the power consumption
"""

file = open("input-3.txt", "r")

binary = [i for i in file.read().split("\n") if i != ""]

# find the most significant bit in each column
# find the least significant bit in each column

# loop through the list for the first bit only
#[i for i, x in enumerate(my_list) if x == "whatever"]

data = ["00100","11110","10110","10111","10101","01111","00111",
"11100","10000","11001","00010","01010"]

# append the position [0] of each binary to new list then count

def most_common(lst):
    return max(set(lst), key=lst.count)

def binatodeci(binary):
    return sum(val*(2**idx) for idx, val in enumerate(reversed(binary)))

def testing(bin):
    elem_arr = []
    most_cmn = []
    least_cmn = []
    position = 0
    # loop through binary at x index 
    # append each elem to a new array
    while position != len(bin[0]):
        for elem in bin:
            elem_arr.append(bin[bin.index(elem)][position])
        most_cmn.append(int(most_common(elem_arr)))
        elem_arr = []
        # get the most occured value (max()?)
        # append to a list
        position += 1
    
    for val in most_cmn:
        if val == 1:
            least_cmn.append(0)
        else:
            least_cmn.append(1)
    
    print(most_cmn)
    print(least_cmn)

    print(binatodeci(most_cmn))
    print(binatodeci(least_cmn))
    
    return binatodeci(most_cmn) * binatodeci(least_cmn)

print(testing(binary))

