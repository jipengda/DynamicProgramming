# I hope to make script understandable by the third person
# Hopefully, with good discussion with Dr. Mastronarde this morning,
# I will make it work.
# This function is to find optimal routes from depot to destination in number of iterations(steps) as less as possible
# Given adjacency matrix as input of graph information(including nodes, cost , timewindow , arc between nodes)
# I use three functions: list_all_sets, criterion and compare.
# Try in each iteration, to get the optimal routes at that moment
# After all iterations finished, optimal routes are listed out in terms of time or cost.


# list_all_sets function is doing to list out optimal routes information(what nodes are visited in which order)
# (final time cost, final distance cost, and teriminal node information )
# within given number of iterations
def list_all_sets(graph, timeInfor, requests, iteration):
    source=[0]
    sets=[]
    row = source[-1]
    node = -1
    labelNumber=0
    labelInforTime=0
    labelInforCost=0
    for i in graph[row]:
        labelInforTime = 0
        labelInforCost = 0
        set1 = source
        node = node + 1
        if(i != 0):
            set1 = source + [node]
            labelNumber = labelNumber + 1
            labelInforTime = labelInforTime + i
            labelInforCost = labelInforCost + i
            labelInforTime = max(labelInforTime, timeInfor[node][0])
            set1 = set1 + [[labelInforTime, labelInforCost]]
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
                for i in graph[row]:
                    labelInforTime = 0
                    labelInforCost = 0
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
    # It works. Same as the paper. Good job!

# criterion function returns trueTabelValue, it judges through three criterions to see if set1 as new set:
# is valid or invalid
# default trueTableValue is True, means set1 as new set is valid
# If sets passes all three criterions, trueTableValue stays True
# But if not, trueTableValue changes to False, means set1 is invalid(not qualified)
def criterion(graph, timeInfor, source, set1, node, requests):
    trueTableValue = True
    if node in source: # criterion #1, new node should not have been visited
        trueTableValue = False
        return trueTableValue
    if node-requests not in source and node >= requests: # criterion #2, pick up node should have been visited before new node
        trueTableValue = False
        return trueTableValue
    memory = set1
    length = len(memory)
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

# fellow_label function returns delete_flag, which relates to if an old set should be kicked out by set1 as the new set
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
if __name__ == '__main__':
    iteration = 5
    requests = 2
    bigNumber = 1000
    diagonal = 1.414 # diagonal distance
    recent = 1 # line distance, bigNumber, diagonal, recent is only for test. In the case of paper, they are not needed.
    graph = [[0,2,3,0,0,0],
             [0,0,4,5,4,0],
             [0,2,0,6,2,0],
             [0,0,6,0,3,4],
             [0,2,0,9,0,7],
             [0,0,0,0,0,0]]
    timeInfor=[[0,30],
               [6,14],
               [12,17],
               [11,21],
               [12,22],
               [0,30]]
    sets = list_all_sets(graph, timeInfor, requests, iteration)
