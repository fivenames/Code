'''
Constraint Satisfaction Problem (CSP) consists of a set of variables, each associated with a domain of possible values, and a set of constraints. Unary constraints involve a single 
variable and restrict its domain based on specific conditions. For example, the unary constraint 'A != 1' indicates that variable A cannot take on the value 1. Binary constraints, 
on the other hand, involve pairs of variables and establish relationships or restrictions between them. An example of a binary constraint is 'A != B,' which indicates that variables 
A and B cannot have the same value simultaneously. To ensure consistency in CSPs, we can make the variables node consistent or arc consistent. Node consistency involves ensuring each 
variable's domain satisfies its unary constraints. Arc consistency involves ensuring every binary constraint between two variables, the values in their domains satisfy the constraint.

A common representation of a CSP is a Constraint Graph, where each node in the graph represents a variable, and edges(connectives) represent constraints between variables. 
This graph helps visualize the relationships between variables and constraints, aiding in problem-solving and constraint propagation.
'''

# function will return True if domain for variable X is modified, False otherwise.
# revised(problem, X, Y):
    # revised = False
    # for x in X.domain:
        # if no y in Y.domain satisfies the constraint for (X, Y):
            # delete x from X.domain
            # revised = True
    # return revised

# function will return True if achieved arc consistency, False otherwise. 
# Note, everytime a domain is deleted, the function need to check again if the revised domain will still satisfy all the neighbouring variables' Binary constraints.
# AC-3(problem):
    # queue = all edges
    # while queue != None:
        # (X, Y) = DEQEUE(queue)
        # if revised(problem, X, Y):
            # if X.domain == 0:
                # return False
            # for each Z in X.neighbours - {Y}:
                # ENQUEUE(queue, (Z, X))
    # return True

'''
The AC-3 algorithm enforces arc consistency between two nodes by examining their binary constraints. However, it only considers two neighboring nodes at a time and may not establish
arc consistency across the entire graph.For example, if variables A and B have the constraint A != B, AC-3 can identify and remove inconsistent values between A and B. However, if 
there is a variable C with the constraint C != A, AC-3 does not consider all three variables together, and nothing is changed.
AC-3 can be helpful in reducing the domains of variables and simplifying the problem.

Since the problem is represented as a graph, a simple search algorithm, specifically a depth-first search, can be used to solve the problem.
initial state: empty assignment(frontier), where each variable is unassigned and can take any value from its domain. 
actions: add a {variable = value} to the assignment, meaning adding a variable-value assignment to the assignment set.
transition model: shows the updated state after each assignment
goal test: checks if all variables are assigned and if all constraints are satisfied
path cost: not applicable as all paths have the same cost, and path taken is not of interest.

However, using a simple search algorithm can be very inefficient due to the large number of assignments and constraint checks involved.
To address this, the Backtracking Search algorithm is employed. It leverages the characteristic of the problem where the sequence of variable assignments does not matter.
By taking advantage of the stack frame and recursive calls, the algorithm can efficiently explore the search space.

The Backtracking Search algorithm recursively calls itself, and if a stack frame returns failure, it indicates that the current assignment will eventually lead to a failure
down the line. This prompts the algorithm to backtrack, undo the current assignment, and explore alternative possibilities. This process continues until either a complete assignment
is reached, in which case the algorithm returns the assignment as the solution, or if no possible solution is found, the algorithm returns failure as the final result.
'''

# backtrack(assignment, problem):
    # if assignment complete:
        # return assignment
    
    # var = select_unassigned_var(assignment, problem) ----- selection sequence of nodes does not matter
    # for value in domain_values(var, assignment, problem):
        # if value consistent with assignment:
            # add {var = value} to assignment
            # result = backtrack(assignment, problem) ----- recursively call the function to check if down the road does adding this value to the frontier causes inconsistency.
            # if result != failure
                # return result ----- returned by the stackframe, it's either a failure or the successful assignment returned by the top frame, which will propagate down the frames.
            # remove {var = value} from assignment
    # return failure

'''
To further optimize the constraint satisfaction problem-solving process, additional techniques can be applied. One approach is to leverage inference with existing knowledge to 
maintain arc consistency. After assigning a value to a variable, enforcement of arc consistency can be performed on its neighboring variables. This inference step, using techniques
like AC-3 algorithm, propagates constraints and narrows down the domains of neighboring variables. By reducing the search space, this technique can lead to more efficient exploration.

In addition to inference, the selection of variables and domain values can be optimized using heuristics. Variable selection heuristics, such as Minimum Remaining Values (MRV) 
and Degree Heuristic, help in choosing the most promising variables. MRV selects the variable with the smallest domain, allowing for early pruning of the search space. 
Degree Heuristic selects the variable with the highest degree, indicating it has the most constraints, which can quickly restrict the domain values for its neighbors.

Similarly, selecting domain values can be optimized using heuristics such as the Least-Constraining Values (LCV) heuristic. LCV prioritizes values that minimize the impact 
on neighboring variables. By selecting values that rule out fewer options for neighboring variables, LCV increases search flexibility and improves the chances of finding a solution.

The selection of domain value heuristic and selecting variable heuristics can present a conflict due to their different goals and impacts on the search process. 
When choosing variables, the aim is to limit the search space by assigning values to variables and moving towards a solution. This process is driven by the fact 
that all variables must be assigned, and there can be multiple valid solutions. The selection of variable heuristics helps in efficiently narrowing down the search space.
On the other hand, selecting domain values has a different objective. It aims to keep the choice open and increase the chances of finding a solution by not immediately assigning 
values that might restrict the search. Unlike variables, not all values need to be assigned to a variable, and leaving out certain values can enhance search efficiency. 
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