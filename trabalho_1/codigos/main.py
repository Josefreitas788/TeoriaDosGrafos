import random
from grafo import Grafo
from matriz_de_adjacencia import GrafoAdjacente

#Menu do programa
while True:
    print('\n*****Biblioteca para manipular grafos*****\n')

    # Ler um grafo de um arquivo texto
    # nome do arquivo
    nome_arq = input('Digite o nome do arquivo de entrada .txt que deve estar localizado dentro da pasta "trabalho1" (Ex: teste.txt) \n')
    Rep_grafos = int(input('Escolha a representação a ser utilizada\n1 - Matriz de adjacência\n2 - Lista de adjacência\n0 - Sair\n'))

    # Grafo.teste("../"+ nome_arq)
    # Grafo.dados("../"+ nome_arq)

    g = Grafo("../"+ nome_arq)
    g.dados("../res_"+ nome_arq)
    g.conexo("../componentes_conexos_"+ nome_arq)
   
    # Matriz de adjacência
    if Rep_grafos == 1:
        matriz = GrafoAdjacente("../"+ nome_arq)
        matriz.write_matriz("../matriz_de_adjacência_"+ nome_arq)
    # Lista de adjacência
    elif Rep_grafos == 2:
        g.imprime_lista_de_adjacência("../lista_de_adjacência_"+ nome_arq)
        print('Lista de adjacência')
    elif Rep_grafos == 0:
        break
    else:
        print('\nOpção inválida!!\nTente novamente.')
     
    print(f'\n*****Saída do programa*****\n1 - res_{nome_arq} retornou o numero de vertices, numero de arestas e o grau de cada vertice.\n2 - componentes_conexos_{nome_arq} retornou o numero de componentes conexas o tamanho (em vertices?) de cada componente e a lista de vertices pertencentes a componente....')
