# -*- conding:utf-8 -*-

MLB_team = {
     'Colorado' : 'Rockies',
     'Boston'   : 'Red Sox',
     'Minnesota': 'Twins',
     'Milwaukee': 'Brewers',
     'Seattle'  : 'Mariners'
     }

print(MLB_team)

MLB_dict = dict([
    ('a', '1'),
    ('b', '2'),
    ('c', '3'),
    ('d', '4')
    ])
print(MLB_dict)

MLB_dict2 = dict(
        a = 1,
        b = 2,
        c = 3,
        d = 4
        )
print(MLB_dict2)
print(type(MLB_dict2))
print(MLB_dict2.get('ab', 'Vincent'))
print(list(MLB_dict2.items()))
print(MLB_dict2.keys())
print(MLB_dict2.values())
MLB_dict2.pop('a')
print(MLB_dict2)

print(dir(MLB_dict2))
print(help(MLB_dict2))






















































