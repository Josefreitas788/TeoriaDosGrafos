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

            
    def teste(self,vertice):
        print(self.grafo[vertice])

    def bfs(self, vertice):
        
        queue  = [vertice]
        visitados = []
        level = {}
        level[vertice] = 0


        while queue:
            
            vertice = queue.pop(0)
            if vertice not in visitados:
               
                print("Vertice: ", vertice, " Nivel: ", level[vertice])
                visitados.append(vertice)
                

                for i in self.grafo[vertice] :

                    level[i] = level[vertice] + 1
                    queue.append(i)

        print(visitados)
        return visitados




    def dfs(self, vertice):
        
        visitados = []
        stack = [vertice]
        level = {}
        level[vertice] = 0
        while stack:
            vertice = stack.pop()
            if vertice not in visitados:
                print("Vertice: ", vertice, " Nivel: ", level[vertice])
                visitados.append(vertice)
                for i in self.grafo[vertice]:
                    if i not in visitados:
                        stack.append(i)
                        level[i] = level[vertice] + 1
        print(visitados)
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
g.teste(1000)
print("BFS")
g.bfs(1)
print("DFS")
#g.dfs(1)
