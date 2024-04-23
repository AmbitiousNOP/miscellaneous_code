"""
create a game of tic-tac-toe

 X | X | X
 ---------
 O | O | O
 ---------
 X | X | X
"""


def tictactoe():

    place_values = [[" "," "," "],
                    [" "," "," "],
                    [" "," "," "]]

    while True:
        # print the board
        print(f" Row:   1   2   3\n  1\t{place_values[0][0]} | {place_values[0][1]} | {place_values[0][2]} \n \t---------\n  2\t{place_values[1][0]} | {place_values[1][1]} | {place_values[1][2]}\n \t---------\n  3\t{place_values[2][0]} | {place_values[2][1]} | {place_values[2][2]}")
        
        # checking for win
        if (place_values[0][0] != " ") & (place_values[0][1] != " ") & (place_values[0][2] != " "):
            print("Win on Row 1")
            break
        elif (place_values[1][0] != " ") & (place_values[1][1] != " ") & (place_values[1][2] != " "):
            print("Win on Row 2")
            break
        elif (place_values[2][0] != " ") & (place_values[1][1] != " ") & (place_values[2][2] != " "):
            print("Win on Row 3")
            break
        elif (place_values[0][0] != " ") & (place_values[1][1] != " ") & (place_values[0][2] != " "):
            print("Win on a Diagonal")
            break
        elif (place_values[0][2] != " ") & (place_values[1][1] != " ") & (place_values[2][0] != " "):
            print("Win on a Diagonal")
            break
        elif (place_values[0][0] != " ") & (place_values[1][0] != " ") & (place_values[2][0] != " "):
            print("Vertical win on column 1")
            break
        elif (place_values[0][1] != " ") & (place_values[1][1] != " ") & (place_values[2][1] != " "):
            print("Vertical win on column 2")
            break
        elif (place_values[0][2] != " ") & (place_values[1][2] != " ") & (place_values[2][2] != " "):
            print("Vertical win on column 3")
            break
        else:
            # ask player for coords
            player_choice = [int(elm) for elm in input("Enter your coord's ").split(",")]
            # update the coords
            place_values[player_choice[1]-1][player_choice[0]-1] = "X"


tictactoe()




