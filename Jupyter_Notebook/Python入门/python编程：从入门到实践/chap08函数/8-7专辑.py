def make_album(singer, album, time=0):
    a = {
        'singer': singer,
        'album': album
    }
    if time:
        a['time'] = time
    return a


b = make_album('周杰伦', '夜的第七章')
print(b)
c = make_album('林俊杰', '专辑a')
print(c)
d = make_album('李四', '专辑b', 50)
print(d)




