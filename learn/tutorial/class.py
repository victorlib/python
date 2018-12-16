# -*- coding:utf-8 -*-

def scope_test():
    def do_local():
        spam = 'local spam'

    def do_nonlocal():
        nonlocal spam
        spam = 'nonlocal spam'

    def do_global():
        global spam
        spam = 'global spam'

    spam = 'test spam'
    do_local()
    print('After local assignment:', spam)
    do_nonlocal()
    print('After nonlocal assignment:', spam)
    do_global()
    print('After global assginment:', spam)

scope_test()
print('In global scope:', spam)


class Dog:

    kind = 'canine'     # class variable shared by all instances

    def __init__(self, name):
        self.name = name  # instance variable unique to each instance
        tricks = []


    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')
print(d.kind)
print(d.name)
print(d)
d.add_trick('roll over')
print(d.tricks)




























