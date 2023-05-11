"""
Escreva uma função que recebe um array de strings como parâmetro e devolve
o primeiro string na ordem lexicográfica, ignorando-se letras maiúsculas e minúsculas
"""

def primeiro_elemento(lista):
    """
    esta funcao recebe uma array de strings e devolve o primeiro string na ordem lexicográfica.
    """
    primeiro = lista[0].strip().lower()
    idx = 1
    while idx < len(lista):
        if lista[idx].strip().lower() < primeiro:
            primeiro = lista[idx].strip().lower()
        idx += 1
    return primeiro
