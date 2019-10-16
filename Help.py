from docplex.mp.model import Model
import numpy as np
import math
import matplotlib.pyplot as plt

depot = 1
A = 4
N = 10

C = 20
lamda = 0.1164
garma = 0.0173
r_to_degree = 180/(math.pi)
grama_new = garma*(r_to_degree)
lamda = round(lamda, 1)
garma_new = round(garma_new, 1)

cagents = [(i) for i in range(A)]
cnodes = [(j) for j in range(N)]
acnodes = [(i,j) for i in cagents for j in cnodes]
arcos=[(i,j) for i in cnodes for j in cnodes if i!=j]
double=[(i,j) for i in cnodes for j in cnodes if i!=j]
triple=[(i,j,k) for i in cnodes for j in cnodes for k in cnodes if i!=j and j!=k and i!=k]
Triple=[(a,i,j) for a in cagents for i in cnodes for j in cnodes if i!=j]
Quarter=[(a,i,j,k) for a in cagents for i in cnodes for j in cnodes for k in cnodes if i!=j and j!=k and i!=k]

random=np.random
random.seed(1)
coord_x = random.rand(N)*100
coord_y = random.rand(N)*100

#swap 7 and 1 location/coordinates to match requirement that depot is 1
temp = 0
temp = coord_x[7]
coord_x[7] = coord_x[1]
coord_x[1] = temp
temp = coord_y[7]
coord_y[7] = coord_y[1]
coord_y[1] = temp
# end
distance={(m,n): lamda*np.hypot(coord_x[m]-coord)x[n], coord_y[m]-coord_y[n]) for m,n in double}

angle={(o,p,q): 0 for o,p,q in triple}
for o,p,q in triple:
    angle[(o,p,q)]=math.pi-np.arccos(round((distance[(o,p)]**2+distance[(p,q)]**2-distance[(o,q)]**2)/(2*distance[(o,p)]*distance[(p,q)]),2))

mdl=Model('EECPP')
x=mdl.binary_var_dict(Triple, name='x')
I=mdl.binary_var_dict(Quarter,name='I')
d=mdl.continuous_var_dict(acnodes,name='d')

#(1)
mdl.minimize(mdl.sum((x[(a,i,j)]*distance[(i,j)]) for a,i,j in Triple)+mdl.sum((anlge[(i,j,k)]*I[(a,i,j,k)]) for a,i,j,k in Quarter))

for n in cnodes:
    if n!=depot:
        mdl.add_constraint(mdl.sum(x[(a,i,j)] for a,i,j in Triple if j==n)==1, ctname='in_%d'%n) #(2)
    if n==depot:
        mdl.add_constraint(mdl.sum(x[(a,i,j)] for a,i,j in Triple if j==n)<=A, ctname='in_%d'%n) #(3)
#(4)
for n in cnodes:
    if n!=depot:
        mdl.add_constraint(mdl.sum(x[(a,i,j)] for a,i,j in Triple if i==n)==1, ctname='out_%d'%n)
    if n==depot:
        mdl.add_constraint(mdl.sum(x[(a,i,j)] for a,i,j in Triple if i==n)>=1, ctname='out_%d'%n) #(5)
        mdl.add_constraint(mdl.sum(x[(a,i,j)] for a,i,j in Triple if i==n)==A, ctname='out_%d'%n) #(6)

#(7)
for m in cagents:
    for n in cnodes:
        mdl.add_constraint(mdl.sum(x[(a,i,j)] for a,i,j in Triple if a==m and j==n)==mdl.sum(x[(a,j,k)] for a,j,k in Triple if a==m and \
        j==n), ctname='arrive and leave the same depot')

for m in cagents:
    for n in cnodes:
        mdl.add_constraint(mdl.sum(x[(a,i,j)] for a,i,j in Triple if a==m and i==1)==mdl.sum(x[(a,j,k)] for a,j,k in Triple if a==m and \
        k==1), ctname='leave and arrive at depot')

#(8)
for m,i,j,k in Quarter:
    mdl.add_constraint(I[(m,i,j,k)]>=x[(m,i,j)]+x[(m,j,k)]-1,ctname='Agent%d'%m)

#(9) and #(10)
for m,i,j,k in Quarter:
    mdl.add_constraint(I[(m,i,j,k)]<=x[(m,i,j)],ctname='Agent_%d_ij'%m)
    mdl.add_constraint(I[(m,i,j,k)]<=x[(m,j,k)],ctname='Agent_%d_jk'%m)

#(11)
for m in cagents:
    mdl.add_constraint((mdl.sum((x[(a,i,j)]*distance[(i,j)]) for a,i,j in Triple if a==m) + mdl.sum((angle[(i,j,k)]*I[(a,i,j,k)]) \
    for a,i,j,k in Quarter if a==m))<=C)
#(12)
for m in cagents:
    for i,j in arcos:
        if j!=depot:
            mdl.add_indicator(x[(m,i,j)], d[(m,i)]+1==d[(m,j)],name='order_(%d, %d, _%d)'%(m,i,j))

solution=mdl.solve(log_output=True)

m=coord_x
n=coord_y

s=[]
for n in range(len(coord_x)):
    s_temp=[]
    s_temp.append("%.1f"%coord_x[n])
    s_temp.append("%.1f"%coord_y[n])
    s.append(s_temp)

arcos_activos=[i for i in Triple if x[i].solution_value>0.9]

plt.figure(figsize=(10, 7.5))
plt.xlabel("Distance X")
plt.ylabel("Distance Y")
plt.title("Solution EECPP")

for n in cnodes:
    if n!=depot:
        plt.scatter(x=coord_x[n], y=coord_y[n], color='blue', zorder=1)
    else:
        plt.scatter(x=coord_x[n], y=coord_y[n], marker='s', linewidths = 40, color='green', zorder=1)

for a,i,j in arcos_activos:
    if a==0:
        plt.plot([coord_x[i],coord_x[j]],[coord_y[i],coord_y[j]], color='blue',zorder=1)
    if a==1:
        plt.plot([coord_x[i],coord_x[j]],[coord_y[i],coord_y[j]],color='red',zorder=2)
    if a==2:
        plt.plot([coord_x[i],coord_x[j]],[coord_y[i],coord_y[j]],color='black',zorder=3)
    if a==3:
        plt.plot([coord_x[i],coord_x[j]],[coord_y[i],coord_y[j]],color='green',zorder=4)

for n in range(len(coord_x)):# coordinates of node
    plt.annotate(str(s[n]), xy=(coord_x[n],coord_y[n],xytext=(coord_x[n]-0.1, coord_y[n]-0.2), color='purple')

for n in range(len(coord_x)):
    plt.annotate(str(n), xy=(coord_x[n],coord_y[n]), xytext=(coord_x[n]+0.05, coord_y[n]+2.1, color='red')

plt.grid(True)
plt.savefig("1_drone.png")
plt.savefig("1_drone.eps")
plt.show
