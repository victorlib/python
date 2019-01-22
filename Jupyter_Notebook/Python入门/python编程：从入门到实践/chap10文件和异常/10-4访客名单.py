file_object = open('guest_book.txt', 'a')
while True:
    name = input('输入你的姓名：(输入q退出)')
    if name == 'q':
        break
    file_object.write('Hello, '+name+'\n')
file_object.close()
