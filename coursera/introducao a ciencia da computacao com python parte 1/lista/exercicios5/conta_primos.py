"""
Exercício 1 - Primos

Escreva a função n_primos que recebe como argumento um número inteiro maior ou igual a 2 
como parâmetro e devolve a quantidade de números primos que existem entre 2 e n (incluindo 2 e, se for o caso, n).

>>>n_primos(2)
1
>>>n_primos(4)
2
>>>n_primos(121)
30
"""

def ehPrimo(n):
    fator = 2
    if n == 2:
        return True
    while n % fator != 0 and fator <= n/2:
        fator += 1
    if n % fator == 0:
        return False
    else:
        return True

def n_primos(n):
    contador = 0
    for i in range(2, n+1):
        if ehPrimo(i):
            contador += 1
    return contador
