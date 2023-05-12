'''
With a clear goal state in mind, meaning the specific configuration/value of the goal is known precisely, a simple search algorithm can be used to solve the problem. However, 
if the goal state of the problem not yet clear, meaning the exact configure/value is not known, then this kind of local search problems can be defined as a State-Space Landscape.

Within the landscape, each possible state the problem can exist is represented and valued. The goal is either finding the maximum or the minimum valued 
state that the problem can exist. To find a global maximum, a objective function is used. On the other hand, to find a global minimum, a cost function is used.

Hill Climbing algorithm is a possible way to solve this problem. It will consider all neighouring states and choose the state that is the highest/lowest possible state.
Limitation are, it may get stuck in a certain state where all neighbouring states are not any higher/lower but the state itself is not the optimal solution,
that current state is called the local maxima/minima. It may also get stuck in a flat local maximum || shoulder, where all neighbouring states are of the same level. 
'''

# Hill climbing algorithm:
# hill_climb(problem)
    # Current = initial state
    # Loop:
        # neighbour = highest valued neighbour of current
        # if neighbour is not better than currrent:
            # return current
        # current = neighbor

'''
Variants of Hill Climbing: 
steepest-ascent(choose the highest/lowest neighbour), stochastic(randomly choose from higher/lower neighbours), first-choice(choose first higher/lower neighbour found),
and variants that attempt to overcome the limitations:
random-restart(conduct the search multiple times with random initial state), local beam search(chooses multiple higher valued neighbours).
'''


'''
Simulated Annealing is way to find the global maximum. It is implemented with the logic that the algorithm has
a probability of accepting worse states and the probability decreases gradually as the algorithm progresses.
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
Application of this types of local search problem can be the Travelling Salesman Problem, 
which is trying to find the shortest path to travel through all the selected cities. Each state of the problem in this case represent a path to travel through all the cities, 
and neighbouring states can be viewed as switching two pairs of connected nodes so that the nodes now point to the node of the other pair.
'''

'''
Linear Programming can be used to minimise a linear equation with some constraints. For eg. A company operates two types of machines: Machine A and Machine B. 
The company wants to find the optimal operating levels to minimize the cost of running the machines, while also ensuring that the supply is sufficient to meet the company's needs.
The cost of the machine and the constraints can all be modelled using linear equations, and algprithms like Simplex and Interior-Point can be used to solve this type of problem.
'''
