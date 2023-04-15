from conta_primos import n_primos


def ler_numero(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            pass

def main():
    n = ler_numero("Digite um numero: ")    
    while n < 2:
        n = ler_numero("Digite um numero: ")
    contador = n_primos(n)
    print(contador)

if __name__ == "__main__":
    main()