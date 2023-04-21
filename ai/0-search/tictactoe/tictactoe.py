"""
Tic Tac Toe Player
"""
# Game:
# Initial state
# Player function: returns which players turn in the current state
# Action function: returns legal moves in the current state
# Result function: returns state after action taken
# Terminal function: Check if terminal state reached
# Utility function: return the score of the terminal state

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
            elif board[i][j] == O:
                counter_O += 1
            else:
                pass
    
    if counter_X + counter_O == 9:
        return None
    elif counter_X - counter_O == 1:
        return O
    elif counter_X == counter_O:
        return X
    else:
        return None

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    action = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                action.add((i, j))
    
    if terminal(board):
        return None
            
    return action


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    X_O = player(board)
    if action not in actions(board):
        raise Exception(f"Invalid action: {action}")
    i, j = action
    # Create a deep copy, plainly assigning new_board to board will be pointing new_board to what board is pointing.
    new_board = [[cell for cell in row] for row in board]
    new_board[i][j] = X_O
    
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # check horizontal cases
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return board[i][0]

    # check vertical cases
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return board[0][i]

    # check diagonal cases
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]

    return None
         
def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
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
    return 0

# Game:
    # current state:
    # Max-player picks the action in Action(state) that produces highest value for Min-Value(Result(state, action))
    # Min-player picks the action in Action(state) that produces lowest value for Max-Value(Result(state, action))

# def Max-Value(state):
    # if Terminal(state):
        # return Utility(state)
    # score = -infinity
    # for action in Action(state):
        # score = Max(score, Min-Value(Result(state, action)))
    # return score

# def Min-Value(state):
    # if Terminal(state):
        # return Utility(state)
    # score = infinity
    # for action in Action(state):
        # score = Min(score, Max-Value(Result(state, action)))
    # return score

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    ai = player(board)
    if ai == X:
        if(board == initial_state()):
            return (1, 1)
        _, best_move = max_value(board)
    elif ai == O:
        _, best_move = min_value(board)
    
    return best_move

def max_value(board):
    if terminal(board):
        return utility(board), None
    
    best_score = -1
    best_move = None
    
    for action in actions(board):
        # Recrusively calling min_value and max_value to play the whole game, until terminal state, return final score and None
        score, _ = min_value(result(board, action))
        if score > best_score:
            best_score = score
            # The next possible action that is passed into the result to conduct recursion is keep track of.
            best_move = action
    
    return best_score, best_move

def min_value(board):
    if terminal(board):
        return utility(board), None
    
    best_score = 1
    best_move = None
    
    for action in actions(board):
        score, _ = max_value(result(board, action))
        if score < best_score:
            best_score = score
            best_move = action
    
    return best_score, best_move

'''
Minimax - Max-player aims to maximise the score, Min-player aims to minimise the score
For example, define the outcome as -1, 0, 1 such that -1 is Player Min wins, 0 is a draw, and 1 is Player Max wins

The algorithm will go through a process of recursion after each action is taken by the oppenent.
During the recursion, the AI will go through each of the possible action for the AI and the opponent in each stack frame(essentially running throught the game multiple times).
Finally, the AI checks the score of each of the possible terminal state, and choose the max/min value depending on which player the AI is assigned to.

The recursion stacks can be represented in a Minimax tree, each node is a score of the terminal state. If the tree is too wide and deep, Alpha-Beta Pruning can be use to optimise,
max: 4 -----> min: 4, 2 -----> max: 4, 5, 6   max: 2, ?, ?
Take for example a tree of 2 branches, looking at the first children of the second branch, if it is a value less than the value of the first branch, 
there is no need to continue looking at the other children, because the second branch can only become smaller or equal to that first children.

Depth-Limited Minimax can be used to limit the how deep the algorithm goes into the Minimax tree to optimise runtime,
Implement a evaluation function which estimates the expected utility of the game from the current state. 
'''

