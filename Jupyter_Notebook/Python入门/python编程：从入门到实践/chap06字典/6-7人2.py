people1 = {
    'first_name': 'chen',
    'last_name': 'jiasheng',
    'age': 22,
    'city': 'zhaoqing'
}
people2 = {
    'first_name': 'zhang',
    'last_name': 'san',
    'age': 21,
    'city': 'hangzhou'
}
people3 = {
    'first_name': 'li',
    'last_name': 'si',
    'age': 32,
    'city': 'chongqing'
}
people = [people1, people2, people3]

for p in people:
    for k, v in p.items():
        print(k+':'+str(v))
    print()