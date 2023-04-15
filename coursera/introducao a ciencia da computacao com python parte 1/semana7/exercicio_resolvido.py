def fatorial(n):
    fat = 1
    while n > 1:
        fat*= n
        n -= 1
    return fat           


def ler_numero():
    while True:
        try:
            return int(input("Digite um número inteiro: "))
        except ValueError:
            pass


def validar_numero(n):
    if n >= 0:
        return True
    return False


def imprimir_fatorial(n):
    print(f"{n}! = {fatorial(n)}")


def main():
    n = ler_numero()
    while validar_numero(n):
        imprimir_fatorial(n)
        n = ler_numero()


if __name__ == "__main__":
    main()
