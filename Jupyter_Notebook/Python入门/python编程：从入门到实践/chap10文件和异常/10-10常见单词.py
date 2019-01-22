ext = '.txt'
files = ["Fighting Germany's Spies", "Aunt Jo's Scrap-Bag, Volume 4", "My Day by Sara Rice Pryor"]
for file in files:
    with open(file+ext, encoding='utf8') as file_obj:
        content = file_obj.read()
        print('the单词在《'+file+'》书籍中出现'+str(content.lower().count('the'))+'次。')
