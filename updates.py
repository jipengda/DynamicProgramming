# Today I hope to am begin to finish criteria part: include 3 criterions: #1, #2, and #6

# I hope to use one function to define all necessary criterion in order to
# eliminate redundant states from the sets

# Before this, I want to google search the song "Faith" by Jordan Feliz(Finished)
# I want to name this function a good name first

def criterion(sets):
    # I want to define a complete set with all nodes inside
    complete_set=[1,2,3,4,5]
    Visit = set(complete_set)
    # I hope to learn set operations for further action: Difference...
    requests = 2
    n = requests
    # I use a variable to store the new set after appending node
    new_set = set.append(node)
    #1: new node j must not have been previously visited
    if node in set:
        sets.remove(set)
        # I am not sure about this delete operation syntax
    #2: precedence constraint, if j is a destination, then the origin node j-n must have been previously visited
    # I don't understant this constraint completely, so that I will check the paper first
    # n is number of requests which is defined, in Figure 2, it is with only 2 requests
    if node-n not in set:
        sets.remove(set)
    #6: if we suppose that node j is visited at time tj, it mustbe
    # possible to visit each unvisited node l belongs to (S|[j])' while
    # respecting the time constraints: tj + Mj + Tjl < Bl, for
    # all l belongs to (S|[j])'
    # I am struggling with this constraint for I think there are including PRECEDING LABEL NUMBER, node j, future node,
    # They are too many possibilities that I am afraid that I cannot handle.

    # First, I need help to get calculate time interval after appending nodes
        # I hope this script from idle is correct
        timeInfor=[[0,30],
                   [6,14],
                   [12,17],
                   [11,21],
                   [12,22],
                   [0,30]]

        graph = [[0,2,3,0,0,0],
                 [0,0,4,5,4,0],
                 [0,2,0,6,2,0],
                 [0,0,6,0,3,4],
                 [0,2,0,9,0,7],
                 [0,0,0,0,0,0]]
        # I hope I can succeed this time
        CRLF=[0,1,2,3,4]
        length=len(CRLF)

        time = timeInfor[0][0]

        for i in range(length-1):
            m=CRLF[i]
            n=CRLF[i+1]
            time = time + graph[m][n]
            time = max(time, timeInfor[n][0])
            print(time)
        # I forget to make comparision between time and upper bound of node
            if(time>timeInfor[n][1]):
                sets.remove(set)
                print("Error")
    return new_sets
