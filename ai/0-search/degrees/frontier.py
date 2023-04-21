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

# For a seach problem, data is stored as nodes;
#   a state
#   a parent (from the prev node)
#   an action (action from parent to result here)
#   a path cost (from the initial state)
class Node():
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action


# Depth-first search(The AI will go deep into one path chosen), it is achieve by using stack model when removing nodes from the frontier.
class StackFrontier():
    def __init__(self):
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
            raise Exception("empty frontier")
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
            raise Exception("empty frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node

# for informed search:
'''
Greedy Best-First Search algorithm implements a heuristic function that returns an estimated cost to reach the goal state, from the current state.
When comes to a decision point, the alogorithm expands the node of lowest heuristic value.

A* Search algorithm expands node with lowest (heuristic value + path cost to reach current node), 
this idea builds on attempting to take even lower cost path to reach the nodes with slightly higher heuristic value.
Greedy Best-First Search alogorithm on the other hand, may ended up accumulating a large path cost by only looking at heuristic value,
as the heuristic value can increase and decrease between nodes but maintaining in the lower range. (Heuristic value is just an estimate using known information)

A* Search algorithm can always produce the optimal solution(lower path cost) provided the following criteria:
The heuristic function willl never over-estimate the cost to reach the goal state, under-estimate is allowed. (The heuristic function is admissible)
The value of (heuristic value + path cost to reach current node) should never be more than this value of all the successor nodes. (The heuristic function is consistent)
'''

