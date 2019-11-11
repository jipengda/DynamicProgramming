# In this file ,I hope to solve the fellow label problem
# Referring to test.py, under guarantee right output, I hope to add a time and cost element for each possilbe set
# And also, with that element, it will be more convenient to get the new time and cost on the basis of previous data
# Assum now sets are full of set1 which already has that element
# I hope to write a funtion to stop the new one which either has same time but less cost, or has same cost but larger time from
# adding into the sets, compared with other ones in the sets

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
                return delete_flag=1

    # if time is equal, compare the cost, if it has more cost, delete flag = 1, default delete flag=0, means does not delete

    # cost compare
    for i in range(length-1):
        compare=sets[i]
        compare_time=compare[0]
        compare_cost=compare[1]
        if (new_one_cost == compare_cost):
            if(new_one_time > compare_time):
                return delete_flag=1
    return delete_flag
    # if cost is equal, compare the time, if it has more time, delete flag = 1, default delete flag=0, means does not delte

    # I will use a example to test Firstly
    # Why delete_flag is 0 rather than 1? It is wrong.
    # Solved: my index for time and cost is wrong. And also the example should have output 0.
    # Solution: correct the script and change to another example.
    # If I want to chang use this function, I have to redefine sets in my previous script. It
    # should have time and cost element in the end.

    # I need to change set1 first to change sets, since sets.append(set1)


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
            set1 = set1+[labelInforTime, labelInforCost]
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
                for i in graph[row]:
                    labelInforTime = 0
                    labelInforCost = 0
                    #change here thanks to formate changing. use last element to store
                    lastElement = source.pop()
                    set1 = source
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
                            set1 = set1+[labelInforTime, labelInforCost]
                            sets.append(set1) # I need to edit scipt around here
                            print("label number:",labelNumber)
                            # print(set_printing)
                            print(set1)
                            # Accrodingly, I need to change criterion function
    return sets
    # Let me have a test
    # Why IndexError: list index out of range
