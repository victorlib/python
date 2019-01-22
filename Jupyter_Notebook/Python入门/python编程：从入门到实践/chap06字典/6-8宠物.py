wangcai = {
    'type': 'dog',
    'owner': '小张'
}
xiaoduo = {
    'type': 'dog',
    'owner': 'anjaxs'
}
xiaomei = {
    'type': 'cat',
    'owner': '翠花'
}
pets = [wangcai, xiaoduo, xiaomei]
for pet in pets:
    for k, v in pet.items():
        print(k+':'+v)
    print()