import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from random import randint

matrix = [[0] * 100 for i in range(100)]
counter = 0
#Generate a random adjacency matrix for a simple undirected unweighted graph with 100 vertices and 200 edges
while counter != 200:
    i,j = 0,0
    while i == j:
        i,j = randint(0,99),randint(0,99)
    if matrix[i][j] != 1: counter+= 1
    matrix[i][j],matrix[j][i] = 1,1

#Transfer the matrix into an adjacency list.
adjacency_list = [[] for i in range(100)]
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == 1:
          adjacency_list[i].append(j)
print("Adjacency list:")
for i in range(len(adjacency_list)):
    print(i,": ",adjacency_list[i])
print("\n")
matrix = np.array(matrix)
print("Adjacency matrix:")
print(matrix)
print("\n")
#Visualize the graph
G = nx.from_numpy_matrix(matrix)
plt.subplot(111)
nx.draw(G, with_labels=True, font_weight='bold')


#Use Depth-first search to find connected components of the graph
visited = [False] * 100
def dfs(v):
    visited[v] = True
    for w in adjacency_list[v]:
        if visited[w] == False:  #checking neighbors
            dfs(w)

components = []
for v in range(100):
    if not visited[v]: #Each unvisited vertex is a new component
        components.append(v)
        dfs(v)
print("Connected components:")
print(components)
print("\n")



# finds shortest path between 2 nodes of a graph using BFS
def bfs_shortest_path(graph, start, goal):
    # keep track of explored nodes
    explored = []
    # keep track of all the paths to be checked
    queue = [[start]]
    # return path if start is goal
    if start == goal:
        return "That was easy! Start = goal"
    # keeps looping until all possible paths have been checked
    while queue:
        # pop the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        if node not in explored:
            neighbours = graph[node]
            # go through all neighbour nodes, construct a new path and
            # push it into the queue
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                # return path if neighbour is goal
                if neighbour == goal:
                    return new_path
            # mark node as explored
            explored.append(node)
    # in case there's no path between the 2 nodes
    return "So sorry, but a connecting path doesn't exist :("

start = randint(0,99)
goal = randint(0,99)
print("Shortest path between " + str(start) + " and " + str(goal))
print(bfs_shortest_path(adjacency_list, start, goal))
plt.show()
