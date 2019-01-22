favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
people = ['jen', 'jiasheng', 'anjaxs', 'phil']

for name in favorite_languages.keys():
    if name in people:
        print('感谢'+name.title()+'，你已经参加过问卷调查了。')
    else:
        print('邀请'+name.title()+'，你来参加调查')