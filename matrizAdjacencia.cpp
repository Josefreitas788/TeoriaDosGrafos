/*Faça em C/C++ um programa que construa uma matriz de adjacência a partir de informações fornecidas pelo usuário (qtde. de vértices, qtde. de arestas, arestas, ou seja, os vértices que definem cada aresta). Considerem os vértices como números.*/
#include <iostream>
#include <stdlib.h>
using namespace std;
int main()
{
    int n, m, i, j, k, l;
    cout << "Digite o numero de vertices: ";
    cin >> n;
    cout << "Digite o numero de arestas: ";
    cin >> m;
    int matriz[n][n];
    for (i = 0; i < n; i++)
    {
        for (j = 0; j < n; j++)
        {
            matriz[i][j] = 0;
        }
    }
    for (k = 0; k < m; k++)
    {
        cout << "Digite o vertice de origem: ";
        cin >> i;
        cout << "Digite o vertice de destino: ";
        cin >> j;
        matriz[i][j] = 1;
        matriz[j][i] = 1;
    }
    for (i = 0; i < n; i++)
    {
        for (j = 0; j < n; j++)
        {
            cout << matriz[i][j] << " ";
        }
        cout << endl;
    }
    return 0;
}
