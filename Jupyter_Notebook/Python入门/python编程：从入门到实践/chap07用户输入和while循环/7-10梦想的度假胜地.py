responses = {}

while True:
    name = input('\nwhat\'t your name?')
    response = input('If you could visit one place in the world, where would you go?')
    responses[name] = response

    flag = input('Would you like to let another person respond? (yes/ no) ')
    if flag == 'no':
        break

print('\n-----------result--------------')
for name, response in responses.items():
    print(name + ' would like visit ' + response + '.')

