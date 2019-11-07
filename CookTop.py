# I hope to add label number, label infor(time, cost) to each feasible route
# The basic part is from China.py
# I need to edit script around append part to store label number, label infor which I request
def list_all_sets(graph, timeInfor, n, iteration):
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
    if node-n not in source and node >= requests: # I hope to stop destination 5 appear early before iteration 5
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
        cp_set=set([0,1,2,3,4,5])
        Jipeng = cp_set - set1
        for n in Jipeng:
            Github= time+graph[m][n]
            if(Github>timeInfor[n][1]):
                trueTableValue = True
                return trueTableValue
    return trueTableValue
if __name__ == '__main__':
    requests = 2
    iteration = 5
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
