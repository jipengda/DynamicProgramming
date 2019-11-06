# I hope to test previous two files to see if it gives the two routes as 317 said

# I will use Spyder to debug first

# I figure out how Fetch should pass variables to updates and also how
# updates should return variables
# Now I hope to whether I can combine thest two functions or not

# I believe I can finish combine today!

# Why not use example ({2,4},4) as it is impossible to visit node 1 afterwards while satisfying
# the time window constraint by criterion # 2
def criterion(graph, timeInfor, set, set1, node, n):
    trueTableValue = False
    if node in set:
        trueTableValue = True # True here means can be redundant infeasible
        return trueTableValue
    if node-n not in set:
        trueTableValue = True
        return trueTableValue
    CRLF=set1
    length=len(CRLF)
    time = timeInfor[0][0]
    for i in range(length-1):
        m=CRLF[i]
        n=CRLF[i+1]
        time = time + graph[m][n]
        timecost = time
        time = max(time, timeInfor[n][0])
        # print(time)
        # I forget to make comparision between time and upper bound of node
        if(time>timeInfor[n][1]):
            trueTableValue = True
            return trueTableValue
    return trueTableValue
    # I wonder something wornd, but I don't know what and where it is
    # And also what to store label's number and preceding lable number is still
    # a # QUESTION:
if __name__ == '__main__':
    node = 1
    i = 2
    set=[0,2,4]
    set1 = set + [node]
    requests = 2
    n = requests
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
    trueTableValue = criterion(graph, timeInfor, set, set1, node, n)


def list_all_sets(graph, iteration):
    set=[0]
    sets=[]
    row = set[-1]
    node = -1
    for i in graph[row]:
        set1 = set
        node = node + 1
        if(i != 0):
            set1 = set + [node]
            sets.append(set1)
    for j in range(iteration-1):
            sets_copy = sets
            sets=[]
            for set in sets_copy:
                row = set[-1]
                node = -1
                for i in graph[row]:
                    set1 = set
                    node = node + 1
                    if(i != 0):
                        # I probably should add criterion function here
                        # I guess def criterion(graph, set1, node)
                        # And return value is True table value
                        # If True table value is True, set1 = set + [node]
                        # sets.append(sets)
                        # If True table value is False, just pass(go back to steps before 36)
                        if node not in set:
                            set1 = set + [node] # I think this part should do somthing with trueTableValue
                            sets.append(set1)
    return sets
