import re

f = open("/Users/cjpenn/CODE/PythonProjects/CHALLENGES/ADVENT-OF-CODE/2023/day_1_puzzle_input.txt", "r")

spelled_out = {"zero":"0",
               "one": "1",
               "two": "2",
               "three": "3",
               "four": "4",
               "five": "5",
               "six": "6",
               "seven":"7",
               "eight":"8",
               "nine":"9"}

puzzle_input = f.readlines()

pattern = re.compile("\d|one|two|three|four|five|six|seven|eight|nine")
cleaned_list = []
for line in puzzle_input:
    cleaned_list.append(re.findall(pattern, line))

for index_m, elem in enumerate(cleaned_list):
    for index_l,item in enumerate(elem):
        if item in spelled_out.keys():
            cleaned_list[index_m][index_l] = spelled_out[item]
        

ans = []
for i in cleaned_list:
    ans.append(int(i[0] + i[-1]))

print(sum(ans))
    

total = 0
for n in cleaned_list:
    total += int(n[0] + n[-1])

print(total)


