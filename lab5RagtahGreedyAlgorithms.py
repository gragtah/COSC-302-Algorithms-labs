import sys
import random
import math
import heapq


#ii) Give a proof of correctness and running-time bound for your algorithm.
'''
Here, I used Dijkstra's algorithm to find a shortest path, stopping  as soon as we select the target node in the graph during the process.
 We know that the normal implementation of Djikstra takes O(V.V + E) since for every iteration, we find the smallest element in a linear array. 
 To improve this, we use a priority queue implemented as a heap. heapq in python takes logarithmic time in the size of number of vertices. 
 Thus the total runtime improves to O(V logV + E)
 Since dijkstra works in a greedy fashion, we can just prove inductively for any number of edges already accepted in the optimal
 and dijkstra result path so far and say that if the optimal picks an edge that weighs lower than the one dijkstra chooses, then it can't be so
 in the first place because dijkstra would indeed have chosen that over the other one (as it is greedy).
'''
def fastest_trip(g, f):
    """
     takes an adjacency list of the travel graph and the travel-time
     function f and returns the path (as a list of nodes) that produces
     the fastest trip from the source to the destination, assuming you
     leave the source at time 0.  The structure of the graph G is as follows:

    0 is the source node
    1 is the destination node
    G is a dictionary indexed by node
    G[x] is a list of nodes [y_1, y_2, ... ] such that (x, y_i) is an edge in G

    You are given a graph G containing the information you need to solve this
    problem.  Assume that G is a directed graph containing a node 0, your
    starting point, and node 1, the destination.
    """
    # Initialize dist and predecessor (pred)
    dist = {}
    pred = {}
    path = []
    for node in g:
        dist[node] = 999999
        pred[node] = None
    dist[0] = 0

    # Create heap with initial distances for each node.
    heap = []
    for node in g:
        heap.append((dist[node],node))
    heapq.heapify(heap)

    while heap:
        distk, k = heapq.heappop(heap)
        if k == 1: #DESTINATION
            break
        if distk == 999999:
            break
        if distk > dist[k]:
            # Found a duplicate tuple with a higher distance so ignored it.
            continue
        for h in g[k]:
            distkh = distk +  f(k, h, 0)
            if distkh < dist[h]:
                dist[h] = distkh
                pred[h] = k
                """
                Python doesn't provide a method to change the key (distance)
                and update the tuple's position in the heap,
                so we just push a new tuple with a lower distance, and
                rather than deleting the old tuple, we'll keep it and
                ignore it if we ever pick it. This is convenient and fast.
                """
                heapq.heappush(heap, (distkh, h))
    x = 1
    path.append(x)
    while (x != 0):
        path.append(pred[x])
        x = pred[x]
    path.reverse()
    return path

   

# PRE-GENERATED TESTING STUFF

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
            G[0].append(r)

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

'''
We chose the movies clusetering, since the graph for the movies turns out to be much smaller, and makes the code run more efficiently.
For the first clustering, the distance between two movies will never be zero, however, that is not true for the second clustering. So, we only consider
movies that share actors.


'''

def kcluster(filename, k):
    file = open(filename, 'r')
    #choice = eval(input("Enter 1 or 2: \n1.k-cluster the movies, where the distance between movies is the number of characters that their titles have in common\n2.k-cluster the movies, where the distance between movies is the number of actors they share\n"))

                  
    d = {}
    s={}
    i=0
    R={}
    for line in file:
        #if i==125:
            #break
        i+=1
        line = line.strip()
        line = line.split("/")
        #print(line)
        try :
            for value in line[1:]:
                d[line[0]].append(value)
        except KeyError:
            for value in line[1:]:
                d[line[0]] = [value]


    G={}

    keys = list(d.keys())
    for i in range(len(keys)):
        s1=keys[i]
        if(s1 not in list(G.keys())):
            G[s1]= {}
        if(s1 not in list(R.keys())):
            R[s1]= {}
        for j in range(i+1,len(keys)):
            s2=keys[j]
            distance = strdist(s1,s2)
            distance1 = strdist(d[s1],d[s2])
            if distance !=0 :
                G[s1][s2] = distance
            if distance1 != 0:
                R[s1][s2] = distance1
            if distance !=0:
                if s2 not in list(G.keys()):
                    G[s2] = {}
                    G[s2][s1]=distance
                else:
                    if s1 not in G[s2]:
                        G[s2][s1] = distance
            if distance1 !=0 :
                if s2 not in list(R.keys()):
                    R[s2] = {}
                    R[s2][s1]= distance1
                else:
                    if s1 not in R[s2]:
                        R[s2][s1] = distance1

    
    #if choice==1:
    print("\n\nClustering 1 : k-cluster the movies, where the distance between movies is the number of characters that their titles have in common\n")
    clustering(G,k)
    #if choice==2:
    print("\n\n\nClustering 2: k-cluster the movies, where the distance between movies is the number of actors they share\n")
    clustering(R,k)
    
def strdist(s1, s2):
    s = {}
    #s1 = s1.lower()
    #s2 = s2.lower()
    for c in s1:
        try:
            x=(int)(s[c].pop())
            s[c].append(x+1)
        except KeyError:
            s[c] = [1]

    ctr = 0    
    for c in s2:
        try:
            x = s[c].pop()
            ctr+=1
            if (x==1):
                del (s[c])
            else:
                s[c].append(x-1)
        except KeyError:
            blah = 0
    return ctr
    
def clustering(G,k):
    count = 0
    subtrees = UnionFind()
    tree = []
    edges = [(G[u][v],u,v) for u in G for v in G[u]]
    edges.sort()
    j=[]
    for W,u,v in edges:
        #if(G[u][v] == G[v][u]):
        #    F("JJJ")
        if subtrees[u] != subtrees[v]:
            tree.append((G[u][v],u,v))
            j.append((G[u][v],u,v))
            subtrees.union(u,v)
    tree.sort(reverse=True)
    a=[]
    D={}
    i=0
    h=[]
    j.sort(reverse=True)

    for i in range(k-1):
        tree.pop(0)
    w=[]
    
    for value in tree:
        g=list(value)
        if g[1] not in w:
            w.append(g[1])
        if g[2] not in w:
            w.append(g[2])
            
    for tup in j:
        b=list(tup)
        if b[1] not in w:
            if b[1] not in h:
                h.append(b[1])
        if b[2] not in w:
            if b[2] not in h:
                h.append(b[2])
    #print(tree,"\n")
    #print(h)
    for tupl in tree:
        a=list(tupl)
        try:
            D[a[1]].append(a[2])
        except KeyError:
            D[a[1]] = [a[2]]
        try:
            D[a[2]].append(a[1])
        except KeyError:
            D[a[2]] = [a[1]]
    ans = []    
    path=[]
    visited = []
    #for key in D:
     #   print(key,D[key])
        
    for key in D:
        if(key not in visited):
            q=[key]
            while q:
                v=q.pop(0)
                if v not in path:
                    path=path+[v]
                    visited.append(v)
                    q=D[v]+q
            ans.append(path)
            path=[]
    for value in h:
        ans.append([value])

    print(ans)




class UnionFind:
    """Union-find data structure.

    Each unionFind instance X maintains a family of disjoint sets of
    hashable objects, supporting the following two methods:

    - X[item] returns a name for the set containing the given item.
      Each set is named by an arbitrarily-chosen one of its members; as
      long as the set remains unchanged it will keep the same name. If
      the item is not yet part of a set in X, a new singleton set is
      created for it.

    - X.union(item1, item2, ...) merges the sets containing each item
      into a single larger set.  If any item is not yet part of a set
      in X, it is added to X as one of the members of the merged set.
    """

    def __init__(self):
        """Create a new empty union-find structure."""
        self.weights = {}
        self.parents = {}

    def __getitem__(self, object):
        """Find and return the name of the set containing the object."""

        # check for previously unknown object
        if object not in self.parents:
            self.parents[object] = object
            self.weights[object] = 1
            return object

        # find path of objects leading to the root
        path = [object]
        root = self.parents[object]
        while root != path[-1]:
            path.append(root)
            root = self.parents[root]

        # compress the path and return
        for ancestor in path:
            self.parents[ancestor] = root
        return root
        
    def __iter__(self):
        """Iterate through all items ever found or unioned by this structure."""
        return iter(self.parents)

    def union(self, *objects):
        """Find the sets containing the objects and merge them all."""
        roots = [self[x] for x in objects]
        heaviest = max([(self.weights[r],r) for r in roots])[1]
        for r in roots:
            if r != heaviest:
                self.weights[heaviest] += self.weights[r]
                self.parents[r] = heaviest

def main():
    """	
    filename = input("Enter the name of the file you want to use: ")
    k = eval(input("Enter k for the k-clustering : "))
    kcluster(filename,k)
    """
    x=0
    #print('USE: gen_travel_graph(n) for generating graph of n nodes edge_time(i, j, t) as edge cost function, ')
    while(x!=3):
        x = eval(input("Choose: \n1. fastest_trip \n2. k-clustering \n3. Exit \n "))
        if(x==1):
            n = eval(input("Enter n to generate graph of n nodes: "))
            G = gen_travel_graph(n)
            print('Graph generated:\n', G)
            print ('\nrunning fastest_trip now... Done!')
            p = fastest_trip(G, edge_time)
            print (p)
            w = input('\nPress Enter to continue')
        if(x==2):
            filename = input("Enter the name of the file you want to use: ")
            k = eval(input("Enter k for the k-clustering : "))
            kcluster(filename,k)
            w = input('\nPress Enter to continue')

        if(x==3):
            break
        
    
main()

