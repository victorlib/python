nums = [i for i in range(1, 10)]

for i in nums:
    if i is 1:
        print(str(i)+'st')
    elif i is 2:
        print(str(i)+'nd')
    elif i is 3:
        print(str(i)+'rd')
    else:
        print(str(i)+'th')