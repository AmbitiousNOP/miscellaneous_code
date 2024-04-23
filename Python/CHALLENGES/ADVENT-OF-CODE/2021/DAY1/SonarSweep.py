"""
Given a set of measurements
Determine how many measurements are larger than the previous
"""

file = open("input.txt", "r")

#data = file.read().split("\n")

data = [int(i) for i in file.read().split("\n") if i != ""]
data.remove(data[-1])

def two_increasingSonar():
    lgr = 0
    for i in range(len(data) - 2 + 1):
        if data[i: i + 2][0] < data[i:i+2][1]:
            lgr += 1
    return lgr


test_data = [199,200,208,210,200,207,240,269,260,263]

def three_increasingSonar():
    lgr = 0
    # get a window size of 6 and split into two
    """
    for i in range(len(test_data)-4+1):
        if sum(test_data[i:i+4][0:3]) <  sum(test_data[i:i+4][1:4]):
            print(sum(test_data[i:i+4][0:3]), sum(test_data[i:i+4][1:4]))
            lgr += 1
    return lgr
    """
    sums = []
    for i in range(len(data)-3+1):
        sums.append((sum(data[i:i+3])))

    print(sums)
    for j in range(len(sums)-2+1):
        if sums[j:j+2][0] < sums[j:j+2][1]:
            lgr+=1
    
    return lgr





