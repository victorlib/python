while True:
    age = int(input('你的年龄是：'))
    if age < 3:
        print('不用钱')
    elif age <= 12:
        print('10美元')
    else:
        print('15美元')
