import heapq
import numpy as np 
from scipy.sparse import csr_matrix
import time
# https://www.ime.usp.br/~pf/algoritmos_para_grafos/aulas/components.html#:~:text=Uma%20componente%20conexa%20(%3D%20connected,subgrafo%20conexo%20maximal%20do%20grafo.
#from memory_profiler import profile
class Grafo:
    
    def __init__(self, input_file):

        self.opcao = input("\nDigite o tipo de representação desejada:\n 1 - Lista de adjacência\n 2 - Matriz de adjacência\n")
        self.read_file(input_file)
        

    # número de vértices, número de arestas, grau de cada vértice.
    def dados(self):
        if(self.opcao == '1'):
            arq = open("../outputs/dados_grafo_lista.txt", "a")
            arq.write('Numero de vertices do grafo = ' + str(self.vertices)  + '\n')
            arestas =  sum([len(self.grafo[i]) for i in self.grafo])
            arq.write('Numero de arestas do grafo = ' + str(arestas//2)  + '\n')
            #grau vertices
            for i in self.grafo:
                qtd = len(self.grafo[i])
                for j in self.grafo:
                    if i in self.grafo[j] and j not in self.grafo[i]:
                        qtd += 1
                arq.write('Grau do vertice'+ str(i) + ' = ' + str(qtd)+ '\n')
            arq.close()
        if(self.opcao == '2'):
            arestas = 0
            arq = open("../outputs/dados_grafo_matriz.txt", "a")
            arq.write('Numero de vertices do grafo = ' + str(self.vertices[0])  + '\n')
            for i in range(int(self.vertices[0])):
                for j in range(int(self.vertices[0])):
                    if self.grafo[i][j] != 0:
                        arestas += 1

            arq.write('Numero de arestas do grafo = ' + str(arestas//2)  + '\n')
            #grau vertices
            for i in range((int(self.vertices[0]))):
                qtd = 0
                for j in range((int(self.vertices[0]))):
                    if self.grafo[i][j] == 1:
                        qtd += 1
                arq.write('Grau do vertice'+ str(i) + ' = ' + str(qtd)+ '\n')
            arq.close()

    def conexo(self, nome_arq):
            self.cc = [] 
            visitados = self.bfs(1, False)
            if len(visitados) == self.vertices:
                # print("Grafo conexo")
                self.componentes_conexos(self.grafo, True, nome_arq)
            else:
                # print("Grafo desconexo")
                self.componentes_conexos(self.grafo, False, nome_arq)

    # mudando o self.grafo
    def componentes_conexos(self, grafo, isconexo, nome_arq):
        id = 0
        dic_grafo = {}
        # aux_grafo = grafo
        aux_grafo = {}
        aux_grafo.update(grafo)
        aux = False
        arq = open(nome_arq, "a")
        # print('grafo correto = ', self.grafo)
        if(self.opcao == '1'):

            if (isconexo == True):
                for i in grafo:
                    if(len(dic_grafo) == 0):
                        dic_grafo[0] = grafo[i]
                    else: 
                        for j in grafo[i]:
                            if( j not in dic_grafo[0]):
                                dic_grafo[0].insert(0,j)
                
                min_max = len(dic_grafo[0])
                arq.write("Quantidade de componentes do grafo = 1\n")
                arq.write('Menor componente conexo = ' + str(min_max) + '\n' + 'Maior componente conexo = ' +  str(min_max) + '\n')
                arq.write('Componentes conexos do grafo = ' + str(dic_grafo)  + '\n')
                arq.close()
                dic_grafo.clear()
            else:
                # for i in dic_grafo:
                for j in grafo:    
                    # primeiro item

                    if(len(dic_grafo) == 0):
                        dic_grafo[id] = aux_grafo[j]
                        dic_grafo[id].insert(0, j)

                    else:
                        for i in dic_grafo:
                            if(j in dic_grafo[id]):
                                dic_grafo[id] = aux_grafo[j]
                                if(j not in dic_grafo[id]):
                                    dic_grafo[id].insert(0, j)
                            else:
                                # se estiver na lista
                                for x in aux_grafo[j]:
                                    if(x in dic_grafo[id]):
                                        dic_grafo[i].insert(0, j)
                                        break
                                    else:
                                        aux = True
                                        break
                                
                        if(aux == True):
                            id += 1
                            dic_grafo[id] = aux_grafo[j]
                            dic_grafo[id].insert(0, j)
                            aux = False

                # Abrindo o arquivo para gravação 
                arq.write("Quantidade de componentes do grafo = " +str(max(dic_grafo.keys()) + 1)+"\n")

                max_value = 0
                min_value = 0
                for i in dic_grafo:
                    if(len(dic_grafo[i]) >= max_value):
                        max_value = len(dic_grafo[i])
                    else:
                        aux_min = len(dic_grafo[i])
                        if(aux >= min_value):
                            min_value = aux_min

                arq.write('Menor componente conexo = ' + str(min_value) + '\n' + 'Maior componente conexo = ' + str(max_value) + '\n')
                arq.write('Componentes conexos do grafo = ' + str(dic_grafo)  + '\n')
                arq.close()
            # print('grafo = ', grafo)
        if(self.opcao == '2'):
            if (isconexo == True):
                componentes = self.bfs(1, False)

                arq.write('Menor componente conexo = ' + min(componentes) + '\n' + 'Maior componente conexo = ' + max(componentes) + '\n')
                arq.write('Componentes conexos do grafo = ' + len(componentes)  + '\n')
                arq.close()
            else:
                for i in range(self.vertices[0]):
                    if i not in visitados:
                        componentes = self.bfs(i, True)
                        # IMPRIMIR OS COMPONENTES CONEXOS, O MENOR,O MAIOR E A QUANTIDADE DE COMPONENTES CONEXOS
    # busca em largura 
    def bfs(self, vertice, returnTxt, verticeParada = None):

        if(self.opcao == '1'):
            queue  = [vertice]
            visitados = []
            level = {}
            level[vertice] = 0

            while queue:
                vertice = queue.pop(0)
                if vertice not in visitados:
                    visitados.append(vertice)

                    if verticeParada != None:
                        if vertice == verticeParada:
                            return visitados
                    
                    for i in self.grafo[vertice] :
                        if i not in visitados:
                            level[i] = level[vertice] + 1
                            queue.append(i)

            if(returnTxt == True):
                arq = open("../outputs/VerticesVisitados_BuscaEmLargura.txt", "a")
                arq.write('Vertices visitados = ' + str(visitados)  + '\n')
                arq.write('Nivel dos vertices = ' + str(level)  + '\n')
            else:
                return visitados

        if(self.opcao == '2'):
            #bsf para Matriz
            queue  = [vertice-1]
            visitados = []
            level = {}
            level[vertice] = 0

            while queue:
                vertice = queue.pop(0)
                if vertice+1 not in visitados:
                    visitados.append(vertice+1)
                    
                    for i in range(int(self.vertices[0])):
                        if self.grafo[vertice][i] != 0 and i+1 not in visitados:
                            level[i+1] = level[vertice+1] + 1
                            queue.append(i)
            if(returnTxt == True):
                arq = open("../outputs/VerticesVisitados_BuscaEmLarguraMatriz.txt", "a")
                arq.write('Vertices visitados = ' + str(visitados)  + '\n')
                arq.write('Nivel dos vertices = ' + str(level)  + '\n')
            else:
                return visitados

            # busca em profundidade
    def dfs(self, vertice):
        if(self.opcao == '1'):
            visitados = []
            stack = [vertice]
            level = {}
            level[vertice] = 0
            
            while stack:
                vertice = stack.pop()
                if vertice not in visitados:
                    visitados.append(vertice)
                    
                    for i in self.grafo[vertice]:
                        if i not in visitados:
                            stack.append(i)
                            level[i] = level[vertice] + 1
            
            arq = open("../outputs/VerticesVisitados_BuscaEmProfundidade.txt", "a")
            arq.write('Vertices visitados = ' + str(visitados)  + '\n')
            arq.write('Nivel dos vertices = ' + str(level)  + '\n')
        if(self.opcao == '2'):
            #dfs para Matriz
            visitados = []
            stack = [vertice-1]
            level = {}
            level[vertice] = 0
            
            while stack:
                vertice = stack.pop()
                if vertice+1 not in visitados:
                    visitados.append(vertice+1)
                    
                    for i in range(int(self.vertices[0])):
                        if self.grafo[vertice][i] != 0 and i+1 not in visitados:
                            stack.append(i)
                            level[i+1] = level[vertice+1] + 1
            
            arq = open("../outputs/VerticesVisitados_BuscaEmProfundidadeMatriz.txt", "a")
            arq.write('Vertices visitados = ' + str(visitados)  + '\n')
            arq.write('Nivel dos vertices = ' + str(level)  + '\n')

    def imprime_lista_de_adjacência(self, nome_arq):
        arq = open(nome_arq, "a")
        arq.write('Lista de adjacência = ' + str(self.grafo)  + '\n')
        arq.close()

    def dijkstra(self, vertice_inicial, vertice_destino):
        if(self.opcao == '1'):
            try:
                print("dijkstra_lista_adjacencia")
            
                af
            except:
                bsf = self.bfs(vertice_inicial, False, vertice_destino)
                print(bsf)
            

        if self.opcao == '2':
            if self.peso == True:
                tamanho_do_grafo = len(self.grafo)
                distancias = []
                distancias = [np.inf for i in range(tamanho_do_grafo)]
                distancias[vertice_inicial-1] = 0
                menor_caminho = { i: [] for i in range(1,len(self.grafo)+1) }
                menor_caminho[vertice_inicial] = [vertice_inicial]
                fechado = [False for i in range(tamanho_do_grafo)]
                visitados = []
                heapq.heappush(visitados, (0, vertice_inicial-1))

                while visitados:
                    
                    vertice = heapq.heappop(visitados)
                    vertice_atual = vertice[1]
                    fechado[vertice_atual] = True

                    for vertice_adjacente in range(tamanho_do_grafo):

                        if self.grafo[vertice_atual][vertice_adjacente] != 0:

                            if distancias[vertice_adjacente] == np.inf:
                                
                                distancias[vertice_adjacente] = distancias[vertice_atual] + self.grafo[vertice_atual][vertice_adjacente]
                                menor_caminho[vertice_adjacente+1] = menor_caminho[vertice_atual+1] + [vertice_adjacente+1]
                                heapq.heappush(visitados, (distancias[vertice_adjacente], vertice_adjacente))
                        
                           
                            if distancias[vertice_adjacente] != np.inf and fechado[vertice_adjacente] == False:

                                if distancias[vertice_adjacente] > distancias[vertice_atual] + self.grafo[vertice_atual][vertice_adjacente]:

                                    distancias[vertice_adjacente] = distancias[vertice_atual] + self.grafo[vertice_atual][vertice_adjacente]
                                    menor_caminho[vertice_adjacente+1] = menor_caminho[vertice_adjacente+1].clear()
                                    menor_caminho[vertice_adjacente+1] = menor_caminho[vertice_atual+1] + [vertice_adjacente+1]
                                    #exclui o vertice adjacente da lista de visitados para inserir com a nova distancia
                                    for i in range(len(visitados)):
                                        if visitados[i][1] == vertice_adjacente:
                                            visitados.pop(i)
                                            break
                                    heapq.heappush(visitados, (distancias[vertice_adjacente], vertice_adjacente))
                                    
                print("Menor caminho = ", menor_caminho)
                print("Distancias = ", distancias)
            else:
                bfs = self.bfs(vertice_inicial, False, vertice_destino)
                print("Caminho da busca em largura = ", bfs[0])

    #@profile
    def read_file(self, input_file):
        
        input = open(input_file, "r")
        if(self.opcao == '1'):
            for line in input:
                line = line.replace("\n", "")
                x = line.split(" ")
                selecionador = 0                
                try:
                    #Se for uma grafo com peso vai executar esse bloco
                    self.grafo[int(x[0])].append([int(x[1]), float(x[2])])
                    # self.grafo[int(x[0])].append([float(x[2])])
                    self.grafo[int(x[1])].append([int(x[0]), float(x[2])])
                    # self.grafo[int(x[1])].append([float(x[2])])
                
                except IndexError:
                    #se for um grafo sem peso vai executar esse bloco
                    self.grafo[int(x[0])].append(int(x[1]))
                    #if int(x[0]) not in self.grafo[int(x[1])]:
                    self.grafo[int(x[1])].append(int(x[0]))
                except:
                    #Esse bloco sempre vai ser executado na primeira linha do arquivo
                    self.vertices = int(x[0])
                    self.grafo = { i: [] for i in range(1 , self.vertices+1) }
                    pass
            print('Grafo = ', self.grafo)
        
        elif(self.opcao == '2'):
            lista = []
            for line in input:
                line = line.replace("\n", "")
                x = line.split(" ")
                lista.append(x)
            
            self.vertices = lista[0]
            del lista[0]

            # Criando a matriz com zeros 
            self.grafo = csr_matrix((int(self.vertices[0]), int(self.vertices[0])), dtype = float).toarray()
            #[[None for x in range(int(self.vertices[0])+1)] for y in range(int(self.vertices[0])+1)]
            
            try:
                self.peso = True
                #adicionando arestas com pesos 
                for i in lista:
                    if(float(i[2]) < 0):
                        self.peso = False
                        
                    self.grafo[int(i[0])-1][int(i[1])-1] = float(i[2])
                    self.grafo[int(i[1])-1][int(i[0])-1] = float(i[2])
            except:
                self.peso = False
                #adicionando arestas
                for i in lista:
                    self.grafo[int(i[0])-1][int(i[1])-1] = 1 
                    self.grafo[int(i[1])-1][int(i[0])-1] = 1
                    
            print(self.grafo)


if __name__ == "__main__":
    # programa de teste
    #nome_arq = "componentes_do_grafo_as_graph.txt"
    # nome_arq = "componentes_do_grafooooo.txt"

    g = Grafo("../grafos/teste.txt")
    # g.bfs(1,True)
    # g.dfs(1,True)

# nome_arq = "../componentes_conexos_as_graph.txt"
# g = Grafo("../collaboration_graph.txt")
    #g = Grafo("../grafos/as_graph.txt")
    #g = Grafo("../grafos/trab2grafo_1.txt")

    # g.dados()
####################################
# start = time.perf_counter()

# g.bfs(1)

# end = time.perf_counter()
# lista_time = []
# lista_time.append(end - start)
# print('lista_time = ', lista_time)
####################################
    # print("DFS")
    # g.dfs(1)
# g.conexo(nome_arq)
#g.dados(nome_arq)

############### dijkstra #####################
    #g = Grafo("../grafos/teste2_dijkstra.txt")
    g.dijkstra(1, 3)
    #g.dijkstra_lista_adjacencia(1, 3)
####################################
