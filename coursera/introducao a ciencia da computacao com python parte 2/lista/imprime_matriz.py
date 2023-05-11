"""
Exercício 1: Imprimindo matrizes

Como proposto na primeira vídeo-aula da semana, escreva uma função imprime_matriz(matriz), 
que recebe uma matriz como parâmetro e imprime a matriz, linha por linha. 
Note que NÃO se deve imprimir espaços após o último elemento de cada linha!

Exemplos:

minha_matriz = [[1], [2], [3]]
imprime_matriz(minha_matriz)
1
2
3

minha_matriz = [[1, 2, 3], [4, 5, 6]]
imprime_matriz(minha_matriz)
1 2 3
4 5 6

"""

def imprime_matriz(matriz):
    """
    funcao que imprime uma matriz no console.
    """
    for linha in matriz:
        for i in enumerate(linha):
            if i < (len(linha) - 1):
                print(linha[i], end=" ")
            else:
                print(linha[i], end="\n")
