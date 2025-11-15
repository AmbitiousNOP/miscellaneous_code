'''
given an array of ints
return the one that appears an odd num of times
there will allways be one int that appears an off num of times

loop through searching for each diff num
drop the num after adding to a variable for count
if count is odd program can quick
dropping the nums after counting will make the array shorter each iter
'''

def find_it(seq):
    for i in set(seq):
        if seq.count(i) % 2 != 0:
            return i
        else:
            pass

print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))


# thought this would be faster due to the list progressively getting smaller
# but according to Code Wars this ran slower...
def find_it_improved(seq):
    for i in set(seq):
        if seq.count(i) % 2 != 0:
            return i
        else:
            seq = list(filter(lambda a: a !=i, seq))
            
print(find_it_improved([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))