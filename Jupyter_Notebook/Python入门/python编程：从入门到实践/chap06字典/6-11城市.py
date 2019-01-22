cities = {
    'hangzhou': {
        'country': 'china',
        'population': 1700,
        'fact': '互联网城市'
    },
    'chongqing': {
        'country': 'china',
        'population': 4700,
        'fact': '重庆火锅'
    },
    'shanghai': {
        'country': 'china',
        'population': 2700,
        'fact': '国际大都市'
    }
}
for name, val in cities.items():
    print(name.title())
    for k, v in val.items():
        print(k+':'+str(v))
    print()