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

part 2:
Write an interactive script that asks for a president’s last name.
● For each president whose last name matches, print out their date of birth and date of death.
● For presidents who are still alive, print three asterisks for the date of death.
NOTE Dates of death and term end date might be the string "NONE".
"""

output = {}
with open("/home/cjpenn/comp4320/ADVPY-with-mydemos/data/presidents.txt") as f:
    for i in f.read().split("\n")[0:-1]:
        try:
            data = i.split(":")
            output[data[1].lower()] = data[3:5] 
        except:
            #output[(i.split(":")[6])] = 1
            continue

pres_req = input("Enter a presidents name: ").lower()
if output[pres_req][1] == "NONE":
    print(f"Birth: {output[pres_req][0]} Death: ***")
else:
    print(f"Birth: {output[pres_req][0]} Death: {output[pres_req][1]}")
