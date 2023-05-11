"""
@ author Ubiratan da Silva Tavares

"""


def criar(num_linhas, num_colunas):
    """
    retorna uma matriz com num_linhas linhas e num_colunas colunas
    em que cada elemento da matriz é igual ao valor dado.    
    """
    matriz = []
    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            valor = int(input(f"Digite o valor do elemento ({i+1}, {j+1}): "))
            linha.append(valor)
        matriz.append(linha)
    return matriz

def ler():
    """
    funcao que le os elementos de uma matriz com n linhas e m colunas
    """
    linhas = int(input("Digite o número de linhas da matriz: "))
    colunas = int(input("Digite o número de colunas da matriz: "))
    return criar(linhas, colunas)


def imprimir(matriz):
    """
    funcao que imprime uma matriz no console.
    """
    for linha in matriz:
        for valor in linha:
            print(valor, end=" ")
        print("")


def main():
    """
    definição da função principal
    """
    matriz = ler()
    imprimir(matriz)


if __name__ == "__main__":
    main()
