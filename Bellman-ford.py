import time
import numpy as np
import matplotlib.pyplot as plt


class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])
    def printArr(self, dist):
        print("Vertex Distance from Source")
        for i in range(self.V):
            print("{0}\t\t{1}".format(i, dist[i]))
    def BellmanFord(self, src):
        dist = [float("Inf")] * self.V
        dist[src] = 0
        for _ in range(self.V - 1):
            for u, v, w in self.graph:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
        for u, v, w in self.graph:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                print("Graph contains negative weight cycle")
                return
        self.printArr(dist)
g = Graph(500)
matrix = np.random.randint(5, size=(500,500))
# print(matrix)
i = 0
for node in matrix:
    x = 0
    for index in node:
        g.addEdge(i, x, index)
        x += 1
    i += 1

while True:
    try:
        start_time = time.time()
        g.BellmanFord(0)
        end_time = time.time()
        print("Total time = ", end_time - start_time)
        break
    except:
        pass


x = [25, 50, 100, 150, 200]
y = [0.15509796142578125, 0.7905609607696533, 5.7084784507751465, 23.45373249053955 ,72.62042880058289]

plt.plot(x, y, label="Time Taken Per n Vertices", color="red",marker="*")
plt.ylabel('Time Taken By BellmanFord Algorithm (in seconds)')
plt.xlabel('Number of Vertices In Graph')
plt.title('BellmanFord Algorithm - Time Analysis')
plt.legend()
plt.show()
