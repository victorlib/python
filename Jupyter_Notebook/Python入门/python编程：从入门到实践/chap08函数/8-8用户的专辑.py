def make_album(singer, album):
    return {
        'singer': singer,
        'album': album
    }


while True:
    print("\n请告诉我歌手名和专辑名:")
    print("(任何时候按'q'退出)")
    singer = input("歌手名: ")
    if singer == 'q':
        break
    album = input("专辑名: ")
    if album == 'q':
        break
    a = make_album(singer, album)
    print('\n'+str(a))

