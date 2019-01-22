my_pizzas = ['披萨a', '披萨b', '披萨c']
friend_pizzas = my_pizzas[:]
my_pizzas.append('my pizza')
friend_pizzas.append('friend pizza')
print('my favorite pizza are:')
for pizza in my_pizzas:
    print(pizza)

print('\nmy friend\'s favorite pizza are:')
for pizza in friend_pizzas:
    print(pizza)
