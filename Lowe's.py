def list_all_sets(graph, timeInfor, requests, iteration):
    source=[0]
    sets=[]
    row = source[-1]
    node = -1
    labelNumber=0 # I use labelNumbet to store feasible route label number
    labelInforTime=0 # I use labelInforTime to store feasible route time
    labelInforCost=0 # I use labelInforTime to store feasible route cost
    for i in graph[row]:# Maybe I can do something helpful here
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
            # set_printing=set1+[[labelInforTime, labelInforCost]]
            set1 = set1+[[labelInforTime, labelInforCost]]
            sets.append(set1) # why not use set1 new instead?
            print("label number:", labelNumber)
            # print(set_printing)
            print(set1)
    for j in range(iteration-1):
            sets_copy = sets
            sets=[]
            for source in sets_copy:
                #row = source[-1] #This needs changing since format is changing
                row = source[-2] #-2 is last visiting node, -1 is time and cost infor
                node = -1
                lastElement = source.pop()
                set1 = source
                for i in graph[row]:
                    labelInforTime = 0
                    labelInforCost = 0
                    #change here thanks to formate changing. use last element to store
                    node = node + 1
                    if(i != 0):
                        set1 = source + [node]
                        trueTableValue = criterion(graph, timeInfor, source, set1, node, requests)
                        if trueTableValue is False:
                            labelNumber = labelNumber + 1
                            memory=set1
                            length=len(memory)
                            labelInforTime=timeInfor[0][0]
                            for k in range(length-1):
                                m=memory[k]
                                n=memory[k+1]
                                labelInforTime=labelInforTime + graph[m][n]
                                labelInforCost = labelInforCost + graph[m][n]
                                labelInforTime = max(labelInforTime,timeInfor[n][0])
                            # set_printing=set1+[[labelInforTime, labelInforCost]]
                            set1 = set1+[[labelInforTime, labelInforCost]]
                            sets.append(set1) # I need to edit scipt around here
                            print("label number:",labelNumber)
                            # print(set_printing)
                            print(set1)
                            # Accrodingly, I need to change criterion function
    return sets
    # Let me have a test

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
        cp_set=set([0,1,2,3,4,5]) # This needs to change when map information is changed. IMPORTANT!
        Jipeng = cp_set - set1
        for n in Jipeng:
            Github= time+graph[m][n]
            if(Github>timeInfor[n][1]):
                trueTableValue = True
                return trueTableValue
    return trueTableValue

def fellow_label(sets, new_one):
    new_one = sets[-1]
    new_one_time = new_one[0]
    new_one_cost = new_one[1]
    length=len(sets)
    delete_flag=0
    # Here, every set has format like [node x1, node x2, node x3, node x4, node x5, [time, cost]]
    # time compare
    for i in range(length-1):
        compare=sets[i]
        compare_time=compare[0]
        compare_cost=compare[1]
        if (new_one_time == compare_time):
            if(new_one_cost > compare_cost):
                delete_flag=1
                return delete_flag

    # if time is equal, compare the cost, if it has more cost, delete flag = 1, default delete flag=0, means does not delete

    # cost compare
    for i in range(length-1):
        compare=sets[i]
        compare_time=compare[0]
        compare_cost=compare[1]
        if (new_one_cost == compare_cost):
            if(new_one_time > compare_time):
                delete_flag=1
                return delete_flag
    return delete_flag
if __name__ == '__main__':
    iteration = 1
    requests = 2
    bigNumber = 1000
    diagonal = 1.414 # diagonal distance
    recent = 1 # line distance
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
