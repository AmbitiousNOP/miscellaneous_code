

# read in the file 
file = open("input-4.txt", "r")
data = file.read()

drawn_nums = [6,69,28,50,36,84,49,13,48,90,1,33,71,0,94,59,53,58,60,96,30,34,29,91,11,41,77,95,17,80,85,93,7,9,74,89,18,25,26,8,87,38,68,5,12,43,27,46,62,73,16,55,22,4,65,76,54,52,83,10,21,67,15,47,45,40,35,66,79,51,75,39,64,24,37,72,3,44,82,32,78,63,57,2,86,31,19,92,14,97,20,56,88,81,70,61,42,99,23,98]


# making a matrix for every board passed might be memory intensive
# could loop through and find out the position of each board
# board 1 = 0:75
# board 2 = 76:150 (75+75=150)
# board 3 = 151:225 (150+75=225)...

# first row match [0:15]
# second row match [+15:+15]...
# first column match [0:2,15:17,30:32,45:47,60:62]
# second column match [+3:+3]...

# second matrix first row match []
matches = []

print(data[76:78])
# loop through data 
    # if match find position 
