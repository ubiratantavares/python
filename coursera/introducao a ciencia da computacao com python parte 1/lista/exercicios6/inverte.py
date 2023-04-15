"""
Exercício 2 - Invertendo sequência
Como pedido na primeira video-aula desta semana, 
escreva um programa que recebe uma sequência de números 
inteiros e imprima todos os valores em ordem inversa. 
A sequência sempre termina pelo número 0. Note que 0 (ZERO) não deve fazer parte da sequência.

Exemplo:

Digite um número: 1
Digite um número: 7
Digite um número: 4
Digite um número: 0

4
7
1

"""

def ler_numero(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            pass

def inverter_lista(lista):
    aux = []
    for i in range(len(lista)-1, -1, -1):
        aux.append(lista[i])
    return aux

def imprimir_lista(lista):
    for item in lista:
        print(item)

def main():
    lista = []
    numero = ler_numero("Digite um número: ")
    while numero != 0:
        lista.append(numero)
        numero = ler_numero("Digite um número: ")
    nova_lista = inverter_lista(lista)
    print("\n")
    imprimir_lista(nova_lista)


if __name__ == "__main__":
    main()
