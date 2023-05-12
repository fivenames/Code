'''
Constraint Satisfaction problem, which contains a set of variable with its set of domain of values it can take on, and a set of constraints.
Unary constraint is the constraints that involves only a single variable, for eg. A != 1  On the other hand, Binary constraint involves two variables, for example A != B
To make the variables node consistent(satisfy Unary constraints) or to make the variables arc consistent(satisfy Binary constraint),
remove elements from the set of of domain for the variables that does not satisfy the constraints.

The problem to be represented as a graph, with each node representing a variable, and if between two nodes there is a constraint, they are connected as neighbours.
'''

# function will return True if domain for X is modified, False otherwise.
# revised(problem, X, Y):
    # revised = False
    # for x in X.domain:
        # if no y in Y.domain satisfies constraint for (X, Y):
            # delete x from X.domain
            # revised = True
    # return revised

# function will return True if achieved arc consistency, False otherwise. 
# Note, everytime a domain is deleted, the function need to check again if the revised domain will still satisfy all the neighbouring variables' Binary constraints.
# AC-3(problem):
    # queue = all constraints
    # while queue != None:
        # (X, Y) = DEQEUE(queue)
        # if revised(problem, X, Y):
            # if X.domain == 0:
                # return False
            # for each Z in X.neighbours - {Y}:
                # ENQUEUE(queue, (Z, X))
    # return True

'''
AC-3 algorithm might not solve the problem directly as it can only enforce arc consistency between two nodes by only consider two neighbouring nodes at a time, not the entire graph.
For eg. if there is multiple possible values for A and B and the constraint is A != B. A can always take on a different value from B, but if there is another variable C 
with constraint C != A, it is not considered together with A and B, hence nothing is changed. However, it can somethimes help in reducing the domain to simplify the problem.

Since the problem is represented as a graph, a simple search algorithm can actually be used to solve the problem, as such:

initial state: empty assignment(frontier), for which assignment is to assign any variable to any possible value
actions: add a {variable = value} to the assignment, meaning assign a variable one of its domain value.
transition model: shows the new frontier after the current action
goal test: check is all variables assigned, and the constraints are all satisfied
path cost: not applicable as all paths have the same cost, and path taken is not of interest.


However, this will be very inefficient since there can be many assigments to be done and constraints to be checked. For this search problem, the sequence of action is not important
as the sequence of assigning variables its values does not matter. Hence leveraging this characteristic, Backtracking Search algorithm can be used to efficiently solve this problem.

This algorithm takes the advantage of the stackframe, by recursively calling itself. If the stackframe above returns a failure,
meaning the current assignment will result in failure in the future, the stackframe breaks and re-assign the current value.
This process will then repeat until the very top of the stack frame when all assignment is complete, the function then returns the assignment, or,
if no possible way is found, the function returns failure as final result.
'''

# backtrack(assignment, problem):
    # if assignment complete:
        # return assignment
    
    # var = select_unassigned_var(assignment, problem)
    # for value in domain_values(var, assignment, problem):
        # if value consistent with assignment:
            # add {var = value} to assignment
            # result = backtrack(assignment, problem) ----- recursively call the function to check if down the road does adding this value to the frontier causes inconsistency.
            # if result != failure
                # return result ----- returned by the stackframe, if it's failure, it will pass down the frames. However, it can be the assignment returned by the top frame as well.
            # remove {var = value} from assignment
    # return failure

'''
To optimise the algorithm further, using inference with existing knowledge. Every assignment to a new variable its value, enforcement on arc consistency can be carried out on its 
neighbours. This is, with the existing knowledge of current variable's assignment, infer what can be assigned to the neighbouring variables by considering their constraints.
To do this - maintain arc consistency, after a new assignment, call AC-3 function with a queue of all constraints that are neighbors of the current assigned variables.

Optimising selection of variables instead of select_unassigned_var(), heuristic such as Minimum Remaining Values(select the variable with the smallest domain) and
Degree Heuristic(select the variable that has the highest degree - number of nodes connected to it) can be used.
During the initialising state, Degree Heuristic can be very useful as starting with highest degree node will quickly restrict(or makes clear) the domain values for neighbours.
This will free up search space to allow quicker search through of the graph, as well as during the intermediate states, using
Minimum Remaining Values can be very helpful as assigning the node with smallest domain will allow the search to explore other nodes faster.

Optimising selection of domain values instead of domain_values() which returns the values in sequence. Selecting the values with higher chance to be correct will result
in faster execution of the code. Heuristics such as the Least-Constraining Values Heuristic(returns the option that does not rule out the neighbouring variables),
using this heuristics, this leaves out higher possibility of finding a solution after moving on. This is conflicted with choosing variables because when chossing variables,
it is an attempt to free up search space since all variables have to be assigned and there can exist multiple solutions. As for choosing values, not all values need to be assigned 
to a variable, hence leaving out a higher chance of finding a solution will increase the search efficiency.
'''

# backtrack(assignment, problem):
    # ......
            # add {var = value} to assignment
            
            # inferences = infer(assignment, problem) ----- the inferred assignments of values to neighbouring variables
            # if inferences != failure:
                # add inferences to assignment
            
            # result = backtrack(assignment, problem)
    # ......
            # remove {var = value} and inferences from assignment
    # ...