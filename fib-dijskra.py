import sys
import fibonnaciheap
import time
import numpy as np
import matplotlib.pyplot as plt 

def addNodes(G,nodes):
    for i in nodes:
        G[i]=[]
    return G 

def addEdges(G,edges,directed=False):
    for u,v,w in edges:
        if directed==True:
            G[u].append((v,w)) 
        else:
            G[u].append((v,w))
            G[v].append((u,w))
    return G

def adj_matrix_to_Graph(M):
    nodes=[]
    for i in range(len(M)):
        nodes.append(i)
    edges=[]
    for i in range(len(M)):
        for j in range(len(M[i])):
            if M[i][j]!=0:
                edges.append((i,j,M[i][j]))
    G={}
    G=addNodes(G,nodes)
    G=addEdges(G,edges)
    return G

class Graph():   
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = {}
    def min_distance(self,distance,traversed):
        min_index = 0 
        min_value = sys.maxsize
        for i in range(self.V):
            if traversed[i] is False and min_value > distance[i]:
                min_value = distance[i]
                min_index = i
        return min_index    
    def dijkstra(self, src, to):
        list_of_nodes=list(self.graph)
        inf = float('inf')
        cost={}
        cost[src]=0
        known={}
        Q= fibonnaciheap.FibonacciHeap()
        Q.insert_node(src)
        for node in self.graph:
            if node!=src:
                cost[node]=inf
                known[node]=False 
                Q.insert_node(src)
        while Q.least != None:
            v=Q.extract_min()
            for u in self.graph[v]:
                print(u)
                distance=cost[v]+u[1]
                if distance<cost[u[0]]:
                    cost[u[0]]=distance
                
        return cost[to] 
    
x = []
y = []

for i in range(25,200+1,25):
    g = Graph(i)
    res = np.random.randint(5, size=(i, i))
    print(res)
    # g.graph = {idx  : res[idx] for idx in range(len(res))}
    g.graph = adj_matrix_to_Graph(res)
    print(g.graph)
    start_time = time.time()
    g.dijkstra(0,i-1)
    end_time = time.time()
    x.append(i)
    y.append(end_time-start_time)
    

# plotting points as a scatter plot
plt.plot(x, y, label="Time Taken Per n Vertices", color="red",
         marker="*")

# y-axis label
plt.ylabel('Time Taken By Dijkstra (in seconds)')
# x-axis label
plt.xlabel('Number of Vertices In The Graph')
# plot title
plt.title('Dijkstra Algorithm using Fibonnaci Heap- Time Analysis')
# showing legend
plt.legend()

# function to show the plot
plt.show()    
    