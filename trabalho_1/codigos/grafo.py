
class Grafo:
    def __init__(self, input_file):
        self.vertices = vertices
        self.grafo = [[0 for i in range(vertices)] for j in range(vertices)]

    def inserir_aresta(self, u, v):
        self.grafo[u][v] = 1

    def remover_aresta(self, u, v):
        self.grafo[u][v] = 0

    def imprimir(self):
        for i in range(self.vertices):
            for j in range(self.vertices):
                print(self.grafo[i][j], end=" ")
            print()
    
    def read_file(self, input_file):
        input = open(input_file, "r")
        n = 0
        for line in input:
            print(line)
            x = line.split(" ")
            try:
                x[1] = x[1].replace("\n", "")
                this.inserir_aresta(int(x[0]), int(x[1]))
            except:
                self.vertices = int(x[0])
                pass

        
