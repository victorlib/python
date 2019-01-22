filename = "learning_python.txt"
with open(filename) as file_object:
    content = file_object.read()
    print(content)
print('------------------------------')
with open(filename) as file_object:
    for line in file_object:
        print(line)
print('------------------------------')
with open(filename) as file_object:
    lines = file_object.readlines()
for l in lines:
    print(l)
print('------------------------------')

