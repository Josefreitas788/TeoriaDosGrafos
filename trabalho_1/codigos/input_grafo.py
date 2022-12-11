import numpy as np
input = open("../as_graph.txt", "r")
n = 0

n = 0
for line in input:
    x = line.split(" ")
    try:
        x[1] = x[1].replace("\n", "")

        grafo[int(x[0])][int(x[1])] = 1
    except:
        vertices = int(x[0])
        grafo = np.zeros(vertices//2+1,vertices)


print(grafo.shape)
print("n = ", n)
print("x = ", x)
