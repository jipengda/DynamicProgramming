# This file i hope to fininsh dual-ride problem using cplex
# by the end of today

from docplex.mp.model import Model
import numpy as np
import math

N = 6
depot = 0
destination = 5
requests = 2
distance = [[0,2,3,0,0,0],
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
cnodes = [(j) for j in range(N)]
arcos = [(i,j) for i in cnodes for j in cnodes if i!=j]
mdl = Model('Dual_ride')
x = mdl.binary_var_dict(arcos, name = 'x')
# Here I wonder if I should use one-element valriables to judge if
# one node is visited or not
mdl.minimize(mdl.sum( (x[(i,j)] * distance[(i,j)]) for i,j in arcos ))
# all nodes need being visited
for n in cnodes:
    mdl.add_constraint(mdl.sum(x[(i,j)] for i,j in arcos if j==n)==1,ctname='in_%d'%n)# I have doubt about this

# pick up nodes must be first visited before next node
for i,j in arcos:
    mdl.add_indicator(x[(i,j)], x[(i,j-requests)]==1, name='order_(%d,%d)'%(i,j))

# time window constraint must be followed, arriving a new node
# should not be later than upper bound
for i in cnodes:
    mdl.add_constraint(time[i] <= timeInfor[i][1], name='time') # I have question about time[i]

# reach and leave the same node
for n in cnodes:
    mdl.add_constraint(mdl.sum(x[(i,j)] for i,j in arcos j==n)==mdl.sum(x[(j,k)] for j,k in arcos if j==n), \
    ctname='arrive and leave the same depot')
