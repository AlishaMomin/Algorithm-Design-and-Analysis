import time
import numpy as np
import random
import matplotlib.pyplot as plt
from collections import defaultdict
 
# This class represents a directed graph
# using adjacency list representation
class Graph:
 
    # Constructor
    def __init__(self):
        self.graph = {}
    def addNodes(self,u):
        self.graph[u] = []
    def addEdge(self,u,v):
        self.graph[u].append(v)
    def BFS(self, s):
        visited = [False] * (max(self.graph) + 1)
        queue = []
        queue.append(s)
        visited[s] = True
 
        while queue:
            print("true")
            v = queue.pop(0)
            #print (s, end = " ")
            for i in self.graph[v]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True


# g = Graph()
# nodez = np.random.randint(5, size=200)
# # print(nodez)
# for z in range(len(nodez)):
#     if z < len(nodez)-1:
#         g.addEdge(nodez[z],nodez[z+1])
#         print("Add - ", nodez[z], " ", nodez[z+1])
# g.BFS(0)
# while True:
#     try:
#         start_time = time.time()
#         g.BFS(0)
#         end_time = time.time()
#         print("Total time = ", end_time - start_time)
#         break
#     except:
#         pass
 
x = []
y = []      

      
for i in range(5,225,25):
    g = Graph()
    
    nodez =[]
    #print(nodez)
    for z in range(i):
        nodez.append(z)
        g.addNodes(z)
    
        
    
    
    for k in range(len(nodez)):
        for j in range(len(nodez)):
            if k != j:
                    
                g.addEdge(nodez[k],nodez[j])
                    
                         
    start_time = time.time()
    # print(start_time)
    g.BFS(0)
    end_time = time.time()
    # print(end_time)
    x.append(i)
  
    y.append(end_time - start_time)
    
    
     
     
     
     
print(x)
print(y)      
      
    
plt.plot(x, y, label="Time Taken Per n Vertices", color="red",
         marker="*")

# y-axis label
plt.ylabel('Time Taken By BFS (in seconds)')
# x-axis label
plt.xlabel('Number of Vertices In The Graph')
# plot title
plt.title('BFS Algorithm - Time Analysis')
# showing legend
plt.legend()

# function to show the plot
plt.show()