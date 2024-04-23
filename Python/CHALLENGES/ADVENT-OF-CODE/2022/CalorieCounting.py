

file = open("input.txt", "r")


# read in the data
# create a list of list seperated by an empty line
# calc each lists sum and return the largest value
#data = [[[i]] for i in file.read().split("\n")]

# create a list
# create new list and sep by elem ''


def tmp():
    fin_lst = []
    tmp_lst = []
    for i in file.read().split("\n"):
        if i == '':
            tmp_lst.clear()
        tmp_lst.append(i)
    print(tmp_lst)
        fin_lst.append(tmp_lst)
    print(fin_lst) 

tmp()
