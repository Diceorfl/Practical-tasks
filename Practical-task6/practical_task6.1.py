from time import time
from random import randint
from sys import maxsize



def create_graph():
    matrix = [[0] * 100 for i in range(100)]
    counter = 0
    #Generate a random adjacency matrix for weighted graph with 100 vertices and 500 edges
    while counter != 500:
        i,j = 0,0
        while i == j:
            i,j = randint(0,99),randint(0,99)
        if matrix[i][j] == 0: counter+= 1
        w = randint(1,500)
        matrix[i][j],matrix[j][i] = w,w
    return matrix

def convert(graph):
 # The row G[i] represents i-th edge with
 # three values u, v and w.
 G = []
 for i in range(len(graph)):
     for j in range(len(graph[i])):
         if graph[i][j] != 0:
             G.append((i,j,graph[i][j]))
 return G


# Function to find the
# vertex with minimum dist value, from
# the set of vertices still in queue
def minDistance(dist,queue):
    # Initialize min value and min_index as -1
    minimum = float("Inf")
    min_index = -1
    # from the dist array,pick one which
    # has min value and is till in queue
    for i in range(len(dist)):
        if dist[i] < minimum and i in queue:
            minimum = dist[i]
            min_index = i
    return min_index

#Function to print shortest path
#from source to j
#using parent array
def printPath(parent, j):
    #Base Case : If j is source
    if parent[j] == -1 :
        print(j, end = " ")
        return
    printPath(parent , parent[j])
    print(j, end = " ")

# Function to print
# the constructed distance
# array
def printSolution(dist, parent):
    src = 0
    print("Vertex \t\tDistance from Source\tPath")
    for i in range(1, len(dist)):
        print("\n%d --> %d \t\t%d \t\t" % (src, i, dist[i]), end = " "),
        printPath(parent,i)

'''Function that implements Dijkstra's single source shortest path
    algorithm for a graph represented using adjacency matrix
    representation'''
def dijkstra(graph, src):
    row = len(graph)
    col = len(graph[0])
    # The output array. dist[i] will hold
    # the shortest distance from src to i
    # Initialize all distances as INFINITE
    dist = [float("Inf")] * row
    #Parent array to store
    # shortest path tree
    parent = [-1] * row
    # Distance of source vertex
    # from itself is always 0
    dist[src] = 0
    # Add all vertices in queue
    queue = []
    for i in range(row):
        queue.append(i)
    #Find shortest path for all vertices
    while queue:
        # Pick the minimum dist vertex
        # from the set of vertices
        # still in queue
        u = minDistance(dist,queue)
        # remove min element
        queue.remove(u)
        # Update dist value and parent
        # index of the adjacent vertices of
        # the picked vertex. Consider only
        # those vertices which are still in
        # queue
        for i in range(col):
            '''Update dist[i] only if it is in queue, there is
            an edge from u to i, and total weight of path from
            src to i through u is smaller than current value of
            dist[i]'''
            if graph[u][i] and i in queue:
                if dist[u] + graph[u][i] < dist[i]:
                    dist[i] = dist[u] + graph[u][i]
                    parent[i] = u
    # print the constructed distance array
    printSolution(dist,parent)


# The main function that finds shortest
# distances from src to all other vertices
# using Bellman-Ford algorithm.
def bellman_ford(G,src):
    # Initialize distance of all vertices as infinite.
    dis = [float("Inf") for i in range(100)]
    # initialize distance of source as 0
    dis[src] = 0
    V = 100
    E = len(G)
    # Relax all edges |V| - 1 times. A simple
    # shortest path from src to any other
    # vertex can have at-most |V| - 1 edges
    for i in range(V - 1):
        for j in range(E):
            if dis[G[j][0]] + G[j][2] < dis[G[j][1]]:
                dis[G[j][1]] = dis[G[j][0]] + G[j][2]
    # By the condition of the problem, the graph has no negative weights, so we can skip this step
    #print("Vertex \t\tDistance from Source","\n")
    for i in range(1,len(dis)):
        print(src,"-->",i,"\t\t",dis[i])


dijkstra_time = 0
bellman_ford_time = 0
for i in range(10):
    matrix = create_graph()
    print("Dijkstra's algorithm")
    start = time()
    dijkstra(matrix,0)
    dijkstra_time+= time() - start
    print("\n")
    print("Bellman-Ford algorithm")
    matrix = convert(matrix)
    start = time()
    bellman_ford(matrix, 0)
    bellman_ford_time+= time() - start
print("Dijkstra average time: ", dijkstra_time/10)
print("Bellman Ford average time: ",bellman_ford_time/10)
