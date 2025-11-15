"""
Using the file presidents.txt (in the data folder), count the number of Presidents born in each state.
● The output of the script should be a table with two columns.
▶ The rows should be sorted by state name in the first column and the number of presidents that
were born in that state in the second column.
● The following steps may be helpful in writing the application
▶ Declare a dictionary to hold the data.
▶ Read the file into your script, one line at a time.
▶ Split each line into fields using a colon as the separator.
▶ Add/update the element of the dictionary where the key is the state.
▶ Update the value by 1 each time the state occurs.
"""

output = {}
with open("/home/cjpenn/comp4320/ADVPY-with-mydemos/data/presidents.txt") as f:
    for i in f.read().split("\n")[0:-1]:
        try:
            output[(i.split(":")[6])] += 1
        except:
            output[(i.split(":")[6])] = 1

# sort by state
for i in sorted(output.keys()):
    print(f"{i} {output[i]}")
