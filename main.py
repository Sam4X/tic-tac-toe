import datetime
import random
import numpy as np

start = datetime.datetime.now()
random.seed(1)

def create_board(row_dim, col_dim):
    board = np.zeros((row_dim, col_dim), dtype=int)
    return board

board = create_board(3,3)
print('New empty board has been created \n')
print(board)

def place(board, player, position):
    player_list = [1,2]
    if player in player_list:
        print('Current player is: Player ' + str(player))
    else:
        print('Cannot play, Player number can either be 1 or 2. You have entered player number:' + str(player))
    if board[(position)] == 0:
        board[(position)] = player
    else:
        print('Current board position ' + str(position) + ' cannot be modified')
    return board

# place(board, 1, (0,0))
# print(board)

def possibilities(board):
    (i,j) = board.shape
    poss = list()
    possibilities = list()
    for x in range(0,i):
        for y in range(0,j):
            index = (x,y)
            poss.append(index)
    for i in range(0, len(poss)):
        (p,q) = poss[(i)]
        if board[(p,q)] == 0:
            possibilities.append(poss[(i)])
    return possibilities

# a = possibilities(board)
# print(a)

def random_place(board, player):
    selections = possibilities(board)
    if len(selections) > 0:
        selection = random.choice(selections)
        place(board, player, selection)
    return board

def row_win(board, player):
    for i in range(3):
        if np.any(np.all(board==player, axis=1)):
            return True
        else:
            return False

def col_win(board, player):
    for i in range(3):
        if np.any(np.all(board==player, axis=0)):
            return True
        else:
            return False

def diag_win(board, player):
    for i in range(3):
        if np.any(np.all(board==player, axis=0)):
            return True
        else:
            return False

def evaluate(board, player):
    # check row win
    for i in range(3):
        if np.any(np.all(board==player, axis=1)):
            a = True
        else:
            a = False
    # check column win
    for i in range(3):
        if np.any(np.all(board==player, axis=0)):
            b = True
        else:
            b = False
    # check diagonal win
    if np.all(np.diagonal(board) == player) or np.all(np.diagonal(np.fliplr(board)) == player):
        c = True
    else:
        c = False

    # return  win value
    if a == True:
        print('Player ' + str(player) + ' has won in row')
        return True
    elif b == True:
        print('Player ' + str(player) + ' has won in column')
        return True
    elif c == True:
        print('Player ' + str(player) + ' has won in diagonal')
        return True
    elif np.all(board != 0):
        print('Game is  a draw. Please restart the game!')
        return False
    # else:
    #     print('Player ' + str(player) + ' has not won in any direction! Please continue playing...')

def play(games):
    win_counter = np.zeros((1, 3), dtype=int)
    for k in range(games):
        board = create_board(3, 3)
        for i in range(5):
            for player in [1, 2]:
                random_place(board, player)
            for j in [1, 2]:
                check = evaluate(board, j)
                if check == True:
                    win_counter[(0,j)] += 1
                    break
                elif check == False:
                    win_counter[(0,0)] += 1
                    break
            if check == True:
                break
    return win_counter

def play_strategic_game(games):
    # win_counter[(0)] == number of draw games
    # win_counter[(1)] == number of player 1 wins
    # win_counter[(2)] == number of player 2 wins
    win_counter = np.zeros((1, 3), dtype=int)
    for k in range(games):
        board = create_board(3, 3)
        for i in range(5):
            for player in [1, 2]:
                if i == 0 and player == 1:
                    print('Current player is: Player ' + str(player))
                    board[(1,1)] = 1
                else:
                    random_place(board, player)
            for j in [1, 2]:
                check = evaluate(board, j)
                if check == True:
                    win_counter[(0,j)] += 1
                    break
                elif check == False:
                    win_counter[(0,0)] += 1
                    break
            if check == True:
                break
    return win_counter

# win_counter = np.zeros((1, 3), dtype=int)
# for i in range(5):
#     for player in [1, 2]:
#         if i == 0 and player == 1:
#             print('Current player is: Player ' + str(player))
#             board[(1, 1)] = 1
#         else:
#             random_place(board, player)
#         print(board)
#     for j in [1, 2]:
#         check = evaluate(board, j)
#         if check == True:
#             win_counter[(0, j)] += 1
#             break
#         elif check == False:
#             win_counter[(0, 0)] += 1
#             break
#     if check == True:
#         break

count = play(1000)
count_str = play_strategic_game(1000)
print('Final Win Counter (normal game):')
print(count)
print('Final Win Counter (strategic game):')
print(count_str)


print('\nElapsed time for program execution:', datetime.datetime.now() - start)