/*Faça em C/C++ um programa que construa uma matriz de adjacência a partir de informações fornecidas pelo usuário (qtde. de vértices, qtde. de arestas, arestas, ou seja, os vértices que definem cada aresta). Considerem os vértices como números.*/
#include <iostream>
using namespace std;

void printMatrixAdjacent(int** matrix, int numeroVertices);
int** insertMatrixAdjacent(int** matrix, int numeroVertices, int numeroArestas);
int** inicializeMatrixAdjacent(int** matrix, int numeroVertices);

int main()
{
    int i = 0;
    int j = 0;
    int numeroVertices = 0;
    int numeroArestas = 0;
    
    int n, m, i, j, k, l;
    cout << "Digite o numero de vertices: ";
    cin >> numeroVertices;
    cout << "Digite o numero de arestas: ";
    cin >> numeroArestas;
    
    int matriz[numeroVertices][numeroVertices];
    
    inicializeMatrixAdjacent(matriz, numeroVertices);
    insertMatrixAdjacent(matriz, numeroVertices, numeroArestas);
    printMatrixAdjacent(matriz, numeroVertices);
    return 0;
}

int** inicializeMatrixAdjacent(int** matrix, int numeroVertices) {
    for (i = 0; i < numeroVertices; i++){
        for (j = 0; j < numeroVertices; j++)
        {
            matriz[i][j] = 0;
        }
    }
    
    return matrix;
}

int** insertMatrixAdjacent(int** matrix, int numeroVertices, int numeroArestas) {
    int i = 0;
    int verticeOrigem = 0;
    int verticeDestino = 0;
    for (i = 0; i < numeroArestas; i++)
    {
        cout << "Digite o vertice de origem: ";
        cin >> verticeOrigem;
        cout << "Digite o vertice de destino: ";
        cin >> verticeDestino;
        matriz[verticeOrigem][verticeDestino] = 1;
        matriz[verticeDestino][verticeOrigem] = 1;
    }
    
    return matrix;
}

void printMatrixAdjacent(int** matrix, int numeroVertices) {
    for (i = 0; i < numeroVertices; i++) {
        for (j = 0; j < numeroVertices; j++)
        {
            cout << matriz[i][j] << " ";
        }
        cout << endl;
    }
}
