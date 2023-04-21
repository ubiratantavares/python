# 1.2.2: Lists

print((1, 2, 3)[-0:0])

numbers = [2, 3, 6, 8]
print(numbers[0])
print(numbers[1])
print(numbers[-1])

numbers.append(10)
print(numbers)

x = [12, 14, 16]
print(numbers + x)

numbers = [1, 3, 5, 7, 11, 13, 17, 19, 23]
print(numbers.reverse())

print(numbers)

names = ['Zofia', 'Alex', 'Morgan', 'Anthony']
print(names.sort())
print(names)
print(names.reverse())
print(names)

sorted_names = sorted(names)
print(names)
print(sorted_names)

sorted_names = sorted(names, reverse=True)
print(sorted_names)
print(len(names))


# 1.2.3: Tuples

T = (1, 3, 5, 7)

print(T.count(3))

print(type(2, ))

print(len(T))

print(T + (9, 11))

print(T[1])

x = 12.23

y = 23.34

coordinate = (x, y)

print(type(coordinate))

(c1, c2) = coordinate

print(c1)

print(c2)

coordinates = [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25), (6, 36), (7, 49), (8, 64), (9, 81)]

print(coordinates)

for (x, y) in coordinates:
  print(x, y)

c = (2, 3)

print(c)

c = (2)

print(type(c))

c = 2,

print(type(c))

# 1.2.4: Ranges

range(5)

list(range(5))

list(range(1, 6))

list(range(1, 13, 2))

# 1.2.5: Strings

S = "Python"

len(S)

S[0]

S[-1]

S[0:3]

S[-3:]

"y" in S

12 + 12

"hello" + "world"

S * 3

"eight equals " + str(8)

dir(str)

#str.replace?

name = "Tina Fey"

name.replace("T", "t")

new_name = name.replace("T", "t")
new_name

name

names = name.split(" ")

type(names)

len(names)

names

type(names[0])

names[0].upper()

names[1].lower()


# 1.2.6: Sets

ids = set()

ids = set([1, 2, 4, 6, 7, 8, 9])

print(len(ids))

ids.add(10)

print(ids)

ids.add(2)

print(ids.pop())

print(ids.pop())

print(ids)

ids = set(range(10))
print(ids)

males = set([1, 3, 4, 6, 7])

females  = ids - males
print(females)

everyone = males | females
print(everyone)

print(everyone & set([1, 2, 3]))

word = "antidisestablishmentarianism"

letters = set(word)

print(len(letters))


# 1.2.7: Dictionaries

age = {}

age  = dict()

age = {"Tim": 29, "Jim": 31, "Pam": 27, "Sam": 35}

print(age["Pam"])

age["Tim"] = age["Tim"] + 1

age["Tim"] += 1

print(age["Tim"])

names = age.keys()

print(type(names))

print(names)

age["Tom"] = 50

print(names)

ages = age.values()
print(ages)

age["Nick"] = 31

print(names)

print("Tom" in age)

print("Zofia" in age)
