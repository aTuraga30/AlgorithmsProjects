"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """

    x_count = 0
    o_count = 0

    for line in range(len(board)):
        for item in board[line]:
            if item == "X":
                x_count += 1

            elif item == "O":
                o_count += 1
        
    if x_count > o_count:
        return "O"

    else:
        return "X"


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions_set = set()

    for line in range(len(board)):
        for item in range(len(board[line])):
            if board[line][item] == EMPTY:
                action_pairs = tuple((line, item))
                actions_set.add(action_pairs)
    
    return actions_set


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    copy_of_board = copy.deepcopy(board)
    player_to_play = player(copy_of_board)

    row = action[0]
    spot = action[1]

    for line in range(len(copy_of_board)):
        if line == row:
            for item in range(len(copy_of_board[line])):
                if item == spot and copy_of_board[line][item] == EMPTY:
                    copy_of_board[line][item] = player_to_play
    
    return copy_of_board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if ((board[0][0] == "X" and board[0][1] == "X" and board[0][2] == "X") or 
       (board[1][0] == "X" and board[1][1] == "X" and board[1][2] == "X") or
       (board[2][0] == "X" and board[2][1] == "X" and board[2][2] == "X") or 
       (board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X") or
       (board[0][1] == "X" and board[1][1] == "X" and board[2][1] == "X") or
       (board[0][2] == "X" and board[1][2] == "X" and board[2][2] == "X") or 
       (board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X") or 
       (board[2][0] == "X" and board[1][1] == "X" and board[0][2] == "X")):

       return "X"
    
    elif ((board[0][0] == "O" and board[0][1] == "O" and board[0][2] == "O") or 
       (board[1][0] == "O" and board[1][1] == "O" and board[1][2] == "O") or
       (board[2][0] == "O" and board[2][1] == "O" and board[2][2] == "O") or 
       (board[0][0] == "O" and board[1][0] == "O" and board[2][0] == "O") or
       (board[0][1] == "O" and board[1][1] == "O" and board[2][1] == "O") or
       (board[0][2] == "O" and board[1][2] == "O" and board[2][2] == "O") or 
       (board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O") or 
       (board[2][0] == "O" and board[1][1] == "O" and board[0][2] == "O")):
       
       return "O"
    
    else:
        return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    winner_of_board = winner(board)
    empty_spots_count = 0

    for line in range(len(board)):
        for item in range(len(board[line])):
            if board[line][item] == EMPTY:
                empty_spots_count += 1

    if winner_of_board == "X" or winner_of_board == "O":
        return True

    elif empty_spots_count == 0:
        return True

    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winner_of_board = winner(board)

    if winner_of_board == "X":
        return 1
    
    elif winner_of_board == "O":
        return -1
    
    else:
        return 0

'''
def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    is_board_terminal = terminal(board)
    player_to_play = player(board)

    if is_board_terminal == True:
        return None
    
    else:
        if player_to_play == "X":
            for action in actions(board):
                lowest_possible_val = -math.inf
                max_player_play = min_value(board)

                if max_player_play > lowest_possible_val:
                    lowest_possible_val = max_player_play
                    action_to_take = action

            return action_to_take

        elif player_to_play == "O":
            #action_to_take = min_value(board)
            for action in actions(board):
                highest_possible_val = math.inf
                min_player_play = max_value(board)

                if min_player_play < highest_possible_val:
                    highest_possible_val = min_player_play
                    action_to_take = action

            return action_to_take

def min_value(board):
    is_board_terminal = terminal(board)

    if is_board_terminal == True:
        return utility(board)
    
    v = math.inf

    for action in actions(board):
        v = min(v, max_value(result(board, action)))
        #min_player_play = max_value(board)

        #if min_player_play < v:
            #v = min_player_play
            #action_to_take = action

    return v

def max_value(board):
    is_board_terminal = terminal(board)

    if is_board_terminal == True:
        return utility(board)
    
    v = -math.inf

    for action in actions(board):
        v = max(v, min_value(result(board, action)))
        #max_player_play = min_value(board)

        #if max_player_play > v:
            #v = max_player_play
            #action_to_take = action

    return v
'''
def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    else:
        if player(board) == X:
            value, move = max_value(board)
            return move
        else:
            value, move = min_value(board)
            return move


def max_value(board):
    if terminal(board):
        return utility(board), None

    v = float('-inf')
    move = None
    for action in actions(board):
        # v = max(v, min_value(result(board, action)))
        aux, act = min_value(result(board, action))
        if aux > v:
            v = aux
            move = action
            if v == 1:
                return v, move

    return v, move


def min_value(board):
    if terminal(board):
        return utility(board), None

    v = float('inf')
    move = None
    for action in actions(board):
        # v = max(v, min_value(result(board, action)))
        aux, act = max_value(result(board, action))
        if aux < v:
            v = aux
            move = action
            if v == -1:
                return v, move

    return v, move

sol2 = minimax([[EMPTY, EMPTY, EMPTY],
            [EMPTY, "X", EMPTY],
            [EMPTY, EMPTY, EMPTY]])

sol = minimax([["O", EMPTY, "O"],
            [EMPTY, "X", EMPTY],
            ["X", "X", EMPTY]])

print(sol)
