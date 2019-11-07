# In this file, I hope to create something related to my EECPP problem referring to CookTop.py
# And also, tomorrow I want to ask Doctors about especially Dr. Kang about requests, node 5 problems
# Why not start it now?
# Firstly, I think I need to define my problem
# What is my start node?
# What is my destination?
# What is my adjacency matrix?
# What is my map?
# Less but not last, what is my criterions in EECPP to eliminate redundant state?
# I hope I can have an idea about those today!


# I must figure out the definition of requests first so that I can change it to get used to new problems.
# I hope to get answer as soon as possible

def list_all_sets(graph, timeInfor, requests, iteration):
    source=[0]
    sets=[]
    row = source[-1]
    node = -1
    labelNumber=0 # I use labelNumbet to store feasible route label number
    labelInforTime=0 # I use labelInforTime to store feasible route time
    labelInforCost=0 # I use labelInforTime to store feasible route cost
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
            sets.append(set1)
            print("label number:", labelNumber)
            print("time is ",labelInforTime, "cost is ", labelInforCost)
            print(set1)
    for j in range(iteration-1):
            sets_copy = sets
            sets=[]
            for source in sets_copy:
                row = source[-1]
                node = -1
                for i in graph[row]:
                    labelInforTime = 0
                    labelInforCost = 0
                    set1 = source
                    node = node + 1
                    if(i != 0):
                        set1 = source + [node]
                        trueTableValue = criterion(graph, timeInfor, source, set1, node, requests)
                        if trueTableValue is False:
                            labelNumber = labelNumber + 1
                            sets.append(set1) # I need to edit scipt around here
                            print("label number:",labelNumber)
                            print(set1)
                            memory=set1
                            length=len(memory)
                            labelInforTime=timeInfor[0][0]
                            for i in range(length-1):
                                m=memory[i]
                                n=memory[i+1]
                                labelInforTime=labelInforTime + graph[m][n]
                                labelInforCost = labelInforCost + graph[m][n]
                                labelInforTime = max(labelInforTime,timeInfor[n][0])
                            print("time is ",labelInforTime, "cost is ",labelInforCost)
    return sets

def criterion(graph, timeInfor, source, set1, node, requests):
    trueTableValue = False
    if node in source:
        trueTableValue = True
        return trueTableValue
    if node-requests not in source and node >= requests: # I hope to stop destination 5 appear early before iteration 5
        trueTableValue = True
        return trueTableValue
    memory=set1
    length=len(memory)
    time = timeInfor[0][0]
    for i in range(length-1):
        m=memory[i]
        n=memory[i+1]
        time = time + graph[m][n]
        timecost = time
        time = max(time, timeInfor[n][0])
    if(time>timeInfor[node][1]):
        trueTableValue = True
        return trueTableValue
    else:
        time=max(time, timeInfor[node][0])
        m=node
        set1=set(memory)
        cp_set=set([0,1,2,3,4,5,6,7,8,9,10]) # This needs to change when map information is changed. IMPORTANT!
        Jipeng = cp_set - set1
        for n in Jipeng:
            Github= time+graph[m][n]
            if(Github>timeInfor[n][1]):
                trueTableValue = True
                return trueTableValue
    return trueTableValue
if __name__ == '__main__':
    iteration = 10
    requests = 5
    bigNumber = 1000
    diagonal = 1.414 # diagonal distance
    recent = 1 # line distance
    timeInfor=[[0, bigNumber],
               [0, bigNumber],
               [0, bigNumber],
               [0, bigNumber],
               [0, bigNumber],
               [0, bigNumber],
               [0, bigNumber],
               [0, bigNumber],
               [0, bigNumber],
               [0, bigNumber],
               [0, bigNumber]]

    graph = [[0,diagonal,recent,diagonal,0,0,0,0,0,0,0],
             [0,0,recent,0,recent,diagonal,0,0,0,0,0],
             [0,recent,0,recent,diagonal,recent,diagonal,0,0,0,0],
             [0,0,recent,0,0,diagonal,recent,0,0,0,0],
             [0,0,diagonal,0,0,recent,0,recent,diagonal,0,0], #4
             [0,diagonal,0,diagonal,recent,0,recent,diagonal,recent,diagonal,0],
             [0,0,diagonal,0,0,recent,0,0,diagonal,recent,0], #6
             [0,0,0,0,0,diagonal,0,0,recent,0,0],
             [0,0,0,0,diagonal,0,diagonal,recent,0,recent,recent],
             [0,0,0,0,0,diagonal,0,0,recent,0,diagonal],
             [0,0,0,0,0,0,0,0,0,0,0]]
    sets = list_all_sets(graph, timeInfor, requests, iteration)

# This verification matches my expectation(a point, if the graph has no feasible route to visit up all nodes, what to do)
# (Do i need change sth of elimination criterion)
# What's most important, how to define my EECPP map to get used to this code, and use this code to get the same result as
# I use Cplex.
# I need to change the also elimination criterion because I don't have time constraint, and I need to add turning cost
# and I only have one drone
# These are too much to handle for today. I am so hungery that I need to go back home before 4 o'clock.
# I wonder to find out the optimal route in each iteration, time cost or cost, the minimum
