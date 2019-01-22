def show_magicians(names):
    """
    向列表中的每位魔术师都发出简单的问候
    """
    for name in names:
        msg = "Hello魔术师，" + name.title() + "!"
        print(msg)


usernames = ['hannah', 'ty', 'margot']
show_magicians(usernames)
