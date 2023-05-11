"""
Escrever uma função que recebe uma lista de Strings
contendo nomes de pessoas como parâmetro e devolve o nome mais curto.
A função deve ignorar espaços antes e depois do nome e deve devolver 
o nome "capitalizando", i.e., apenas
com a 1a letra maiúscula.
"""

def mais_curto(lista_de_nomes):
    """
    funcao que recebe uma lista de nomes e devolve o nome mais curto.
    """
    idx_menor = 0
    menor_tamanho = len(lista_de_nomes[idx_menor].strip())
    idx = 1
    while idx < len(lista_de_nomes):
        tamanho = len(lista_de_nomes[idx].strip())
        if tamanho < menor_tamanho:
            menor_tamanho = tamanho
            idx_menor = idx
        idx += 1
    return lista_de_nomes[idx_menor].strip().capitalize()
