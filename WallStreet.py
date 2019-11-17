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

# i hope to define the constraints first
# probabaly I can get some idea from do.py
# after sketching do.py, i think it is better to define a map first

from docplex.mp.model import Model
import numpy as np
import math
# import matplotlib.pyplot as plt
# currently I don't need to draw a graph

N = 6 # node 0, node 1, node 2, node 3, node 4 and node 5
# node 0 is depot , node 5 is destination, node 1 and node 2 are pick up nodes
# But how to define the relationship between two nodes
# Can use a distance function or matrix
depot = 0
requests = 2
destination = 5
distance =  [[0,2,3,0,0,0],
             [0,0,4,5,4,0],
             [0,2,0,6,2,0],
             [0,0,6,0,3,4],
             [0,2,0,9,0,7],
             [0,0,0,0,0,0]]
timeInfor = [[0,30],
             [6,14],
             [12,17],
             [11,21],
             [12,22],
             [0,30]]

cnodes=[(j) for j in range(N)]
arcos = [(i,j) for i in cnodes for j in cnodes if i!=j]
# after this, i need create decision variables for which arc to follow during the path
mdl = Model('Dual_ride')
x = mdl.binary_var_dict(arcos, name = 'x')
# i should creat a model
mdl.minimize(mdl.sum((x[(i,j)]*distance[(i,j)]) for i,j in arcos))

# what about the constraints?
# constraint 1 all notes need being visited

for n in cnodes:
    mdl.add_constraint(mdl.sum(x[(i,j)] for i,j in arcos if j==n)==1,ctname='in_%d'%n) #(1) constraint

# constraint 2 pick up constraint must be respected

for i,j in arcos:
    mdl.add_indicator(x[(i,j)],x[(i,j-requests)]==1,name='order_(%d, %d,%d)'%(m,i,j)) #(2) constraint

# constraint 3 time window constraint must be followed
# Before this, I need to add timeInfor in the main function
for i in cnodes:
    mdl.add_constraint(time[i] <= timeInfor[i][1], name='time') #(3) constraint
# I always think constraint 3 is difficult to convert to cplex language
# I need help
# The reason I set constraint is to limit x variables

# reach and leave the same noded

# I hope to review those three constraints and make necessary changes to make it work
for n in cnodes:
    mdl.add_constraint(mdl.sum(x[(i,j)] for i,j in arcos j==n)==mdl.sum(x[(j,k)] for j,k in arcos if j==n), \
    ctname='arrive and leave the same depot')
