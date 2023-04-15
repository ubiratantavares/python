"""
Exercício 2
Refaça o exercício 1 imprimindo os retângulos sem preenchimento, de forma que os caracteres que não estiverem na borda do retângulo sejam espaços.

Por exemplo:

digite a largura: 10
digite a altura: 3
##########
#        #
##########


digite a largura: 2
digite a altura: 2
##
##

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
            if i == 0 or i == altura - 1:
                print("#", end="")
            else:
                if j == 0 or j == largura - 1:
                    print("#", end="")
                else:
                    print(" ", end="")
        print("")

def main():
    largura = ler_numero("digite a largura: ")
    altura = ler_numero("digite a altura: ")
    imprimir_retangulo(altura, largura)


if __name__ == "__main__":
    main()
