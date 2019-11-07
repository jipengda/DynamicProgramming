# I hope to add label number, label infor(time, cost) to each feasible route
# The basic part is from China.py
# I need to edit script around append part to store label number, label infor which I request
def list_all_sets(graph, timeInfor, n, iteration):
    source=[0]
    sets=[]
    row = source[-1]
    node = -1
    for i in graph[row]:
        set1 = source
        node = node + 1
        if(i != 0):
            set1 = source + [node]
            sets.append(set1)
    for j in range(iteration-1):
            sets_copy = sets
            sets=[]
            for source in sets_copy:
                row = source[-1]
                node = -1
                for i in graph[row]:
                    set1 = source
                    node = node + 1
                    if(i != 0):
                        set1 = source + [node]
                        trueTableValue = criterion(graph, timeInfor, source, set1, node, n)
                        if trueTableValue is False:
                            sets.append(set1) # I need to edit scipt around here
    return sets

def criterion(graph, timeInfor, source, set1, node, n):
    trueTableValue = False
    if node in source:
        trueTableValue = True
        return trueTableValue
    if node-n not in source and node >= n:
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
    n = requests
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
    sets = list_all_sets(graph, timeInfor, n, iteration)
