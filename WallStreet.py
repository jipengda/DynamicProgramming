# In this file, i hope to finish editing script using Cplex to
# implement the figure from paper
# and compare implement using dynamic programming with regards to time
# see who is better(or who is weaker)

# cplex needs objective, needs constraints
# objective: minimum time or minimum cost
# constraints possible:
# 1: visited constraints, new node must not have been visited
# 2: pick up nodes constriants, before new node has been vistied, pick up nodes must be visited
# 3: time window constraint, new node visting must respect time window constraint
# 
