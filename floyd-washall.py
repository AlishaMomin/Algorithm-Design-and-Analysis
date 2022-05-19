# from matplotlib import pyplot as plt 
import timeit 
import random 

from matplotlib import pyplot as plt


n = 200

# create a graph 
def make_graph(novertices):
    x=[0,1,2,3,4,5,6,7,8,9,10,999]
    G=[]
    for i in range(novertices):
        row = []
        for j in range(novertices):
            row.append(random.choice(x))
        G.append(row)
             
    return G    
    
# Algorithm implementation
def floyd_warshall(G,nV):
    # defined table 
    distance = list(map(lambda i: list(map(lambda j: j, i)), G)) 
    print(distance)
    # Adding vertices individually
    for k in range(nV):
        for i in range(nV):
            for j in range(nV):
                # checks 
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    

x_list = []
floyd_warshall_list = []
for i in range(25,200+1,25):
    G = make_graph(i)
    # print(G)

    start = timeit.default_timer()
    floyd_warshall(G,i)
    end = timeit.default_timer()
    floyd_warshall_list.append(end-start)
    
    x_list.append(i)
    
    
    
plt.plot(x_list,floyd_warshall_list,linestyle = "solid",marker="*",c="blue", label="Floyd-Warshall - Time Analysis")
plt.title("Floyd-Warshall - Time Analysis")
plt.legend(['Time Taken Per n Nodes '],loc='upper left')
plt.xlabel("Number of nodes in Graph")
plt.ylabel("Time taken by Floyd-Warshall Algorithm (in seconds)")
plt.show()    
