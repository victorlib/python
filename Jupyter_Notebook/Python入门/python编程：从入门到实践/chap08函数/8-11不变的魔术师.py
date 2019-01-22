def show_magicians(names):
    """
    向列表中的每位魔术师都发出简单的问候
    """
    for name in names:
        msg = "Hello魔术师，" + name.title() + "!"
        print(msg)


def make_great(names):
    """
    为列表中的每位魔术师名字前加上the Great
    """
    for i in range(0, len(names)):
        names[i] = 'the Great ' + names[i]
    return names


a = ['hannah', 'ty', 'margot']
b = make_great(a[:])
show_magicians(a)
show_magicians(b)

