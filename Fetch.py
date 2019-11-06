# def add_Node(start, iteration, SETS):
# I hope to finish this part in order to do next step
# Before this part, I have adjacency matrix for graph
# I have start node, I have end node
# Exactly 5 steps, I have to go from start node to end node
# start node is node 0, end node is node 5
# In this part, I hope to add one node in the set at each new
# step, (in the updated set, list out terminal node, label number,
# preceding label number these three information)
# until end node 5 is reached. Stop!

def add_Node(graph, iteration, set):
    set.add(iteration)
    return set

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
                            set1 = set + [node]
                            sets.append(set1)
    return sets
    # And I am not sure if my method is dynamic programming or not.
    # My question: why some states be deleted automatically?such as [0,2,4,3,5]
    # I think do it once, then use sets as loop varialbe
    # result is wrong when iteration = 2
    # but result is right when iteration = 1
    # Smart loves problem. Something needs solving!
    # I guess something needs to do with iteration
    # Since after each iteration, set has been changed.
    # I want to try main function instead of def function
    # If it is success, I will manage to def function
    # I need to judge based on adjacency martix before add ing
    # new node
    # I hope to get it write down in 5 minutes
    # If only I can get the last element in the set, I can use set[-1]

if __name__ == '__main__':
    graph = [[0,2,3,0,0,0],
             [0,0,4,5,4,0],
             [0,2,0,6,2,0],
             [0,0,6,0,3,4],
             [0,2,0,9,0,7],
             [0,0,0,0,0,0]]
    iteration = 5
    sets = list_all_sets(graph, iteration)

# I hope to list out all possible set in each iteration
# which means, in first iteration, there should list out
# {0, 1} and {0, 2}
