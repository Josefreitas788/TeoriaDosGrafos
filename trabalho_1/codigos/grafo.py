import numpy as np
class Grafo:
    def __init__(self, input_file):
        self.read_file(input_file)

    def dados(self):
        print("Grafo = ",self.grafo)
        print("Vertices = ", self.vertices)
        arestas =  sum([len(self.grafo[i]) for i in self.grafo])
        #grau vertices
        for i in self.grafo:
            qtd = len(self.grafo[i])
            for j in self.grafo:
                if i in self.grafo[j] and j not in self.grafo[i]:
                    qtd += 1
            print("Grau do vertice ", i, " = ", qtd)

            
    def bfs(self, vertice):
        queue  = [vertice]
        visitados = [vertice]
        level = 0
        cont_levelAtual = len(self.grafo[vertice])

        while len(queue) != 0:
            vertice = queue.pop(0)
            if cont_levelAtual == 0:
                level += 1
                cont_levelAtual = len(self.grafo[vertice])
            cont_levelAtual -= 1
            
            #print("Vertice =", vertice, "Level ", level)
            #adiciona vizinhos nao visitados
            for i in self.grafo[vertice]:
                if i not in visitados:
                    queue.append(i)
                    visitados.append(i)
                    
        return visitados
    
    def dfs(self, vertice):
        visitados = []
        stack = [vertice]
        while len(stack) != 0:
            vertice = stack.pop()
            if vertice not in visitados:
                visitados.append(vertice)
                for i in self.grafo[vertice]:
                    stack.append(i)
        return visitados
    def read_file(self, input_file):
        input = open(input_file, "r")
      
        for line in input:
            x = line.split(" ")
            try:
                x[1] = x[1].replace("\n", "")
                self.grafo[int(x[0])].append(int(x[1]))
            except:
                self.vertices = int(x[0])
                self.grafo = { i: [] for i in range(1 , self.vertices) }
                pass


g = Grafo("../as_graph.txt")
g.dfs(1)
