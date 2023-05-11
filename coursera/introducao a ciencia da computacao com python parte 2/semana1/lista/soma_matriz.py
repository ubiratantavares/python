"""
Exercício 2: Soma de matrizes
Escreva a função soma_matrizes(m1, m2) que recebe 2 matrizes e devolve uma matriz que 
represente sua soma caso as matrizes tenham dimensões iguais. 
Caso contrário, a função deve devolver False.

Exemplos:

m1 = [[1, 2, 3], [4, 5, 6]]
m2 = [[2, 3, 4], [5, 6, 7]]
soma_matrizes(m1, m2) => [[3, 5, 7], [9, 11, 13]]

m1 = [[1], [2], [3]]
m2 = [[2, 3, 4], [5, 6, 7]]
soma_matrizes(m1, m2) => False

"""

def verifica_dimensoes(matriz1, matriz2):
    """
    esta função retorna True se as dimensoes das matrizes matriz1 e matriz2 são idênticas, 
    caso contrário, retorna False.
    """
    if (len(matriz1) == len(matriz2)) and (len(matriz1[0]) == len(matriz2[0])):
        return True
    return False


def soma_matrizes(matriz1, matriz2):
    """
    esta função retorna a soma das matrizes matriz1 e matriz2 se possuirem dimensões idênticas, 
    caso contrário retorna False
    """
    if verifica_dimensoes(matriz1, matriz2):
        soma = []
        for i, _ in enumerate(matriz1):
            linha = []
            for j, _ in enumerate(matriz1[0]):
                linha.append(matriz1[i][j]+matriz2[i][j])
            soma.append(linha)
        return soma
    return False


def main():
    """
    esta é a função principal
    """
    matriz1 = [[1, 2, 3], [4, 5, 6]]
    matriz2 = [[2, 3, 4], [5, 6, 7]]
    print(soma_matrizes(matriz1, matriz2))

    matriz1 = [[1], [2], [3]]
    matriz2 = [[2, 3, 4], [5, 6, 7]]
    print(soma_matrizes(matriz1, matriz2))


if __name__ == "__main__":
    main()
