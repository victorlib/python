# -*- coding:utf-8 -*-
import sys
import numpy as np

captains = ['Janeway', 'Picard', 'Sisko']

for captain in captains:
    print(captain)


numbers_divisible_by_three = [3, 6, 9, 12, 15]

for num in numbers_divisible_by_three:
    quotient = num / 3;
    print("{} divided by 3 is {}.".format(num, int(quotient)))

for i in range(3, 16, 3):
    quotient = i / 3
    print("{} diveded by 3 is {}.".format(i, int(quotient)))

# range(stop)
# When you call range() with one argument, you will get a series of numbers 
# that starts at 0 and includes every whole number up to, but not including,
# the number you have provided as the stop.

for i in range(3):
    print(i)

# range(start, stop)
# When you call range() with two arguments, you get to decide not only where 
# the series of numbers stops but also where it starts, so you don’t have to
# start at 0 all the time. You can use range() to generate a series of
# numbers from A to B using a range(A, B). Let’s find out how to generate
# a range starting at 1.

for i in range(1, 8):
    print(i)

# range(start, stop, step)
# When you call range() with three arguments, you can choose not only where the
# series of numbers will start and stop but also how big the difference will be 
# between one number and the next. If you don’t provide a step, then range() 
# will automatically behave as if the step is 1.

for i in range(3, 16, 3):
    quotient = i / 3
print("{} divided by 3 is {}".format(i, int(quotient)))


# incrementing with rang()

for i in range(3, 100, 25):
    print(i)


# decrementing with range()

for i in range(10, -6, -2):
    print(i)

for i in reversed(range(5)):
    print(i)


print(type(range(3)))
print(range(3)[1])
print(range(3)[2])


for i in np.arange(100, 500, 30):
    print(i)

for i in np.linspace(100, 500, 35):
    print(i)































