"""
@author Ubiratan da Silva Tavares
"""


def temperatura_minima(temperaturas):
    """
    retorna a temperatura minima do mês.
    """
    minima = temperaturas[0]
    i = 1
    while i < len(temperaturas):
        if temperaturas[i] < minima:
            minima = temperaturas[i]
        i += 1
    return minima


def temperatura_maxima(temperaturas):
    """
    retorna a temperatura máxima do mês.
    """
    maxima = temperaturas[0]
    i = 1
    while i < len(temperaturas):
        if temperaturas[i] > maxima:
            maxima = temperaturas[i]
        i += 1
    return maxima


def imprimir_temperatura(mensagem):
    """
    imprime uma mensagem com uma temperatura.
    """
    print(mensagem)



def main():
    """
    define a função principal.
    """
    temperaturas = [30, 27, 25, 26, 29, 31,
                    32, 33, 30, 29, 24, 26,
                    30, 27, 24, 25, 26, 24,
                    22, 23, 25, 25, 28, 28,
                    32, 32, 31, 29, 28, 31, 33]
    imprimir_temperatura(f"A temperatura máxima do mês foi {temperatura_maxima(temperaturas)} ºC.")
    imprimir_temperatura(f"A temperatura mínima do mês foi {temperatura_minima(temperaturas)} ºC.")


if __name__ == "__main__":
    main()
