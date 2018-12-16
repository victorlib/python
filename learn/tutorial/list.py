# -*- coding:utf-8 -*-
from collections import deque
from math import pi

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits.count('apple'))
print(fruits.index('apple'))

print(fruits)
# -*- coding:utf-8 -*-
from collections import deque
from math import pi

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits.count('apple'))
print(fruits.index('apple'))

print(fruits)
fruits.reverse()
print(fruits)
fruits.sort()
print(fruits.pop())

# deque
queue = deque(['Eric', 'John', 'Michael'])
queue.append('Terry')
queue.append('graham')
print(queue.popleft())
print(queue.popleft())
print(queue)


# list 
squares = []
for x in range(10):
    squares.append(x**2)

print(squares)

squares = list(map(lambda x: x**2, range(10)))
squares = [x**2 for x in range(10)]
squares = [(x,y) for x in range(3) for y in range(4)]
print(squares)


print([4*x + x*y for x in range(3) for y in range(4)])

print([str(round(pi, i)) for i in range(1, 6)])


matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
   
        ]
row = []
row = [[row[i] for row in matrix] for i in range(4)]
print(row)

zr = list(zip(*matrix))
print(zr)


basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)

'orange' in basket  # True
'crabgrass' in basket  # False

a = set('abracadabra')
b = set('alacazam')
print(a)
print(b)
print(a - b)  # {'r', 'b', 'd'}
print(a | b)
print(a & b)  # {'a', 'c'}
print(a ^ b)

c = {x for x in 'abcdefg' if x not in 'abc'}
print(c)

# dictionary

dic = dict(sape = 4139, guido = 4127, jack = 4098)
print(dic)

for k, v in dic.items():
    print(k, v)

for i, v in enumerate(dic.items()):
    print(i, v)

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

for i in reversed(range(1, 10, 2)):
    print(i)

import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)

print(filtered_data)




