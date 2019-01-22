likeNums = {
    'man1': [50, 64, 21],
    'man2': [10, 64, 21],
    'man3': [40, 64, 21],
    'man4': [150, 64, 21],
    'man5': [110, 64, 21],
    'man6': [2140, 64, 21],
}
for man, numbers in likeNums.items():
    print(man + ' like number are:')
    for num in numbers:
        print(num)
    print()



