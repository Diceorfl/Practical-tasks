from time import time
from random import randint
import matplotlib.pyplot as plt


def create_graph(V,E):
    matrix = [[float("Inf")] * V for i in range(V)]
    for i in range(V):
        matrix[i][i] = 0
    counter = 0
    #Generate a random adjacency matrix for weighted graph with 100 vertices and 500 edges
    while counter != E:
        i,j = 0,0
        while i == j:
            i,j = randint(0,V-1),randint(0,V-1)
        if matrix[i][j] == float("Inf"): counter+= 1
        matrix[i][j] = randint(1,E)
    return matrix

def floyd_warshall(graph):
    """ dist[][] will be the output matrix that will finally
        have the shortest distances between every pair of vertices """
    """ initializing the solution matrix same as input graph matrix
    OR we can say that the initial values of shortest distances
    are based on shortest paths considering no
    intermediate vertices """
    V = len(graph)
    dist = graph[:]
    """ Add all vertices one by one to the set of intermediate
     vertices.
     ---> Before start of an iteration, we have shortest distances
     between all pairs of vertices such that the shortest
     distances consider only the vertices in the set
    {0, 1, 2, .. k-1} as intermediate vertices.
      ----> After the end of a iteration, vertex no. k is
     added to the set of intermediate vertices and the
    set becomes {0, 1, 2, .. k}
    """
    for k in range(V):
        # pick all vertices as source one by one
        for i in range(V):
            # Pick all vertices as destination for the
            # above picked source
            for j in range(V):
                # If vertex k is on the shortest path from
                # i to j, then update the value of dist[i][j]
                dist[i][j] = min(dist[i][j] , dist[i][k]+ dist[k][j])
    for i in dist:
        print("Length from ",dist.index(i)," to others ",i)


FW_average_time = []
x = []
for n in range(10,201,10):
    FW_time = 0
    for k in range(5):
            G = create_graph(n,5*n)
            print("\nGraph: ")
            for i in G:
              print(i)
            print("\nFloyd Warshall algorithm: ")
            start = time()
            floyd_warshall(G)
            FW_time += time() - start
    x.append(n)
    FW_average_time.append(FW_time/5)

plt.title("Floyd Warshall")
plt.ylabel("Running Time")
plt.xlabel("V")
plt.grid()
plt.plot(x,FW_average_time,"-",label = "Emprical graph")
plt.legend()
plt.show()
