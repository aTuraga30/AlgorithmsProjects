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

    raise Exception("Invalid Move")


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


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    is_board_terminal = terminal(board)
    player_to_play = player(board)

    if is_board_terminal == True:
        return None

    if player_to_play == "X":
        max_player_value, max_player_move = max_value(board)
        return max_player_move

    elif player_to_play == "O":
        min_player_value, min_player_move = min_value(board)
        return min_player_move


def max_value(board):
    is_board_terminal = terminal(board)

    if is_board_terminal == True:
        return utility(board), None

    v = -math.inf
    player_move = None

    for action in actions(board):
        max_instance_value, max_player_action = min_value(result(board, action))

        if max_instance_value > v:
            v = max_instance_value
            player_move = action

            if v == 1:
                return v, player_move

    return v, player_move


def min_value(board):
    is_board_terminal = terminal(board)

    if is_board_terminal == True:
        return utility(board), None

    v = math.inf
    player_move = None

    for action in actions(board):
        min_instance_value, min_player_action = max_value(result(board, action))

        if min_instance_value < v:
            v = min_instance_value
            player_move = action

            if v == -1:
                return v, player_move

    return v, player_move
