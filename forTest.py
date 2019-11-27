# data based on Figure 2:Numerical Example.
def forTest_criterion():
    requestNumbers = 2
    n = requestNumbers
    origin = range(1, n +1)
    Nodes = range(1, 2*n + 1)
    NodesAndDeparture = range(0, 2*n + 1)
    NodesAndArrival = range(1, 2*n + 1 + 1)
    NodesAndDepots = range(0, 2*n + 1 + 1)
    S=[0,2,1] # A good example matches optimal route
    NodeToAdd = 3
    j=NodeToAdd
    CapacityLimit=2
    unvisited_orgins=[]
    AllNodes = range(0, 2*n + 1 +1)
    C=[0,1,1,-1,-1,0]
    y_S = 0
    for i in S:
        y_S = y_S + C[i]

    A=[0, 6, 12, 11, 12, 0]# the lower bounds of the time window at the nodes 0~2n+1
    B=[30, 14, 17, 21, 22, 30]# the upper bounds of the time window at the nodes 0~2n+1
    M=[0, 0, 0, 0, 0, 0]# the time required to handle pick-up at node i
    T=[[0, 2, 3, N, N, N], # N represents for no way, or a very big travel time cost
       [N, 0, 4, 5, 4, N], # 0 is from node to node itself
       [N, 2, 0, 6, 2, N],
       [N, N, 6, 0, 3, 4],
       [N, 2, N, 9, 0, 7],
       [N, N, N, N, N, 0]]# the travel time between nodes i and j

    D=[[0, 2, 3, N, N, N],
       [N, 0, 4, 5, 4, N],
       [N, 2, 0, 6, 2, N],
       [N, N, 6, 0, 3, 4],
       [N, 2, N, 9, 0, 7],
       [N, N, N, N, N, 0]] # the distance traveled between nodes i and j

    memory = S
    length = len(memory)
    time = A[0]
    for i in range(length-1):
        m=memory[i]
        n=memory[i+1]
        time=time+T[m][n]
        time=max(time,A[n])
        t_j= time + T[n][j]
        t_j= max(t_j, A[j])# t_j is that node j is visited at time t_j
    #3
    if (j in origin):
        if y_S + C[j] > CapacityLimit: # Convert to python syntax
            return False
        #6
    complete_set = [i for i in range(NodesAndDepots)]
    SAndj=S+j
    subset_of_SAndj = complete_set - SAndj
    for l in subset_of_SAndj:
        if t[j] + M[j] + T[j][l] > B[l]: # Convert to pyhton syntax
            return False
    #7
    #all pairs of destination n+l1 and n+l2 whose origins l1 and l2 have been previously visited while respecting the time constraints
    #while respecting the time constraints
    #with two visiting permutations for n+l1 and n+l2,we must satisfy
    for l1 in set(S and {j}):
        for l2 in set(S and {j}):
            if n+l1 not in subset_of_SAndj:
                if n+l2 not in subset_of_SAndj:
                    if max(A[n+l1], t[j]+M[j]+T[j][n+l1]) + M[n+l1] + T[n+l1][n+l2] > B[n+l2]:
                        return False
                    elif max(A[n+l2], t[j]+M[j]+T[j][n+l2]) + M[n+l2] + T[n+l2][n+l1] > B[n+l1]:
                        return False
#8
#if node j is visited at time tj, it must be possible to visit all pairs of unvisited origins l1 and l2 while
#respecting the time constraints
# tested for only one pair(l1, l2)
# The origins are preordered in non-decreasing order of their upper bounds
# the two first unvisited origins are chosen
    visited_origins = []
    for node in S:
        if node in origins:
            visited_origins.append(node)
        unvisited_origins = orignis - visited_origins
        for l1 in unvisited_origins:
            for l2 in unvisited_origins:
                if max(A[l1], t[j] + M[j] + T[j][l1]) + M[l1] + T[l1][l2] > B[l2]:
                    return False
                elif max(A[l2], t[j]+M[j]+T[j][l2]) + M[l2] + T[l2][l1] > B[l1]:
                    return False
#6(and the same applies to criterion #8)
#cannot be improved by also considering the destination corresponding to the unvisited origin
#we would then have to satisfy:
#But the time intervals are always defined so that Bn+l >= Bl + M[l]+T[l][n+l]
#This is a condition on the input data.Given this condiation, the feasibility check for the destination follows from
#the check for the origin
#for l in set(S and {j}): #SAndj equals to S and {j}
    for l in SAndj:
        for n+l in SAndj:
            if max(A[j], t[j]+M[j]+T[j][l]) + M[l] + T[l][n+l] > B[n+l]:
                return False

#9 elimination criterion in the case with several clients at the same location
# criterion #9, tested after criterion #5, was developed to limit the proliferation of states when i and j represent the same physical
# location
#t is the arrival time at this location
# Let i and j be the two nodes at the same location with time windows[Ai, Bi] and [Aj, Bj] and handling times Mi and Mj(travel times are zero).
# The state (S,i) or (S,j) retained is the one which has the earliest finishing time at that physical location
# If t is the arrival time at this location, the state(S,j) is retained(i.e. the order i+j is imposed)
#for i in set(S):
#convert to python syntax
    for i in S:
        if max(A[j], max(A[i],t)+M[i]) + M[j] > max(A[i], max(A[j],t) + M[j]) + M[i]:
            return False

if __name__ == '__main__':

    forTest_criterion()
