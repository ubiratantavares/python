# 1.1.2 - objects
from numpy import array

x = array([1, 3, 5])

y = array([1, 5, 9])

print(x.mean())

print(y.mean())

print(x.shape)

print(y.shape)

# 1.1.3 - modules and methods
from math import pi, sqrt, sin

print(pi)

print(sqrt(10))

print(pi/2)

print(sin(pi/2))

from numpy import sqrt

print(type(sqrt))

print(sqrt(2))

print(sqrt([2, 3, 4, 5]))

name = "Amy"

print(type(name))

#print(dir(name))

#print(help(name.upper))

#print(name.upper)

print(name.upper())

#help(name.upper())


#  1.1.4 - numbers and basic calculations

print(123 + 34)

print(123 * 34)

print(123 ** 34)

print(123 ** 346)

print(6 / 7)

print(15 / 7)

print(15 // 7)

print(15 / 2.3)

# print(_ * 2.3)

print(10 * 2)

# print(_ + 5)

# print(_ ** 2)

from math import factorial

print(factorial(3))

# 1.1.5: Random Choice

from random import choice

print(choice([2, 44, 55, 66]))

print(choice(['aa', 'bb', 'cc', 'dd']))

print(choice((1, 2, 3, 4, 5)))

# 1.1.6: Expressions and Booleans

print(type(True))

print(type(False))

print(True or False)

print(True and True)

print(True and False)

print(not True)

print(not False)

print(2 < 4)

print(2 <= 2)

print(2 == 2)

print(2 != 2)

print([2, 3] == [3, 3])

print([2, 3] == [2, 3])

print([2, 3] is [2, 3])
