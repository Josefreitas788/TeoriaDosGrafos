# import numpy as np
import time
# https://www.ime.usp.br/~pf/algoritmos_para_grafos/aulas/components.html#:~:text=Uma%20componente%20conexa%20(%3D%20connected,subgrafo%20conexo%20maximal%20do%20grafo.
#from memory_profiler import profile
class Grafo:

    
    def __init__(self, input_file):

        self.opcao = int(input("\nDigite o tipo de representação desejada:\n 1 - Lista de adjacência\n 2 - Matriz de adjacência\n"))
        self.read_file(input_file)
        

    # número de vértices, número de arestas, grau de cada vértice.
    def dados(self, nome_arq):
        if(self.opcao == '1'):
            arq = open(nome_arq, "a")
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

    def conexo(self, nome_arq):
        if(self.opcao == '1'):
            self.cc = [] 
            visitados = self.dfs(1, False)
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

    # busca em largura 
    def bfs(self, vertice):

        queue  = [vertice]
        visitados = []
        level = {}
        level[vertice] = 0

        while queue:
            vertice = queue.pop(0)
            if vertice not in visitados:
                visitados.append(vertice)
                
                for i in self.grafo[vertice] :
                    if i not in visitados:
                        level[i] = level[vertice] + 1
                        queue.append(i)

        
        arq = open("VerticesVisitados_BuscaEmLargura.txt", "a")
        arq.write('Vertices visitados = ' + str(visitados)  + '\n')
        arq.write('Nivel dos vertices = ' + str(level)  + '\n')

    # busca em profundidade
    def dfs(self, vertice):
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
        
        arq = open("VerticesVisitados_BuscaEmProfundidade.txt", "a")
        arq.write('Vertices visitados = ' + str(visitados)  + '\n')
        arq.write('Nivel dos vertices = ' + str(level)  + '\n')

    def imprime_lista_de_adjacência(self, nome_arq):
        arq = open(nome_arq, "a")
        arq.write('Lista de adjacência = ' + str(self.grafo)  + '\n')
        arq.close()


    #@profile
    def read_file(self, input_file):
        
        input = open(input_file, "r")
        if(self.opcao == '1'):
            for line in input:
                x = line.split(" ")
                try:
                    x[1] = x[1].replace("\n", "")
                    self.grafo[int(x[0])].append(int(x[1]))
                    if int(x[0]) not in self.grafo[int(x[1])]:
                        self.grafo[int(x[1])].append(int(x[0]))
                except:
                    self.vertices = int(x[0])
                    self.grafo = { i: [] for i in range(1 , self.vertices+1) }
                    pass
        
        else:
            lista = []
            for line in input:
                line = line.replace("\n", "")
                x = line.split(" ")
                lista.append(x)
            
            self.vertices = lista[0]
            del lista[0]

            # Criando a matriz com zeros 
            self.grafomatriz = [[None for i in range(int(self.vertices[0]))] for j in range(int(self.vertices[0]))]
            
            #adicionando arestas
            for i in lista:
                self.inserir_aresta(int(i[0]),int(i[1]))
                self.grafomatriz[i[0]][int(i[1])] = 1
                self.grafomatriz[int(i[1])][int(i[0])] = 1
            
            print(self.grafomatriz)


if __name__ == "__main__":
    # programa de teste
    #nome_arq = "componentes_do_grafo_as_graph.txt"
    # nome_arq = "componentes_do_grafooooo.txt"
    # g = Grafo("../teste2.txt")
# nome_arq = "../componentes_conexos_as_graph.txt"
# g = Grafo("../collaboration_graph.txt")
    g = Grafo("../as_graph.txt")

    # g.dados()
    # print("BFS")
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

