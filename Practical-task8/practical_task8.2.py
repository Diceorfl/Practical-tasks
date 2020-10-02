import numpy as np
import networkx as nx
import random
import string
import tracemalloc
from timeit import timeit
import matplotlib.pyplot as plt

N = 200

def find_cliques(G):
    """Search for all maximal cliques in a graph.

    Maximal cliques are the largest complete subgraph containing
    a given node.  The largest maximal clique is sometimes called
    the maximum clique.

    Returns
    -------
    generator of lists: genetor of member list for each maximal clique

    See Also
    --------
    find_cliques_recursive :
    A recursive version of the same algorithm

    Notes
    -----
    To obtain a list of cliques, use list(find_cliques(G)).

    Based on the algorithm published by Bron & Kerbosch (1973) [1]_
    as adapted by Tomita, Tanaka and Takahashi (2006) [2]_
    and discussed in Cazals and Karande (2008) [3]_.
    The method essentially unrolls the recursion used in
    the references to avoid issues of recursion stack depth.

    This algorithm is not suitable for directed graphs.

    This algorithm ignores self-loops and parallel edges as
    clique is not conventionally defined with such edges.

    There are often many cliques in graphs.  This algorithm can
    run out of memory for large graphs.

    References
    ----------
    .. [1] Bron, C. and Kerbosch, J. 1973.
       Algorithm 457: finding all cliques of an undirected graph.
       Commun. ACM 16, 9 (Sep. 1973), 575-577.
       http://portal.acm.org/citation.cfm?doid=362342.362367

    .. [2] Etsuji Tomita, Akira Tanaka, Haruhisa Takahashi,
       The worst-case time complexity for generating all maximal
       cliques and computational experiments,
       Theoretical Computer Science, Volume 363, Issue 1,
       Computing and Combinatorics,
       10th Annual International Conference on
       Computing and Combinatorics (COCOON 2004), 25 October 2006, Pages 28-42
       http://dx.doi.org/10.1016/j.tcs.2006.06.015

    .. [3] F. Cazals, C. Karande,
       A note on the problem of reporting maximal cliques,
       Theoretical Computer Science,
       Volume 407, Issues 1-3, 6 November 2008, Pages 564-568,
       http://dx.doi.org/10.1016/j.tcs.2008.05.010
    """
    if len(G) == 0:
        return

    adj = {u: {v for v in G[u] if v != u} for u in G}
    Q = [None]

    subg = set(G)
    cand = set(G)
    u = max(subg, key=lambda u: len(cand & adj[u]))
    ext_u = cand - adj[u]
    stack = []

    try:
        while True:
            if ext_u:
                q = ext_u.pop()
                cand.remove(q)
                Q[-1] = q
                adj_q = adj[q]
                subg_q = subg & adj_q
                if not subg_q:
                    yield Q[:]
                else:
                    cand_q = cand & adj_q
                    if cand_q:
                        stack.append((subg, cand, ext_u))
                        Q.append(None)
                        subg = subg_q
                        cand = cand_q
                        u = max(subg, key=lambda u: len(cand & adj[u]))
                        ext_u = cand - adj[u]
            else:
                Q.pop()
                subg, cand, ext_u = stack.pop()
    except IndexError:
        pass

def graph_number_of_cliques(G,cliques=None):
    """Returns the number of maximal cliques in G.

    An optional list of cliques can be input if already computed.
    """
    if cliques is None:
        cliques=list(find_cliques(G))
    return   len(cliques)

def F(G):
    graph_number_of_cliques(G)

experimental_time_F = []
experimental_space_F = []

for i in range(1, N + 1):
    G = nx.complete_graph(i)
    experimental_time_F += [timeit(lambda: F(G), number=3)]  # measure experimental time
    tracemalloc.start()
    G = nx.complete_graph(i)
    F(G)
    experimental_space_F += [tracemalloc.get_traced_memory()[1]]  # measure experimental space
    tracemalloc.stop()

theoretical_one_step = sum(experimental_time_F[100:]) / sum([n ** 3 for n in range(100, N + 1)])
# calculate theoretical time
theoretical_time_F = [theoretical_one_step * n ** 3 for n in range(N + 1)]

theoretical_one_step = sum(experimental_space_F[100:]) / sum([n ** 2 for n in range(100, N + 1)])
# calculate theoretical space
theoretical_space_F = [theoretical_one_step * n ** 2 for n in range(N + 1)]

# create plot
plt.title('Max clique')
plt.xlabel('Number of nodes')
plt.ylabel('Running time')
plt.grid()
plt.plot(experimental_time_F, color='red', label='experimental')
plt.plot(theoretical_time_F, color='blue', label='theoretical')
plt.legend(loc='upper left')
plt.show()

# create plot
plt.title('Max clique')
plt.xlabel('Number of nodes')
plt.ylabel('Space')
plt.grid()
plt.plot(experimental_space_F, color='red', label='experimental')
plt.plot(theoretical_space_F, color='blue', label='theoretical')
plt.legend(loc='upper left')
plt.show()
