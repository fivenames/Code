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
    counter_X = 0
    counter_O = 0

    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                counter_X += 1
            else:
                counter_O += 1
    
    if counter_X + counter_O == 9:
        return None
    elif counter_X - counter_O == 1:
        return O
    elif counter_X == counter_O:
        return X
    else:
        raise Exception

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    action = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                action.add((i, j))
            
    if action == None:
        return None

    return action


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    X_O = player(board)
    i, j = action
    board[i][j] = X_O
    
    return board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # check whose turn curerently
    X_O = player(board)
    if X_O == X:
        X_O = O
    elif X_O == O:
        X_O = X

    # check if the other party has won:
        # check horizontal cases
    for i in range(3):
        if winning_counter == 3:
            return X_O
        winning_counter = 0
        for j in range(3):
            if board[i][j] != X_O:
                break
            else:
                winning_counter += 1

        # check vertical cases
    for i in range(3):
        if winning_counter == 3:
            return X_O
        winning_counter = 0
        for j in range(3):
            if board[j][i] != X_O:
                break
            else:
                winning_counter += 1

        # check diagonal cases
    for i, j in range(3):
        if winning_counter == 3:
            return X_O
        winning_counter = 0
        if board[i][j] == X_O:
            winning_counter += 1

    j = 2
    for i in range(3):
        if winning_counter == 3:
            return X_O
        winning_counter = 0       
        if board[i][j] == X_O:
            winning_counter += 1
            j -= 1
        else:
            break
    
    return None
        

         
def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if (winner(board) == None):
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    return False
    
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    X_O = winner(board)
    if(X_O == X):
        return 1
    elif(X_O == O):
        return -1
    elif(terminal(board)):
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return utility()
