import random

# Constants
NORTH = 'n'
EAST = 'e'
SOUTH = 's'
WEST = 'w'

YES = "y"
NO = "n"

def pull_lever(col_row,coins,coins_list_temp):
    try:
        index = coins_list_temp.index(col_row)
    except ValueError:
        pass
    if col_row in coins_list_temp:
        lever = random.choice([YES,NO])
        if lever == 'y':
            coins += 1
            print("You received 1 coin, your total is now {}.".format(coins))
    return coins


def move(direction, col, row):
    ''' Returns updated col, row given the direction '''
    if direction == NORTH:
        row += 1
    elif direction == SOUTH:
        row -= 1
    elif direction == EAST:
        col += 1
    elif direction == WEST:
        col -= 1
    return(col, row)    

def is_victory(col, row):
    ''' Return true if player is in the victory cell '''
    return col == 3 and row == 1 # (3,1)

def print_directions(directions_str):
    print("You can travel: ", end='')
    first = True
    for ch in directions_str:
        if not first:
            print(" or ", end='')
        if ch == NORTH:
            print("(N)orth", end='')
        elif ch == EAST:
            print("(E)ast", end='')
        elif ch == SOUTH:
            print("(S)outh", end='')
        elif ch == WEST:
            print("(W)est", end='')
        first = False
    print(".")
        
def find_directions(col, row):
    ''' Returns valid directions as a string given the supplied location '''
    if col == 1 and row == 1:   # (1,1)
        valid_directions = NORTH
    elif col == 1 and row == 2: # (1,2)
        valid_directions = NORTH+EAST+SOUTH
    elif col == 1 and row == 3: # (1,3)
        valid_directions = EAST+SOUTH
    elif col == 2 and row == 1: # (2,1)
        valid_directions = NORTH
    elif col == 2 and row == 2: # (2,2)
        valid_directions = SOUTH+WEST
    elif col == 2 and row == 3: # (2,3)
        valid_directions = EAST+WEST
    elif col == 3 and row == 2: # (3,2)
        valid_directions = NORTH+SOUTH
    elif col == 3 and row == 3: # (3,3)
        valid_directions = SOUTH+WEST
    return valid_directions

def play_one_move(col, row, valid_directions, coins, coins_list_temp, invalid_moves, valid_moves):
    ''' Plays one move of the game
        Return if victory has been obtained and updated col,row '''
    victory = False
    direction = random.choice([NORTH, EAST, SOUTH, WEST])
    direction = direction.lower()

    if not direction in valid_directions:
        col_row =str(col)+"."+str(row)
        if col_row in coins_list_temp:
            index = coins_list_temp.index(col_row)
            coins_list_temp.pop(index)
            invalid_moves += 1
        print("Not a valid direction!")

    else:
        col, row = move(direction, col, row)
        col_row =str(col)+"."+str(row)
        coins = pull_lever(col_row,coins,coins_list_temp)
        victory = is_victory(col, row)
        valid_moves += 1
    return victory, col, row, coins, invalid_moves, valid_moves


# The main program starts here
def play():
    victory = False
    row = 1
    col = 1
    coins = 0
    valid_moves = 0
    invalid_moves = 0
    coins_list_temp = ['1.2','2.2','2.3','3.2']

    while not victory:
        valid_directions = find_directions(col, row)
        print_directions(valid_directions)
        victory, col, row ,coins, invalid_moves, valid_moves = play_one_move(col, row, valid_directions, coins, coins_list_temp, invalid_moves, valid_moves)
        total_moves = valid_moves + invalid_moves
    print("Victory! Total coins {}. Moves {}".format(coins, total_moves))
    return input("Play again (y/n): ")

play_again = "y"
while play_again.lower() == "y":
    random.seed(int(input("Input seed: ")))
    play_again = play()