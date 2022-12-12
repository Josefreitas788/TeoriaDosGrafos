# import numpy as np

class GrafoAdjacente:
    def __init__(self, input_file):
        self.read_file(input_file)
        self.imprimir()

    def imprimir(self):
        print('Matriz de adjacência = ', self.grafomatriz)

    # Adiciona 0 ou 1 na matriz
    def preenche_matriz(self, lista):
        self.grafomatriz[int(lista[0]) -1 ][int(lista[1])-1 ] = 1
        self.grafomatriz[int(lista[1]) -1 ][int(lista[0])-1 ] = 1

    def inserir_aresta(self, u, v):
        self.grafo[u][v] = 1

    def read_file(self, input_file):
        input = open(input_file, "r")
        lista = []
        for line in input:
            line = line.replace("\n", "")
            x = line.split(" ")
            lista.append(x)
        
        self.vertices = lista[0]
        del lista[0]

        # Matriz 
        self.grafomatriz = []
        self.grafomatriz_teste = []
        # linha
        for i in range(0, int(self.vertices[0])):
            self.grafomatriz.append([])
            
            #coluna
            for j in range (0, int(self.vertices[0])):
                self.grafomatriz[i].append(0)
                
        
        for y in range(0, int(self.vertices[0])):
            self.grafomatriz_teste.append([])
            print('y type= ',  y)
            print('lista[y][0] = ',type( lista[y][0]))
            if(int(lista[y][0]) == y+1):
                self.grafomatriz_teste[y].insert(0,1)
            else: 
                self.grafomatriz_teste[y].insert(0,0)

        print('grafomatriz_teste = ',self.grafomatriz_teste)
        
        # lista_bla = ['um', 'dois']
        # #lista_bla[2] = 'três'
        # lista_bla.insert(0,"borracha") 
        # print('lista_bla = ' , lista_bla)
     

        print(lista)    
        for x in lista:
            self.preenche_matriz(x)

g = GrafoAdjacente("../teste.txt")
# g = GrafoAdjacente("../as_graph.txt")
