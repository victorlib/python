# -*- coding: utf-8 -*-
def triangle(n):
    L = [1]
    while True:
        yield L
        L.append(0)
        L = [L
                [i-1] + L[i] for i in range(len(L))]

n = 0
for t in triangle(10):
    print(t)
    n = n + 1
    if 10 == n:
        break


import math
import sys
from sys import *
print(version)
print(executable)

if __name__ == '__main__':
    print('main')
else:
    print('not main')



