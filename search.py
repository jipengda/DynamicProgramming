#Type here to search

# God, first , I hope to define the map as Figure 2 rather than Figure 3
# God, second, I hope to implement the algorithm of dynamic programming
# God, third, I hope Fetch my programming gives out Feasible Routes


#def creat map(x1, x2):

#def creatMap(N,timeInformation, costInformation):

# RecursionError: maximum recursion depth exceeded in comparision
# def find_all_paths(graph, start, end, path=[]):
#     pth = path + [start]
#     if start == end:
#         return [path]
#     if not graph.has_key(start):
#         return []
#     paths = []
#     for node in graph[start]:
#         if node not in path:
#             newpaths = find_all_paths(graph, node, end, path)
#             # I hope I already understand the script
#             for newpath in newpaths:
#                 paths.append(newpath)
#     return paths
# #end
#  finds the shortest path:
def find_shortest_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
    # I hope before I write script, I can understand script.
        return None
    shortest = None
    for node in graph[start]:
        if node not in path:
            newpath = find_shortest_path(graph, node, end, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    return shortest
# # find path until one is available
# def find_path(graph, start, end, path=[]):
#     path = path + [start]
#     if start == end:
#         return path
#     if start not in graph:
#         return None
#     for node in graph[start]:
#         if node not in path:
#             newpath = find_path(graph, node, end, path)
#             if newpath: return newpaht
#     return None
# # end
#hotjar #Adjacency List is bad to represent Graph as it can't include weight, I think.
# A classs to represent a graph. A graph
# is the list of the adjacency lists.
# Size of the array will be the no. of the
# vertices "V"
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [None] * self.V

    # Function to add an edge in an undirected graph
    def add_edge(self, src, dest):
        #Adding the node to the source node
        node = AdjNode(dest)
        node.next = self.graph[src]
        self.graph[src] = node

        #Adding the source node to the destination as
        #it is the undirected graph
        node = AdjNode(src)
        node.next = self.graph[dest]
        self.graph[dest] = node
    # Function to print the graph
    def print_graph(self):
        for i in range(self.V):
            print("Adjacency list of vertex {}\n head".format(i), end="")
            temp=self.graph[i]
            while temp:
                print("->{}".format(temp.vertex),end="")
                temp = temp.next
            print("\n")
#end

#adjacency matrix, applied!
graph = [[0,2,3,0,0,0],
         [0,0,4,5,4,0],
         [0,2,0,6,2,0],
         [0,0,6,0,3,4],
         [0,2,0,9,0,7],
         [0,0,0,0,0,0]]
#end

if __name == '__main__':
    graph  = {
            '0':['1','2'],
            '1':['2','3','4'],
            '2':['1','3','4'],
            '3':['2','4','5'],
            '4':['1','3','5']
        }
    # find_all_paths(graph, start, end, path=[])
    find_path(graph, '0','5')
