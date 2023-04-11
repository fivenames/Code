# initial state - the problem at hand.
# actions - stops of action to take from the initial state to the goal state.
# transition model - describes how each action taken will output a certain state. A state space is a graph of intermediate states via a sequence of actions.
# goal test - test whether the goal state is reached
# path cost function - measures the cost of solution, can be money, time etc.

# To solve a seach problem, data is stored as nodes;
# - a state
# - a parent (from the prev node)
# - an action (action from parent to result here)
# - a path cost (from the initial state)