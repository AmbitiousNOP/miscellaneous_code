"""
Calculate the horizontal position and depth you would have after 
following the planned course. What do you get if you multiply your 
final horizontal position by your final depth?
"""


file = open("input-2.txt", "r")

movement = [i for i in file.read().split("\n") if i != ""]


# possible commands
# Forward
# Down 
# Up

h_pos = 0   # horizontal position
d_pos = 0   # depth position

# loop through movement 
# split the line by \s into a tmp list
# if [0] contains forward
    # add [1] to h_pos
# if [0] contains down
    # sub [1] from d_pos
# if [0] contains up
    # add [1] to d_pos

def answer():
    for line in movement:
        tmp_lst = line.split(" ")

        if tmp_lst[0] == "forward":
            h_pos += int(tmp_lst[1])
        elif tmp_lst[0] == "down":
            d_pos += int(tmp_lst[1])
        elif tmp_lst[0] == "up":
            d_pos -= int(tmp_lst[1])
        
    print(d_pos * h_pos)