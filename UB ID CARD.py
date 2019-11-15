# This file is hopefully to finish turing cost consideration so that one agent EECPP problem
# can be implemented.
# I wonder if I have time to change all frame, as EECPP does not have time constraint.

import numpy as np
lamda = 1
    # where should I add it?
    # So we don't need sets as xingcan
    def turingCost(set1, dic_angle):#Before, this I need to calculate the cost (including turing cost),too
        # I first take the last three nodes of set1 as new set
        view = len(set1)
        tool = view - 1
        lastThree = set1[tool-3:tool]
        # Then we get the last three nodes of set1, to get turning cost
        # Or use this way
        fir = lastThree[0] # index first
        sec = lastThree[1] # index second
        thi = lastThree[2] # index third
        # turningCost= dic_anagle[(lastThree[0],lastThree[1],lastThree[2])]# I am not sure abouth the format, goold first
        turningCost= dic_angle[(fir, sec, thi)]
        # What if fir, sec, thi is not found in the dictionary?
    return turningCost

    def list_all_sets(graph, timeInfor, requests, iteration):
        source=[0]
        sets=[]
        row = source[-1]
        node = -1
        labelNumber=0
        labelInforTime=0
        labelInforCost=0
        turningCost = 0
        for i in graph[row]:
            labelInforTime=0
            labelInforCost=0
            set1 = source
            node = node + 1
            if(i != 0):
                set1 = source + [node]
                labelNumber = labelNumber + 1
                labelInforTime = labelInforTime + i
                labelInforCost = labelInforCost + i
                labelInforTime = max(labelInforTime, timeInfor[node][0])
                set1 = set1+[[labelInforTime, labelInforCost]]
                sets.append(set1)
                print("label number:", labelNumber)
                print(set1)
        for j in range(iteration-1):
                sets_copy = sets
                sets=[]
                for source in sets_copy:
                    row = source[-2] #-2 is last visiting node, -1 is time and cost infor
                    node = -1
                    lastElement = source.pop() # If there is problem in the future, it must be here!
                    set1 = source
                    # I probably add initiallize turning cost Here
                    turningCost = 0
                    for i in graph[row]:
                        labelInforTime = 0
                        labelInforCost = 0
                        turningCost = 0
                        node = node + 1
                        if(i != 0):
                            set1 = source + [node]
                            trueTableValue = criterion(graph, timeInfor, source, set1, node, requests)
                            # If trueTableValue is 1(True), means set1 as new set is valid
                            # If trueTableValue is 0(False), means sets as new set is invalid
                            if(node == iteration and j != iteration-2):
                                trueTableValue = False
                            if trueTableValue is True:
                                memory = set1
                                length = len(memory)
                                labelInforTime = timeInfor[0][0]
                                for k in range(length-1):
                                    m = memory[k]
                                    n = memory[k+1]
                                    labelInforTime = labelInforTime + graph[m][n]
                                    labelInforCost = labelInforCost + graph[m][n]
                                    labelInforTime = max(labelInforTime , timeInfor[n][0])


                                turningCost = turningCost + turningCost(set1, dic_angle)
                                labelInforCost = labelInforCost + turningCost
                                set1 = set1+[[labelInforTime, labelInforCost]]
                                delete_flag = compare(sets,set1)
                                # delete_flag value has three states generally
                                # -1: set1 is invalid
                                # -2: set1 is valid, should be added
                                # other: set1 is valid(should be added) and it kicks out an old one in the sets which has no advantage of time or cost
                                if(delete_flag == -1):
                                    pass
                                elif(delete_flag==-2):
                                    sets.append(set1)
                                else:
                                    del sets[delete_flag]
                                    sets.append(set1)
                # Here, at this iteration, sets are finally determined(all set in the sets are rightly added or kicked out)
                for print_set in sets:
                    labelNumber = labelNumber + 1
                    print("label number:", labelNumber)
                    print(print_set)
        return sets

# compare function returns delete_flag, which relates to if an old set should be kicked out by set1 as the new set
# delete_flag value has three states generally
# -1: set1 is invalid
# -2: set1 is valid, should be added. And -2 is default value.
# other: set1 is valid(should be added) and it kicks out an old one in the sets which has no advantage of time or cost
# I wonder if I give a new name to this function, fellow_lables or something else?compare is a good idea for name
def compare(sets, new_one):
    View = len(new_one)
    Tool = View-1
    new_one_nodes = new_one[0:Tool]
    new_one_time = new_one[-1][0]
    new_one_cost = new_one[-1][1]
    length = len(sets)
    delete_flag = -2
    # Here, every set has format like [node x1, node x2, node x3, node x4, node x5, [time, cost]]

    # time compare
    for i in range(length):
        compare=sets[i]
        compare_time=compare[-1][0]
        compare_cost=compare[-1][1]
        if (new_one_time == compare_time):
            if(new_one_cost > compare_cost):
                delete_flag=-1
                return delete_flag

    # if time is equal, compare the cost, if it has more cost, delete flag = 1, default delete flag=0, means does not delete
    # cost compare
    for i in range(length):
        compare=sets[i]
        compare_time=compare[-1][0]
        compare_cost=compare[-1][1]
        if (new_one_cost == compare_cost):
            if(new_one_time > compare_time):
                delete_flag=-1
                return delete_flag

    # see if new_one can kick some old one. If so, record index of old one
    # However, this operation should be very careful becaue it matters!!
    for i in range(length):
        compare=sets[i]
        View=len(compare)
        Tool=View-1
        compare_nodes=compare[0:Tool]
        compare_time=compare[-1][0]
        compare_cost=compare[-1][1] # The same way as new_one to get necessary infor of compare_one
        if(new_one_cost<=compare_cost):
            if(new_one_time<=compare_time):
                if( set(new_one_nodes ) == set(compare_nodes) ):
                    delete_flag = i # it means ith label can be kicked out by new_label
                    return delete_flag
    return delete_flag

def criterion(graph, timeInfor, source, set1, node, requests):
    trueTableValue = True
    if node in source: # criterion #1, new node should not have been visited
        trueTableValue = False
        return trueTableValue
    if node-requests not in source and node >= requests: # criterion #2, pick up node should have been visited before new node
        trueTableValue = False
        return trueTableValue
    memory=set1
    length=len(memory)
    time = timeInfor[0][0]
    for i in range(length-1):
        m=memory[i]
        n=memory[i+1]
        time = time + graph[m][n]
        time = max(time, timeInfor[n][0])
    if(time>timeInfor[node][1]): # criterion #5, time window constraint must be respected
        trueTableValue = False
        return trueTableValue
    else:
        time=max(time, timeInfor[node][0])
        m=node
        set1=set(memory)
        cp_set=set([0,1,2,3,4,5]) # This needs to change when map information is changed. IMPORTANT!
        Jipeng = cp_set - set1
        for n in Jipeng:
            Github= time+graph[m][n]
            if(Github>timeInfor[n][1]): # criterion #7, future time window constraint must be strictly followd
                trueTableValue = False
                return trueTableValue
    return trueTableValue

if __name__ == '__main__':
        coord=[[0,2],
               [1,2],
               [2,2],
               [3,2],
               [4,2],
               [1,1],
               [2,1],
               [1,0],
               [2,0],
               [4,1]]
        # Mabe I can learn sth from Do.py
        N = 10
        nodes = [(j) for j in range(N)]
        tiple = [(i,j,k) for i in nodes for j in nodes for k in nodes if i!=j and j!=k and i!=k]
        double = [(i,j) for i in cnodes for j in cnodes if i!=j]
        # I don't need distance as I defined it in the adjacency matrix already.
        # distance={(m,n):lamda*np.hypot(coord[m][0]-coord[n][0],coord[m][1]-coord[n][1]) for m,n in double} # some changes needs for coord_x[m]
        dic_angle={(o,p,q):0 for o,p,q in triple}
        for o,p,q in triple:
            dic_angle[(o,p,q)]=math.pi-np.arccos(round((distance[(o,p)]**2+distance[(p,q)]**2-distance[(o,q)]**2)/(2*distance[(o,p)]*distance[(p,q)]),2))
        # I think I can have a test now. WHy not?
    iteration = 9
    # We don't need requests here
    bigNumber = 1000
    diagonal = 1.414 # diagonal distance
    recent = 1 # line distance, bigNumber, diagonal, recent is only for test. In the case of paper, they are not needed.
    # Use grid map as graph. However, I am worried in the future sth
    # related to memory storage may cause error.
    l = 1 # line distance between two neighboring nodes
    d = 1.414 # diagonal distance

    # This a 10-node map, numbering from 0 to 9
    # node 0 is depot, and node 9 is destination

    graph=[[0,l,0,0,0,d,0,0,0,0],
           [0,0,l,0,0,l,d,0,0,0],
           [0,l,0,l,0,d,l,0,0,0],
           [0,0,l,0,l,0,d,0,0,d],
           [0,0,0,l,0,0,0,0,0,l],
           [0,l,d,0,0,0,l,l,d,0],
           [0,d,l,d,0,l,0,d,l,0],
           [0,0,0,0,0,l,d,0,l,0],
           [0,0,0,0,0,d,l,l,0,0],
           [0,0,0,0,0,0,0,0,0,0]]
    # I try to wipe out time window constraint
    timeInfor=[[0,bigNumber],
               [0,bigNumber],
               [0,bigNumber],
               [0,bigNumber],
               [0,bigNumber],
               [0,bigNumber],
               [0,bigNumber],
               [0,bigNumber],
               [0,bigNumber],
               [0,bigNumber]]
    sets = list_all_sets(graph, timeInfor, iteration)
