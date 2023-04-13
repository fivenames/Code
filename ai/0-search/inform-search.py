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

