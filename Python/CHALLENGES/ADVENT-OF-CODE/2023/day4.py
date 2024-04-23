

total_score = 0
with open("example.txt") as f:
    for line in f:
        winning_numbers = line.split("|")[0].split(":")[1].split()
        my_numbers = line.strip().split("|")[1].split()
        game_points = 0
        for n in my_numbers:
            if n in winning_numbers:
                if game_points == 0:
                    game_points += 1
                else:
                    game_points = game_points*2
                
        total_score += game_points

print(total_score)