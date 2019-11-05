def map():
    graph = [[0,2,3,0,0,0],
             [0,0,4,5,4,0],
             [0,2,0,6,2,0],
             [0,0,6,0,3,4],
             [0,2,0,9,0,7],
             [0,0,0,0,0,0]]
    return graph
def timeInformation():# (Solved)
    timeInfor=[[0,30],
               [6,14],
               [12,17],
               [11,21],
               [12,22],
               [0,30]]
    return timeInfor

if __name__ == '__main__':
    map = map()
    timeInformation=timeInformation()
    print(map)


# I hope during this file, I can implement the algorithm
# (Solved)The time interval for each node is not defined. But I don't want to corret it now, implementation is more important.

def find_path(graph, start, end, path=[]):
    path = path + [start]
    start = 0
    sets = {1}
    sets = {2}
    STATES={SETS, TERMINAL NODES, LABLES}
    LABEL'S NUMBERS=[]
    PRECEDING LABEL NUMBER=[]
    k=[]
# And, what about elimination criteria. Why not list them out?
# Please refer criterion.pptx
# n means: n service requests
    iteration = 5
    SETS={start}
    for k in range(iteration):
        SETS=add_NODE(start, k, SETS) # I hope it works
        SETS=elimination_NODE()
# Each iteration, first find all possible sets, then eliminate states by criteria, finally save necessary states

def add_Node(start, iteration, SETS):
    if node not in SETS:
        SETS = SETS.add(node)
        # For each set, I hope to use different LABEL'S Number to differentiate.
        # Accrodingly, I need to add terminal nodes, LABELS(time, cost), and
        # PRECEDING LABEL NUMBER for each set, too
        # Nigara Falls this Saturday, plz give me power. Thanks
        # if specific condition is satisfied, then add_Node
        # specific condition, new node must be different,
        # new node must have connection with current node
        

    return SETS
