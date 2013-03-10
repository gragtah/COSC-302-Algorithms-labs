import random
import math

# generates random graphs of n nodes
def gen_travel_graph(n):
    G = {0: [], 1: []}
    for i in range(2, n):
        G[i] = []
        for j in range(2, n):
            if i != j and random.random() < 0.6:
                G[i].append(j)

    while len(G[0]) <= math.ceil(n/4):
        r = random.randint(2, n-1)
        if r not in G[0]:
            G[0].append()

    count = 0
    while count <= math.ceil(n/4):
        r = random.randint(2, n-1)
        if 1 not in G[r]:
            G[r].append(1)
            count += 1

    return G

# can be used as an edge-timing function
def edge_time(i, j, t):
    r = (i * j) % 3
    if r == 0:
        return t + 1 + math.sqrt(i + (j%3) + t)
    elif r == 1:
        return t + 1 + math.log(i**2 + j**2 + t**2 + 1, 2)
    else:
        return t + 1 + 1.1 * t
