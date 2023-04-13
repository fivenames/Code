# Minimax - Max-player aims to maximise the score, Min-player aims to minimise the score
# For example, define the outcome as -1, 0, 1 such that -1 is Player Min wins, 0 is a draw, and 1 is Player Max wins

# The algorithm will go through a process of recursion after each action is taken by the oppenent.
# During the recursion, the AI will go through each of the possible action for the AI and the opponent in each stack frame(essentially running throught the game multiple times).
# Finally, the AI checks the score of each of the possible terminal state, and choose the max/min value depending on which player the AI is assigned to.

# The recursion stacks can be represented in a Minimax tree, each node is a score of the terminal state. If the tree is too wide and deep, Alpha-Beta Pruning can be use to optimise,
# max: 4 -----> min: 4, 2 -----> max: 4, 5, 6   max: 2, ?, ?
# Take for example a tree of 2 branches, looking at the first children of the second branch, if it is a value less than the value of the first branch, 
# there is no need to continue looking at the other children, because the second branch can only become smaller or equal to that first children.

# Depth-Limited Minimax can be used to limit the how deep the algorithm goes into the Minimax tree to optimise runtime,
# Implement a evaluation function which estimates the expected utility of the game from the current state.

# Game:
# Initial state
# Player function: returns which players turn in the current state
# Action function: returns legal moves in the current state
# Result function: returns state after action taken
# Terminal function: Check if terminal state reached
# Utility function: return the score of the terminal state

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