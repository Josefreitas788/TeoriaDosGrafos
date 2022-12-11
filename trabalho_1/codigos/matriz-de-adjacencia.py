# import numpy as np

class GrafoAdjacente:
    def __init__(self, input_file):
        self.read_file(input_file)
        # self.imprimir()
      

    def imprimir(self):
        print(self.vertices)
  
        # for i in range((self.vertices//2)+1):
        #     for j in range(self.vertices):
        #         print(self.grafo[i][j], end=" ")
        #     print()

    
    # def matriz(self, i, j):
    def matriz(self, lista):
        print('-------------TESTE-------------')
        print('lista[0]' , int(lista[0]))

        self.grafomatriz[int(lista[0]) -1 ][int(lista[1])-1 ] = 1
        self.grafomatriz[int(lista[1]) -1 ][int(lista[0])-1 ] = 1
        
        #print('self.vertices matriz = ', type(int(self.vertices[0])))
        # print('lista matriz = ', lista)
        # print('isso é a matriz = ', self.grafomatriz)

    def inserir_aresta(self, u, v):
        self.grafo[u][v] = 1

    def read_file(self, input_file):
        input = open(input_file, "r")
        lista = []
        for line in input:
            line = line.replace("\n", "")
            x = line.split(" ")
            lista.append(x)

        #######################################################
        
        self.vertices = lista[0]
        del lista[0]


        # Matriz 
        self.grafomatriz = []
        # linhas
        for i in range(0, int(self.vertices[0])):
            print('i =', i)
            self.grafomatriz.append([])
            for j in range (0, int(self.vertices[0])):
            # self.grafomatriz[i][j] = 0
                self.grafomatriz[i].append(0)
        print('isso é a matriz = ', self.grafomatriz)

        #passandoa a lista para a matriz 
        for x in lista:
            self.matriz(x)
        print('isso é a matriz = ', self.grafomatriz)

    

g = GrafoAdjacente("../teste.txt")


