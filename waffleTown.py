# This file i hope to fininsh dual-ride problem using cplex
# by the end of today

from docplex.mp.model import Model
import numpy as np
import math

N = 6
depot = 0
destination = 5
requests = 2
test = math.inf
distance = [[test,2,3,test,test,test],
            [test,test,4,5,4,test],
            [test,2,test,6,2,test],
            [test,test,6,test,3,4],
            [test,2,test,9,test,7],
            [test,test,test,test,test,test]]
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
# I hope to get an idea durimg my study at UB preparing homework 8 for the coming Monday by glaring cplex at the desktop
# !!
# I only need to refer #1 #2 #3 #4 in Do.py. And if I want to be better, maybe also the late part of drawing the figure.
# One question: how to define the time when agent arrive a node, the time should be bigger one of arriving time and left visiting time
# why not have a test first? i hope to have an idea of this project
# I need to switch to windows because i don't have cplex in Mac
