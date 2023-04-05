# define o valor do limiar
limiar = 5

menores = []
maiores = []

# divide os numeros de 1 a 10 em maiores e menores
for i in range(10):
    if i < limiar:
        menores.append(i)
    else:
        maiores.append(i)

# imprime na tela os valores das listas
print('menores:', menores)
print('maiores:', maiores)
