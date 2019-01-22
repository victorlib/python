sandwich_orders = ['三明治a', '三明治b', '三明治c']
finished_sandwiches = []
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print('I made your '+sandwich+' sandwich ')
    finished_sandwiches.append(sandwich)

print('所有三明治已经完成')
print(finished_sandwiches)

