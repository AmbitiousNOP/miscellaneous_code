
import re

puzzle_input = []
with open("day_3_puzzle_input.txt") as f:
    for line in f:
        puzzle_input.append(line)


symbols = ["!","@","#","$","%","^","&","*","(",")","_","-","+","=","{","}","\\","|",":",";","\"","'",
    ",","<",">","/","?","`","~","[","]"]
num_cords = {}
num_pattern = re.compile("(\d{1,})")
symbol_pattern = re.compile("([^A-Za-z0-9.\n])")

total = 0
# loop over puzzle_input to find all number positions
for idx, elem in enumerate(puzzle_input):
    # method (2) on match check above row and below row at left, right, below, or above for value
    for m in num_pattern.finditer(elem):
        #idx holds the row num & m.span() holds the position within the row
        #detect left
        if (m.start() > 0) & (puzzle_input[idx][m.start()-1] in symbols):
            total += int(m.group())
        #detect right
        if (m.end() < len(puzzle_input[0])) & (puzzle_input[idx][m.end()] in symbols):
            total += int(m.group())
        # detect above
        if (idx > 0):
            if int(m.end()) == len(puzzle_input[0]):
                for s in puzzle_input[idx-1][m.start()-1:m.end()]:
                    if s in symbols:
                        total += int(m.group())
            else:
                for s in puzzle_input[idx-1][m.start()-1:m.end()+1]:
                    if s in symbols:
                        total += int(m.group())
        # detect below
        if (idx < (len(puzzle_input)-1)):
            if int(m.start()) == 0:
                for s in puzzle_input[idx+1][m.start():m.end()+1]:
                    if s in symbols: 
                        total += int(m.group())
            else:
                for s in puzzle_input[idx+1][m.start()-1:m.end()+1]:
                    if s in symbols: 
                        total += int(m.group())

print(total)