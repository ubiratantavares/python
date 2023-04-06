# Erros de Sintaxe

x = 10
y = 5
print(x + y)

if x == 3:
    print('x é igual à 3')
    print('fim do bloco de código')

# Erros em Tempo de Execução

a = 1000
print(a)
b = 0
print(b)
#c = a / b
#print(c)

cidade = 'Belo Horizonte'
print(cidade)
estado = 'Minas Gerais'
print(estado)
#print(cidade, estado, pais)

cidade = 'Belo Horizonte'
print(cidade)

#1estado = 'Minas Gerais'
#print(1estado)
#print(cidade, 1estado, pais)

# Erros Lógicosb

x = 5.0
y = 7.0
z = 12.0
media = x + y + z / 3
#media = 5 + 7 + 12 / 3
#media = 5 + 7 + 4 = 16
print(media)

x = 5.0
y = 7.0
z = 12.0
media = (x + y + z) / 3
print(media)