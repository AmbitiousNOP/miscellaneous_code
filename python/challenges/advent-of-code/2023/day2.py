import re

f = open("/Users/cjpenn/CODE/PythonProjects/CHALLENGES/ADVENT-OF-CODE/2023/day_2_puzzle_input.txt", "r")

import re 
puzzle_input = f.readlines()


'''
Determine which games would have been possible if the 
bag had been loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes.
What is the sum of the IDs of those games?
'''

bag = {
    "red": 12,
    "green": 13,
    "blue": 14
}

pattern = re.compile("(\w+)")
game_finder = re.compile("(\d+)")

played_cubes = {
    "red": 0,
    "green":0,
    "blue":0,
}

total = 0
for i in puzzle_input:
    game_id = int(re.findall(game_finder, i.split(":")[0])[0])
    for elem in i.split(";"):
        possible = False
        for idx, item in enumerate(re.findall(pattern, elem)):
            match item:
                case "red":
                    played_cubes["red"] += int(re.findall(pattern, elem)[idx-1])
                case "green":
                    played_cubes["green"] += int(re.findall(pattern, elem)[idx-1])
                case "blue":
                    played_cubes["blue"] += int(re.findall(pattern, elem)[idx-1])
            
        if (played_cubes["red"] > bag["red"]) or (played_cubes["green"] > bag["green"]) or (played_cubes["blue"] > bag["blue"]):
            played_cubes = played_cubes.fromkeys(played_cubes, 0)
            break
        else:
            possible = True
            
        # new turn
        played_cubes = played_cubes.fromkeys(played_cubes, 0)


    # new game
    if possible == True:
        total += game_id


print(f"total {total}")


