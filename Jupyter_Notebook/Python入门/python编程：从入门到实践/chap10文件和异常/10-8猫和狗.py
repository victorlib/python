try:
    files = ['cats.txt', 'dogs.txt']
    for file in files:
        with open(file, encoding='utf8') as file_res:
            content = file_res.read()
            print(content)
except FileNotFoundError:
    print('文件不存在')
