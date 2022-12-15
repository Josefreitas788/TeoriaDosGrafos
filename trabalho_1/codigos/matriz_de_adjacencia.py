class GrafoAdjacente:
    def __init__(self, input_file):
        self.read_file(input_file)
        # self.write_matriz()

    def write_matriz(self, nome_arq):
        arq = open(nome_arq, "a")
        arq.write('Matriz de adjacencia =\n' + str(self.grafomatriz)  + '\n')
        arq.close()
        # print('Matriz de adjacência = ', self.grafomatriz)

    # Adiciona 0 ou 1 na matriz
    def inserir_aresta(self, u, v):
        # matriz começa do 1
        # não é grafo direcionado 
        self.grafomatriz[u-1][v-1] = 1
        self.grafomatriz[v-1][u-1] = 1

    def read_file(self, input_file):
        input = open(input_file, "r")
        lista = []
        for line in input:
            line = line.replace("\n", "")
            x = line.split(" ")
            lista.append(x)
        
        self.vertices = lista[0]
        del lista[0]

        # Criando a matriz com zeros 
        self.grafomatriz = [[0] *int(self.vertices[0]) for i in range(int(self.vertices[0]))]
        
        #adicionando arestas
        for i in lista:
            self.inserir_aresta(int(i[0]),int(i[1]))

# g = GrafoAdjacente("../teste.txt")
# g = GrafoAdjacente("../teste2.txt")
# g = GrafoAdjacente("../as_graph.txt")
