# the departure node 0

depot = 0

n=10
N = 2*n + 1
# first iteration k=1:
#    generate states made up of routes visiting a single node from among the origins
for iteration in range(N):
    if iteration == 1:
        generate states;


# each subsequent iteration k(1<k<2n+1):
    if iteration > 1 and iteration<= N:
#    the states are constructed from the states of previous iteration and are made up of
#    routes visiting one additional node from among the origins and destinations
        construct states(one additional node)

# last iteration k=2n+1:
    if iteration == 2 and iteration<= N:
#    the vehicle must go to the arrival node 2n+1
        vehicle go to the arrival node

# iteration k(1, 2n+1) define a state(S, i)
    if iteration >= 1 and iteration <= 2*n + 1:
        define a state(S, i)

# start at node 0
depot = 0
# exists a feasible route visits all the nodes in S belongs to set {1,...,2n}
    a feasible route
# and terminals at node i belongs to S
    if(terminals belongs to S):
        return True
# S is a non-ordered set of cardinality K
S = non-ordered set of cardinality
# two cases:
# state(S,i) is ante-feasible: ending with node i, exists an order of visiting
# state(S,i) is post-feasible: begining with node i
def ante-feasbible():
    ending_node = 1
    an_order_visiting = 1
def post_feasbile():
    begining_node = 1
    an_order_visiting = 1

# (S, i) means there are several routes from node 0 to node i
# (S, i) in each state only some of the labels are stored
# eliminate a label: if it cannot be part of the minimum cost route from 0 to 2n + 1, using the following optimality principle
# eliminate for state (S,i): the label(t', z') is eliminated if there exists another label with both a lesser time and a lesser constructed
# the labels are placed in a list with times in strictly increasing order
assert (S,i) state which there are several routes from node 0 to node i
assert (S,i) state in which only some of the labels are stored
if (a label cannot be part of the minimum cost route):
    eliminate label
if(there exists another label with both a lesser time and a lesser constructed):
    eliminate for state a label
if(labels are placed in a list with times in strictly increasing order):
    eliminate a label
# The first iteration is carried out by visiting the origins from node 0 resulting in the set of states
# At subsequent iterations new states by adding one node to the toal visited at the preceding iteration
# At the final iteration, there is only one state. All nodes have been visited from the departure point to the arrival point
# The minimum value of the objective function is given in the label with the smallest cost, i.e., the last in the list. If this set is non-empty.
# If the set is empty, the problem is infeasible; this can be detected at any given iteration if no labels are created.
if(iteration == 1):
    resulting in the set of states which visite the origins from node 0
if(iteration>1 and iteration<2*n+1):
    add_one_node()
if(iteration==2*n+1):
    finish_visite_nodes()
judge(set)
    if(set is empty):
        the problem is feasible
    elif(set is non empty):
        the problem is infeasible
# When node j is to be added for a state(S,i)
# to simplify the execution of the tests, information on the states is stored in a three level structure.
def add_one_node():
    information_stored()

# first level: we have set S and its load y(s)
# second level: for S, we have the terminal nodes i used to form (S,i)
# third level: the reduced set of labels H(S,i) is stored for (S,i)
def first_level():
    set {value for value in variable}
    load y(s)
def second_level():
    manage_to_get(teriminal nodes)
def third_level():
    the reduced set is information_stored

# Elimination criteria
# 1: node j must not have been previously visited: j belongs to S/
# 2: if j is a destination, then the origin node j-n must have been previously visited: if j belongs to {n+1, ..., 2n} then j-n belongs to {value for value in variable}
# 3: if j is an origin, vehicle capacity constraints must be respected
# 4: time tj = Aj is the earliest time at which node j can be visited, it must be possible to visit each subsequent unvisited node
# l belongs to S U {j}\ while respecting the time constraint:
#   Aj + Mj + Tjl < Bl, for all l belongs to S U {j} \
# For all unvisited nodes, criterion #4 is not tested. The test is carried out for the most likely candidate nodes to be unvisited
# next at iteration k + 1, only the unvisited nodes ranked from k-2 to k+4 are tested. If one of these nodes cannot be visited after j
# then state (S U {j},j) is rejected
def elimination_criteria():
    is_node j_visited = False
    if(j is a destination):
        origin_node_been_visited = True
    if(j is an origin):
        vechicle_capacity_constraints_respected = True

# Another way of four criterias stated formally below are based on:
# 1 the time of the visit to node j
# 2 the time of visit to a node subsequent to node j
# 3 visits to two destinations whose origins are already visited, following the visit to node j
# 4 visits to two new origins following node j
# 5 time constraint must be respected: t1 + M1 + tij < Bj
# I discard three following criteria because currently they are not related to my project. (311, #6 #7 #8)
# 3.3 Elimination criteria in the case with several clients at the same solution. I don't consider this because I do one-agent case now.
def elimination_criteria_2():
    def ti the time of the visit to node j
    def tx the time of visit to a node subsequent to node j
    def vi visits to two destinations whose origins are already visited, following the visit to node j
    def vj visits to two new origins following node j
    def criteria 5 t1 + M1+ tij < Bj
