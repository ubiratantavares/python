"""
Exercício 2: Matrizes multiplicáveis

Duas matrizes são multiplicáveis se o número de colunas da primeira 
é igual ao número de linhas da segunda. Escreva a função sao_multiplicaveis(m1, m2) 
que recebe duas matrizes como parâmetro e devolve True se as matrizes forem multiplicavéis 
(na ordem dada) e False caso contrário.

Exemplos:

m1 = [[1, 2, 3], [4, 5, 6]]
m2 = [[2, 3, 4], [5, 6, 7]]
sao_multiplicaveis(m1, m2) => False

m1 = [[1], [2], [3]]
m2 = [[1, 2, 3]]
sao_multiplicaveis(m1, m2) => True

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
