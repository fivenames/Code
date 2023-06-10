'''
With a clear goal state in mind, meaning the specific configuration/value of the goal is known precisely, uninformed search algorithms can be employed to solve the problem. 
However, when the goal state is not yet clear, the problem can be defined as an optimisation problem within a State-Space Landscape.

Within this landscape, each possible state of the problem is represented and assigned a value. The objective is to either find the maximum valued state (using an objective function) 
or the minimum valued state (using a cost function). Both functions assess the value of the current state based on the optimisation criteria.

The Hill Climbing algorithm is a method to solve optimisation problems by considering direct neighboring states and selecting the state with the highest/lowest value. 
However, it has some limitations. It may get trapped in a local maximum/minimum, where all immediate neighboring states have lower/higher values, but the current state itself is 
not the optimal solution. Another limitation is the possibility of getting stuck in a flat local maximum or minimum, where all neighboring states have the same value.
'''

# Hill climbing algorithm:
# hill_climb(problem)
    # Current = initial state
    # Loop:
        # neighbour = highest valued neighbour of current
        # if neighbour is not better than currrent:
            # return current
        # current = neighbour

'''
Variants of the Hill Climbing algorithm: The Steepest-Ascent variant always chooses the highest/lowest-valued neighbor. The Stochastic variant,
selects the next state probabilistically based on certain quality of the neighbouring states. The First-Choice variant selects the first higher/lower neighbour it encounters.
To address the limitations, the Random-Restart variant conducts the search multiple times with random initial states, allowing exploration of different regions of the search space. 
Another variant called Local Beam Search chooses multiple higher-valued neighbors to avoid getting trapped in local optima/minima.
'''


'''
Simulated Annealing is an algorithm used to find the global maximum by accepting worse states with a gradually decreasing probability as the algorithm progresses. 
It takes inspiration from the annealing process in metallurgy, where materials are heated and slowly cooled to reduce defects.
'''

# simulated_annealing(problem. max):
    # current = initial state
    # for t = 1 to max:
        # T = Temperature(t)
        # neighbour = random neighbour of current
        # E = how much better neighbour is better than current
        # if E > 0:
            # current = neighbour
        # else:
            # with probability of e^(E/T) set current = neighbour    
    # return current

'''
Travelling Salesman Problem is one possible application, which aims to find the shortest path that visits all selected cities exactly once and returns to the starting city.
Each state represents a specific path, and neighbouring states are obtained by switching two pairs of connected nodes so that the nodes now point to the node of the other pair.
'''

'''
Another optimisation technique, Linear Programming, is used to minimise or maximise a linear objective function while satisfying a set of linear constraints. It is commonly applied
to problems where both the objective function and the constraints can be modeled using linear equations. For example, in a scenario where a company operates two types of machines,
Machine A and B, Linear Programming can be used to find the optimal operating levels that minimise the cost of running the machines, while ensuring sufficient supply to meet 
the company's needs. Algorithms like the Simplex method, Interior-Point methods, Revised Simplex Method, and Dual Simplex Method can be employed to solve these types of problems.
'''
