''' 
Solving search problem:
    Initial state - the problem at hand.
    Actions - stops of action to take from the initial state to the goal state.
    Transition model - describes how each action taken will output a certain state. A state space is a graph of intermediate states via a sequence of actions.
    Goal test - test whether the goal state is reached
    Path cost function - measures the cost of solution, can be money, time etc. 
'''

# To solve a seach problem, data is stored as nodes;
#   a state
#   a parent (from the prev node)
#   an action (action from parent to result here)
#   a path cost (from the initial state)
class Node:
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action

'''
Frontier is a storage of nodes:
    Starts with initial state(starting node)
    Starts with an empty list of explored nodes
    Loop:
        If frontier is empty, return no solution
        Remove a node from the frontier
        If the node is a goal state, return the solution
        Add the removed node to the explored nodes list
        Expand node, add the resulting nodes to the frontier is they are not in the explored nodes list.
'''
    
# Depth-first search(The AI will go deep into one path chosen), it is achieve by using stack model when removing nodes from the frontier.
class StackFrontier:
    def __init__(self) -> None:
        self.frontier = []
        
    def add(self, node):
        self.frontier.append(node)
    
    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)
    
    def empty(self):
        # return Ture or False
        return len(self.frontier) == 0
    
    def remove(self):
        if self.empty():
            raise Exception("Empty Frontier")
        else:
            # index '-1' into list outputs the last element in the list
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node

# Breadth-first search(The AI will alternate between two different routes, exploring the nodes with the lowest cost path first), it is achieve by using queue model instead.
class QueueFrontier(StackFrontier):
    # Polymorphism
    def remove(self):
        if self.empty():
            raise Exception("Empty Frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node