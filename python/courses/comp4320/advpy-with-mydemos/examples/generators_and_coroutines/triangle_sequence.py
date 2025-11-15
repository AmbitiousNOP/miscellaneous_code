#!/usr/bin/env python

max_rows = int(input("Max logs that will be placed on the bottom row? "))

# create a generator expression that generates the triangle sequence.
logs =(row * (row + 1) // 2 for row in range(1, max_rows + 1))
#logs = [row * (row + 1) // 2 for row in range(1, max_rows + 1)]
print(type(logs))
fmt = '{:^10}' * 2
print(fmt.format("#Rows", "#Logs"))
for rows, log in enumerate(logs, start=1):    
    #if rows > 2 : break
    print(fmt.format(rows, log))
