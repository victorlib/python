while True:
    print("请输入两个整数")
    try:
        num1 = input('输入第一个数：')
        num2 = input('输入第二个数：')
        print(num1+'+'+num2+'='+str(int(num1)+int(num2)))
    except ValueError:
        print('请确保两个都是整数')








