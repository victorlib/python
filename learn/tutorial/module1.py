# -*- coding:utf-8 -*-

import builtins
import fibo

result1 = fibo.fib(1000)
result2 = fibo.fib2(100)
print(result1)
print(result2)
print(dir(fibo))
print(dir(builtins))

# rw file

#with open('workfile.txt') as f:
#    read_data = f.read()
f = open('workfile.txt')
for line  in f:
    print(line, end='')

