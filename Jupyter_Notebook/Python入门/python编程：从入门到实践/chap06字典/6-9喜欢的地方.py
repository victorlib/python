favorite_places = {
    '小张': ['墨西哥', '美国', '英国'],
    '小美': ['加拿大', '中国'],
    '小强': ['印度']
}
for name, places in favorite_places.items():
    print(name+'喜欢的地方有：')
    for place in places:
        print(place)
    print()
