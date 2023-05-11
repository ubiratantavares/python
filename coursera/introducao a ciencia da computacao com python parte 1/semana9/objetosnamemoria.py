a = "banana"
b = "banana"
c = "maça"


print(a is b)

print(a is c)

a = [81, 82, 83]
b = [81, 82, 83]

print(a is b)

print(a == b)

# repeticoes e referencias
origlist = [45, 76, 4, 55]

print(origlist * 3)

print([origlist] * 3)

newlist = [origlist] * 3

print(origlist)

origlist[1] = 99

print(origlist)

print(newlist)

lista1 = ["carro", "ônibus", "barco", "bicicleta"]
lista2 = ["carro", "ônibus", "barco", "bicicleta"]
lista3 = ["carro", "barco"]

print(lista1 is lista2)
print(lista2 == lista1)
print(lista1 is lista3)


lista1 = ["carro", "barco"]
print(lista1)

lista2 = lista1
print(lista2)

lista3 = [lista1] * 3
print(lista3)

lista4 = lista1 * 3
print(lista4)

lista1 = ["carro", "barco"]
print(lista1)

lista2 = [["carro", "barco"], ["carro", "barco"], ["carro", "barco"]]
print(lista2)

lista3 = ["carro", "barco", "carro", "barco", "carro", "barco"]
print(lista3)

lista1[1] = "metrô"
print(lista1)

print(lista2)

print(lista3)

print("-------------------------------------------------------------------")

lista1 = ["carro", "barco"]
lista2 = [lista1] * 3
lista3 = lista1 * 3
lista1[1] = "metrô"
print(lista1)
print(lista2)
print(lista3)



