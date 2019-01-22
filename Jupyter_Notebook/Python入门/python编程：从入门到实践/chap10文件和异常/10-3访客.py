name = input('输入你的姓名')
with open('guest.txt', 'w') as file_object:
    file_object.write(name)
