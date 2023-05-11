"""
Multiplica duas matrizes

@author Ubiratan da SIlva Tavares

"""

def sao_multiplicaveis(matriz1, matriz2):
    """
    funcao que verifica se duas matrizes m1 e m2 são multiplicaveis.
    """
    colunas_m1 = len(matriz1[0])
    linhas_m2 = len(matriz2)
    if colunas_m1 == linhas_m2:
        return True
    return False

def produto(matriz1, matriz2):
    """
    funcao que retorna o produto das matrizes matriz1 e matriz2.
    """
    mult = []
    for linha, _ in enumerate(matriz1):
        mult.append([])
        for coluna, _ in enumerate(matriz2[0]):
            mult[linha].append(0)
            for k, _ in enumerate(matriz1[0]):
                mult[linha][coluna] += matriz1[linha][k] * matriz2[k][coluna]
    return mult

def imprime_matriz(matriz):
    """
    funcao que imprime uma matriz no console.
    """
    for linha in matriz:
        for i, _ in enumerate(linha):
            if i < (len(linha) - 1):
                print(linha[i], end=" ")
            else:
                print(linha[i], end="\n")

def main():
    """
    esta é a função principal
    """
    matriz1 = [[1, 2, 3], [4, 5, 6]]
    matriz2 = [[2, 3, 4], [5, 6, 7]]
    if sao_multiplicaveis(matriz1, matriz2):
        prod = produto(matriz1, matriz2)
        imprime_matriz(prod)

    matriz1 = [[1], [2], [3]]
    matriz2 = [[2, 3, 4]]
    if sao_multiplicaveis(matriz1, matriz2):
        prod = produto(matriz1, matriz2)
        imprime_matriz(prod)


if __name__ == "__main__":
    main()
