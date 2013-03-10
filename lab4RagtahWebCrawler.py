import sys
import re
import urllib.request, urllib.error, urllib.parse
from urllib.parse import urlparse
from urllib.request import urlopen
from urllib.parse import urljoin
linkregex = re.compile('<a\s*href=[\'|"](.*?)[\'"].*?>')
crawled = set([])
R={}
sccno=[]
size = []
def webcrawl(url, maxdepth = 10, domain = True):
    tocrawl = set([url])
    crawled = set([])
    test = url.split(".")[1]
    #print(tocrawl)
    depth=0
    nodes=0
    G = {}
    while (len(tocrawl)>0):
        links=set()
        try:
            crawling = tocrawl.pop()
            nodes+=1
            #print(len(tocrawl),crawling)

        except KeyError:
            raise StopIteration
        url = urlparse(crawling)
        try:
            response = urlopen(crawling)
        except:
            continue
        msg = str(response.read())
        links = linkregex.findall(msg)
        crawled.add(crawling)
        for link in links:
            if link.startswith('/'):
                link = 'http://' + url[1] + link
            elif link.startswith('#'):
                link = 'http://' + url[1] + url[2] + link
            elif not link.startswith('http'):
                link = link = 'http://' + url[1] + '/' + link
                h = urlparse(link)
                #if h[1].split(".")[1] == test:
            h = urlparse(link)
            if(domain == True):
                if h[1].split(".")[1] == test:
                    if link not in crawled:
                        if(depth<maxdepth):
                            tocrawl.add(link)
            else:
                if link not in crawled:
                    if(depth<maxdepth):
                        tocrawl.add(link)
            try:
                if link not in G[crawling]:
                    G[crawling].append(link)
                    nodes+=1
            except KeyError:
                nodes+=1
                G[crawling] = [link]
            try:
                if(crawling not in R[link]):
                    R[link].append(crawling)
            except KeyError:
                R[link] = [crawling]
        
        depth +=1
        
   
    scc_dict,comp_dict = strongly_connected_components(G)
    
    graphstats(G,nodes)

    return scc_dict,comp_dict

def graphstats(G,nodes):
    edges=0
    indegree =[]
    outdegree =[]
    for key in G:
        edges += len(G[key])
    print("Total number of nodes visited: ",nodes)
    print("Density: ",(nodes/edges))
    print("No. of SCCs : ",sccno[0])
    size.sort()
    print("Maximum number of SCCs : ", size[len(size)-1])
    print("Minimum number of SCCs : ", size[0])
    if(len(size)%2 == 0):
        print("Median : ", size[(len(size)//2)-1])
    else:
        print("Median : ", (size[len(size)//2] + size[(len(size)//2)+1]))
    for key in G:
        outdegree.append(len(G[key]))
    for key in R:
        indegree.append(len(R[key]))
    indegree.sort()
    outdegree.sort()
    print("Maximum number of indegree : ", indegree[len(indegree)-1])
    print("Minimum number of indegree : ", indegree[0])
    if(len(indegree)%2 == 0):
        print("Median of indegree : ", indegree[(len(indegree)//2)-1])
    else:
        print("Median of indegree : ", (indegree[(len(indegree)//2)-1] + indegree[(len(indegree)//2)])/2)

    print("Maximum number of outdegree : ", outdegree[len(outdegree)-1])
    print("Minimum number of outdegree : ", outdegree[0])
    if((len(outdegree))%2 == 0):
        print("Median of outdegree : ", outdegree[(len(outdegree)//2)-1])
    else:
        print("Median of outdegree : ", (outdegree[(len(outdegree)//2)-1] + outdegree[len(outdegree)//2])/2)
    
def strongly_connected_components(graph):
    """ Find the strongly connected components in a graph using
        Tarjan's algorithm.
        
       
        """
    
    result = []
    stack = [ ]
    low = { }
    l={}
    def visit(node):
        if node in low: return
        
        num = len(low)
        low[node] = num
        stack_pos = len(stack)
        stack.append(node)

        if(node in graph):
                for successor in graph[node]:
                    visit(successor)
                    low[node] = min(low[node], low[successor])
        
        if num == low[node]:
            component = tuple(stack[stack_pos:])
            del stack[stack_pos:]
            result.append(component)
            for item in component:
                low[item] = len(graph)
    
    for node in graph:
        visit(node)
    j=0
    for i in result:
            l[j]= list(i)
            size.append(len(list(i)))
            j+=1
    sccno.append(j)
    return SCC_number(graph,l)

def SCC_number(g,l):
    h=[]
    scc_dict= {}
    comp_dict = {}
    count = 0
    for i in range(0,len(list(l.keys()))):
        scc_dict[i]={}
        comp_dict[i]={}
        for value in l[i]:
            try:
                comp_dict[i][value] = g[value]
            except KeyError:
                comp_dict[i][value] = []
            for j in range(0,len(list(l.keys()))):
                if(i==j): continue
                if value in list(g.keys()):
                    for val in g[value]:
                        if val in l[j]:
                            h.append((value,val))
                            count+=1
        scc_dict[i][count]=h
        h =[]
        count =0
    '''for key in newG:
        for i in range(1,500):
            try:
                print(key,"  ",newG[key][i])
            except KeyError:
                b=0
    '''
    '''for i in range(len(list((scc_dict.keys())))):
        for key in scc_dict[i]:
            #if(comp_dict[i][key] != []):
            print(i,"   ",key,"  ",scc_dict[i][key],"\n")
    '''
    return scc_dict,comp_dict 
                
                        
                        
        

def main():
    ur = input("Enter the url of the website: ")
    depth = eval(input("enter the depth: "))
    domain = input("Enter True or False for domain: ")
    if domain == "True":
        scc_dict,comp_dict = webcrawl(ur,depth,True)
    else:
        scc_dict,comp_dict = webcrawl(ur,depth, False)

    print(scc_dict,"\n\n")
    print(comp_dict, "\n\n")
        

main()
#(strongly_connected_components({0:[1,2,3],1:[0,2,4,5],2:[3], 3:[0],5:[4]}))
