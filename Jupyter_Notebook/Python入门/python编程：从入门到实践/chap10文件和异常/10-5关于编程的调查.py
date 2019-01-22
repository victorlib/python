file_object = open('why_like_program.txt', 'a', encoding='utf8')
while True:
    reason = input('为什么喜欢编程？(输入q退出)')
    if reason == 'q':
        break
    file_object.write(reason+'\n')
file_object.close()
