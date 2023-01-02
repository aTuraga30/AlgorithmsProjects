"""
Tic Tac Toe Player
"""

import math

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
    copy_of_board = board[:]
    player_to_play = player(copy_of_board)

    row = action[0]
    spot = action[1]

    for line in range(len(copy_of_board)):
        if line == row:
            for item in range(len(copy_of_board[line])):
                if item == spot and copy_of_board[line][item] == EMPTY:
                    copy_of_board[line][item] = player_to_play
                    return copy_of_board
    
    raise Exception
 

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if (board[0][0] and board[0][1] and board[0][2] == "X" or 
       board[1][0] and board[1][1] and board[1][2] == "X" or
       board[2][0] and board[2][1] and board[2][2] == "X" or 
       board[0][0] and board[1][0] and board[2][0] == "X" or
       board[0][1] and board[1][1] and board[2][1] == "X" or
       board[0][2] and board[1][2] and board[2][2] == "X" or 
       board[0][0] and board[1][1] and board[2][2] == "X" or 
       board[2][0] and board[1][1] and board[0][2] == "X"):

       return "X"

    elif (board[0][0] and board[0][1] and board[0][2] == "O" or 
       board[1][0] and board[1][1] and board[1][2] == "O" or
       board[2][0] and board[2][1] and board[2][2] == "O" or 
       board[0][0] and board[1][0] and board[2][0] == "O" or
       board[0][1] and board[1][1] and board[2][1] == "O" or
       board[0][2] and board[1][2] and board[2][2] == "O" or 
       board[0][0] and board[1][1] and board[2][2] == "O" or 
       board[2][0] and board[1][1] and board[0][2] == "O"):
       
       return "O"
    
    else:
        return None

sol = winner(
    [["X", "O", "O"],
    [EMPTY, "X", EMPTY],
    [EMPTY, EMPTY, "X"]]
)

print(sol)

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError