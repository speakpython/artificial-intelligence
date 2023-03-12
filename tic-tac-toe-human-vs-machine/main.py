#https://speakpython.codes/artificial-intelligence/2023/03/09/tic-tac-toe-human-vs-machine.html#variables-initialisation

taken_moves = []
default_values = [' ' for i in range(9)]
players_moves = {
    'X_moves': [],
    'O_moves': []
}
players = ['X', 'O']


#https://speakpython.codes/artificial-intelligence/2023/03/09/tic-tac-toe-human-vs-machine.html#possible-winning-patterns

winning_pattern = [
    
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [1,4,7],
    [2,5,8],
    [3,6,9],
    [1,5,9],
    [3,5,7]
    
]

#https://speakpython.codes/artificial-intelligence/2023/03/09/tic-tac-toe-human-vs-machine.html#grid-box-pattern

def game_grid(value):  
    print("\n")  
    print("\t____________________")  
    print("\t|      |      |     |")  
    print("\t|    {} |  {}   |  {}  |".format(value[0], value[1], value[2]))  
    print('\t|______|______|_____|')  
    print("\t|      |      |     |") 
    print("\t|   {}  |  {}   |  {}  |".format(value[3], value[4], value[5]))  
    print('\t|______|______|_____|')  
    print("\t|      |      |     |")  
    print("\t|  {}   |  {}   |  {}  |".format(value[6], value[7], value[8]))  
    print('\t|______|______|_____|')
    print("\n") 


#https://speakpython.codes/artificial-intelligence/2023/03/09/tic-tac-toe-human-vs-machine.html#update-game-state



def update_game(move, player):
    taken_moves.append(move)
    players_moves[player + '_moves'].append(move)
    default_values[move - 1] = player
    return game_grid(default_values)


#https://speakpython.codes/artificial-intelligence/2023/03/09/tic-tac-toe-human-vs-machine.html#decide-winner

def check_winning():
    for player in players_moves:
        for i in winning_pattern:
            if all(j in players_moves[player] for j in i):
                return player      
    return False


#https://speakpython.codes/artificial-intelligence/2023/03/09/tic-tac-toe-human-vs-machine.html#ai-first-move



def initial_move():
    #Acquire Center
    if 5 not in players_moves['X_moves']:
        return 5
    #Acquire any corner
    return random.choice([1,3,7,9])


#https://speakpython.codes/artificial-intelligence/2023/03/09/tic-tac-toe-human-vs-machine.html#ai-winning-move-


def winning_move():
    moves = smart_move(players_moves['X_moves'], players_moves['O_moves'])
    return moves if moves else None



#https://speakpython.codes/artificial-intelligence/2023/03/09/tic-tac-toe-human-vs-machine.html#ai-smart-move-


def smart_move(mine_move, opp_moves):
    next_move = []
    for i in winning_pattern:
        if not [x for x in mine_move if x in i]:
            for j in i:
                if j not in opp_moves:
                    next_move.append(j)
            if len(next_move) == 1:
                return next_move[0]
            next_move = []
    return False


#https://speakpython.codes/artificial-intelligence/2023/03/09/tic-tac-toe-human-vs-machine.html#ai-random-edge-move

def random_edge_move():
    for i in [2,4,6,8]:   
        if i not in taken_moves:
            return i


#https://speakpython.codes/artificial-intelligence/2023/03/09/tic-tac-toe-human-vs-machine.html#driver-code---ai-vs-human

import random
step = 0
game_grid(default_values)
while step < 9 and step >= 0:

    if step >= 4:
        print('Match tied!')
        break
    
    player = "X"
    
    move = int(input(player + " : "))
    if move < 10 and move not in taken_moves:
        step += 1
        update_game(move,player)
        winner = check_winning() if step > 1 else None
        if winner:
            print(winner, 'Won!')
            break
        elif step == 1:
            O_move = initial_move()
        else:
            O_move = winning_move()
            O_move = smart_move(players_moves['O_moves'], players_moves['X_moves']) if not O_move else O_move
            O_move = random_edge_move() if not O_move else O_move
        print("O (Python 🐍): ",O_move)
        player = "O"
        update_game(O_move, player)
        winner = check_winning() if step > 1 else None
        if winner:
            print(winner, 'Won!')
            break
        continue
    print("Invalid move! - either your move is too high or already taken.")

