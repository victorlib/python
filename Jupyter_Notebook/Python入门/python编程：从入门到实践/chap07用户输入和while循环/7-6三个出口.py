active = 10
while active > 0:
    print(active)
    active -= 1
    if active % 2 == 0:
        continue


    cmd = input('输入你的命令：')
    if cmd == 'quit':
        break


