import numpy as np
class Grafo:
    def __init__(self, input_file):
        self.read_file(input_file)

    def inserir_aresta(self, u, v):
        self.grafo[u][v] = 1

    def remover_aresta(self, u, v):
        self.grafo[u][v] = 0

    def imprimir(self):
        for i in range((self.vertices//2)+1):
            for j in range(self.vertices):
                print(self.grafo[i][j], end=" ")
            print()
    
    def read_file(self, input_file):
        input = open(input_file, "r")
        n = 0
        for line in input:
            x = line.split(" ")
            try:
                x[1] = x[1].replace("\n", "")
                self.inserir_aresta(int(x[0]), int(x[1]))
            except:
                self.vertices = int(x[0])
                self.grafo = [[0 for i in range((self.vertices//2)+1)] for j in range(self.vertices)]
                pass


g = Grafo("../as_graph.txt")
g.imprimir()
