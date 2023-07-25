tel = {'jack': 4098, 'sape': 4139}

# adding a new key, value pair
tel['guido'] = 4127

# deleting a kv pair
del tel['sape']

tel['irv'] = 4127

s = list(tel)
print(s)

sorted(tel)

'guido' in tel

'jack' not in tel


# dict function
p = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print(p)

# dict comprehensions
r = {x: x ** 2 for x in (2, 4, 6)}
print(r)

# another use of dict
e = dict(sape=4139, guido=4127, jack=4098)
print(e)

# when looping through dictionaries, the key and the corresponding value can be retrieved at the same time using the items() method

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i+1, v)

# zip()
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print("What is your {0}: {1}".format(q, a))

print()
for i in reversed(range(2, 10, 2)):
    print(i)
print()
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for i in sorted(basket):
    print(i)
print()
for i in sorted(set(basket)):
    print(i)

import math

raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []

for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)

print(filtered_data)

sum = lambda x, y:  x+y
print(sum(10, 5))

values = (1, 2, 3, 4, 5)

def fahrenheit(T):
    return ((float(9)/5)*T + 32)

def celsius(T):
    return (float(5)/9)*(T-32)


temperatures = (36.5, 37, 37.5, 38, 39)
temperatures_in_fahr = list(map(fahrenheit, temperatures))
temperatures_in_cels = list(map(celsius, temperatures_in_fahr))
print(temperatures_in_fahr)
print(temperatures_in_cels)

C = [39.2, 36.5, 37.3, 38, 37.8]
F = list(map(lambda x: (float(9)/5)*x + 32, C))
print(F)

C2 = list(map(lambda x: (float(5)/9)*(x-32), F))
print(C2)

a = [1, 2, 3, 4]
b = [17, 12, 11, 10]
c = [-1, -4, 5, 9]

print(list(map(lambda x, y, z: x+y+z, a, b, c)))
print(list(map(lambda x, y: x+y, a, b)))
print(list(map(lambda x, y, z: 2.5*x + 2*y - z, a, b, c)))

# mapping a list of functions
from math import sin , cos, tan, pi
def map_functions(x, functions):
    res = []
    for func in functions:
        res.append(func(x))
    return res
family_of_functions = (sin, cos, tan)
print(map_functions(pi, family_of_functions))