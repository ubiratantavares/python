# 1.3.1 Dynamic Typing

L = [1, 2, 3]

M = [1, 2, 3]

print(L == M)

print(L is M)

print(id(L))

print(id(M))

print(id(L) == id(M))

L = [1, 2, 3]

M = L

print(M is L)

M = list(L)

print(M is L)

print(M == L)

M = L[:]

print(M)

# 1.3.3: Statements

x, y = 10, 5

if x > y:
    difference = x - y
    print("x is greater than y")
print("But this gets printed no matter what!")


# 1.3.4: For and While Loops

for x in range(10):
    print(x, end=" ")

names = ['Jim', 'Tom', 'Nick', 'Pam', 'Sam', 'Tim']

print("\n")
for name in names:
    print(name, end=" ")

print("\n")
for i in range(len(names)):
    print(names[i], end=" ")

age = {'Jim': 31, 'Nick': 31, 'Pam': 27, 'Sam': 35, 'Tim': 31, 'Tom':50}

print("\n")
print(age.keys())

print("\n")
for name in age.keys():
    print(name, age[name])

print("\n")
for name in age:
    print(name, age[name])

print("\n")
for name in sorted(age.keys()):
    print(name, age[name])

print("\n")
for name in sorted(age.keys(), reverse=True):
    print(name, age[name])


# 1.3.5: List Comprehensions

numbers = range(10)

squares = []

for number in numbers:
    squares.append(number**2)

print(squares)

squares = [number**2 for number in numbers]

print(squares)

squares = [number**2 for number in range(15)]
print(squares)

# 1.3.6: Reading and Writing Files

filename = "1.txt"

for line in open(filename, encoding="utf-8"):
    print(line)

for line in open(filename, encoding="utf-8"):
    line = line.rstrip()
    print(line)

for line in open(filename, encoding="utf-8"):
    line = line.rstrip().split(" ")
    print(line)

F = open("output.txt", "w", encoding="utf-8")
F.write("Python\n")
F.close()

F = open("input.txt", "w", encoding="utf-8")
F.write("Hello\nWorld")
F.close()
lines = []
for line in open("input.txt", encoding="utf-8"):
    lines.append(line.strip())
print(lines)

# 1.3.7: Introduction to Functions

def add(a, b):
    return a + b

print(add(12, 15))

def add_and_sub(a, b):
    return (a+b, a-b)

print(add_and_sub(12, 15))

print(add)

new_add = add

print(new_add(2, 3))

#def modify(mylist):
#    mylist[0] *= 10

L = [1, 3, 5, 7, 9]

#print(modify(L))

print(L)

def modify(mylist):
    mylist[0] *= 10
    return mylist

L = [1, 3, 5, 7, 9]

M = modify(L)

print(M is L)

# 1.3.8: Writing Simple Functions

def intersect(lista1, lista2):
    res = []
    for j in lista1:
        if j in lista2:
            res.append(j)
    return res

print(intersect([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]))

from random import choice
from string import ascii_letters, digits 

# gerador de senhas
def password(length):
    senha = str()
    characters = ascii_letters + digits + "!@#$%&*"
    for _ in range(length):
        senha += choice(characters)
    return senha

print(password(12))

def is_vowel(letter):
    if type(letter) == int:
        letter = str(letter)
    if letter in "aeiouy":
        return True
    return False

print(is_vowel(4))


def factorial(numero):
    if numero == 0:
        return 1
    else:
        num = 1
        for idx in range(1, numero + 1):
            num *= idx
        return(num)

print(factorial(5))
