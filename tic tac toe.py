# simple tic tac toe I guess


print("Welcome to tic tac toe")
print("Enter the place number where you want to input ur \"x\" or \"0\"")

# SIGN
""" -│-│-
    -│-│-
    -│-│-"""

# "o"
""" O│O│O
    O│O│O
    O│O│O"""
# "X"
""" X│X│X
    X│X│X
    X│X│X """


#\
# func
def model(pos1,pos2,pos3,pos4,pos5,pos6,pos7,pos8,pos9): # The board where the games is initiate
    model = "{}│{}│{}\n{}│{}│{}\n{}│{}│{}".format(pos1,pos2,pos3,pos4,pos5,pos6,pos7,pos8,pos9)
    return model

def update(place,player): # updates the board value
    global value_to_change
    value_to_change[place] = player
    global board
    board = model(value_to_change[0],value_to_change[1],value_to_change[2],value_to_change[3],value_to_change[4],value_to_change[5],value_to_change[6],value_to_change[7],value_to_change[8])
    return board

def turns(turn): # basically this game turn can be cateriozed into odd or even e.g odd = x and even = 0 
    if turn%2 == 0:
        global p1
        return p1
    else:
        global p2
        return p2


def anyone_win():
    global value_to_change
    global p1
    global p1_win
    global p2
    global p2_win
    # row of p1
    if value_to_change[0] == p1 and value_to_change[1] == p1 and value_to_change[2]  == p1:
        p1_win = True
        return p1_win
    elif value_to_change[3] == p1 and value_to_change[4] == p1 and value_to_change[5] == p1:
        p1_win = True
        return p1_win   
    elif value_to_change[6] == p1 and value_to_change[7] == p1 and value_to_change[8] == p1:
        p1_win = True
        return p1_win

    # colomn of p1
    elif value_to_change[0] == p1 and value_to_change[3] == p1 and value_to_change[6] == p1:
        p1_win = True
        return p1_win
    elif value_to_change[1] == p1 and value_to_change[4] == p1 and value_to_change[7] == p1:
        p1_win = True
        return p1_win   
    elif value_to_change[2] == p1 and value_to_change[5] == p1 and value_to_change[8] == p1:
        p1_win = True
        return p1_win

    # diagonal of p1
    elif value_to_change[0] == p1 and value_to_change[4] == p1 and value_to_change[8] == p1:
        p1_win = True
        return p1_win

    elif value_to_change[2] == p1 and value_to_change[4] == p1 and value_to_change[6] == p1:
        p1_win = True
        return p1_win
    
    # row of p2
    if value_to_change[0] == p2 and value_to_change[1] == p2 and value_to_change[2] == p2:
        p2_win = True
        return p2_win
    elif value_to_change[3] == p2 and value_to_change[4] == p2 and value_to_change[5] == p2:
        p2_win = True
        return p2_win   
    elif value_to_change[6] == p2 and value_to_change[7] == p2 and value_to_change[8] == p2:
        p2_win = True
        return p2_win

    # colomn of p2
    elif value_to_change[0] == p2 and value_to_change[3] == p2 and value_to_change[6] == p2:
        p2_win = True
        return p2_win
    elif value_to_change[1] == p2 and value_to_change[4] == p2 and value_to_change[7] == p2:
        p2_win = True
        return p2_win   
    elif value_to_change[2] == p2 and value_to_change[5] == p2 and value_to_change[8] == p2:
        p2_win = True
        return p2_win

    # diagonal of p2
    elif value_to_change[0] == p2 and value_to_change[4] == p2 and value_to_change[8] == p2:
        p2_win = True
        return p2_win

    elif value_to_change[2] == p2 and value_to_change[4] == p1 and value_to_change[6] == p1:
        p2_win = True
        return p2_win    
def reset(): # bassically reset the games
    global default_value_to_change
    global value_to_change
    global p1_win 
    global p2_win

    p1_win = False
    p2_win = False
    value_to_change = default_value_to_change
    return value_to_change




# begin froms here
turn = 4 # changing "o" and "x"
p1 = "X"
p2 = "O"
none = "-"
p1_win = False
p2_win = False


default_value_to_change = [
         none,none,none,
         none,none,none,
         none,none,none
         ]

value_to_change = [
         none,none,none,
         none,none,none,
         none,none,none
         ]

board = model(value_to_change[0],value_to_change[1],value_to_change[2],value_to_change[3],value_to_change[4],value_to_change[5],value_to_change[6],value_to_change[7],value_to_change[8])

while True: # game loop
    print(board)
    if p1_win == True:
        print("Congrates, 'P1' you win...")
        decison_play = str.lower(input("Wanna play again yes/no:"))

        if decison_play == "yes":
            reset()
            continue
        else:
            break
    elif p2_win == True:
        print("Congrates, 'P2' you win...")
        decison_play = str.lower(input("Wanna play again yes/no:"))

        if decison_play == "yes":
            reset()
            continue
        else:
            break

    place = int(input("Enter the number of that place:"))
    update(place -1,turns(turn))
    anyone_win()
    turn += 1

# bugs bugs bugs
# whenver I try to play again after 2 times it does not reset
# we can change rewrite the value of value_to_change in game LOL
