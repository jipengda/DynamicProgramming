# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 11:44:38 2019

@author: jipengda
"""

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
                        # I probably should add criterion function here
                        # I guess def criterion(graph, set1, node)
                        # And return value is True table value
                        # If True table value is True, set1 = source + [node]
                        # sets.append(sets)
                        # If True table value is False, just pass(go back to steps before 36)
                        # The order should be adjusted for set1
                        set1 = source + [node]
                        trueTableValue = criterion(graph, timeInfor, source, set1, node, n)
                        if trueTableValue is False:# I hope this works
#                        if node not in source:
#                            set1 = source + [node] # I think this part should do somthing with trueTableValue
                            sets.append(set1)
    return sets

def criterion(graph, timeInfor, source, set1, node, n):
    trueTableValue = False
    if node in source:
        trueTableValue = True # True here means can be redundant infeasible
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
        # print(time)
        # I forget to make comparision between time and upper bound of node
    if(time>timeInfor[node][1]):
        trueTableValue = True
        return trueTableValue
    else:
        time=max(time, timeInfor[node][0])
        m=node
        set1=set(memory)
        cp_set=set([0,1,2,3,4,5])
        Jipeng = cp_set - set1
        for n in Jipeng: # I am lack of a range here, I want to use set operations to get left set
            Github= time+graph[m][n]
            if(Github>timeInfor[n][1]):
                trueTableValue = True
                return trueTableValue
    return trueTableValue
    # I wonder something wornd, but I don't know what and where it is
    # And also what to store label's number and preceding lable number is still
    # a # QUESTION:

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

# The Out of sets is not as expected. I believe there is something wrong.
# The simulation result is right, I made it !
# Jingyiqiujing, in the future I need to delete unnecessary commendts and make scripts short and simple
# So now, I can change iteration and get results, compare them to 316 to double check.
# I hope to change the name of source variable with source, as it is confliced wtth definition source
# node 5 problem is still to be solved.
