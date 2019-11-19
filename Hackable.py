# In this file, I hope to solve time constraint problem

timeInfor = [[0,30],
             [6,14],
             [12,17],
             [11,21],
             [12,22],
             [0,30]]

for i in nodes:
    mdl.add_constraint(mdl.sum() <= timeInfor[i][1])


# Jamie said, it's just another if statement(well really big M but since CPLEX can now handle if instead of big M)
# However, it well not explain how to deal with the wait time
# Why not try max function
labelInforTime = max(labelInforTime, timeInfor[node][0])

# Maybe I can calculate out all possible path routes cost. And use a if statement to get


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

solution = mdl.solve(log_output=True)
#
