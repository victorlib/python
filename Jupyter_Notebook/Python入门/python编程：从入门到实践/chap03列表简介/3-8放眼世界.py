places = ['ls拉萨', 'bj北京', 'sh上海', 'cq重庆', 'cd成都', 'hz杭州']
print('想要去的地方：')
print(places)
print('按字母排序：')
print(sorted(places))
print('上个用的是sorted()不会改变原列表')
print(places)
print('列表倒置：')
places.reverse()
print(places)
print('改变列表的排序')
places.sort()
print(places)


