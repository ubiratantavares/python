"""
Exercício 1
Escreva um programa que recebe como entradas (utilize a função input) 
dois números inteiros correspondentes à largura e à altura de um retângulo, respectivamente. 

O programa deve imprimir, usando repetições encaixadas (laços aninhados), 
uma cadeia de caracteres que represente o retângulo informado com caracteres '#' na saída.

Por exemplo:

digite a largura: 10
digite a altura: 3
##########
##########
##########


digite a largura: 2
digite a altura: 2
##
##


Dica: lembre-se que a função print pode receber um parametro 'end', 
que altera o último caractere da cadeia, tornando possível a remoção da quebra de linha (reveja as vídeo-aulas)

"""

def ler_numero(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            pass

def imprimir_retangulo(altura, largura):
    for i in range(altura):
        for j in range(largura):
            print("#", end="")
        print("")

def main():
    largura = ler_numero("digite a largura: ")
    altura = ler_numero("digite a altura: ")
    imprimir_retangulo(altura, largura)


if __name__ == "__main__":
    main()
