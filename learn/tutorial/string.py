# -*- coding:utf-8 -*-

print('We are the {} who say "{}!"'.format('knights', 'Ni'))
print('{0} and {1}'.format('spam', 'eggs'))
print('{1} and {0}'.format('spam', 'eggs'))
print('This {food} is {adjective}.'.format(
    food = 'spam', adjective = 'absolutely horrible'))
print('The story of {0}, {1} and {other}.'.format('Bill', 'Manfred',
    other = 'Georg'))

for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x**2, x**3))

print('12'.zfill(5))
print('-3.14'.zfill(7))
print('3.1415926'.zfill(5))
print('3.1315926'.ljust(5)[:5])
print('3.1315926'.ljust(5))

def GetMiddleStr(content,startStr,endStr):
  startIndex = content.index(startStr)
  if startIndex>=0:
    startIndex += len(startStr)
  endIndex = content.index(endStr)
  return content[startIndex:endIndex]

# print(GetMiddleStr('<div class="a">jb51.net</div>','<div class="a">','</div>'))
# print(GetMiddleStr('    _T("liwenxing")', '_T("', '")'))

import re
string = '_T("liwenxing("ll")(sdf)s")'
p1 = re.compile(r'[(](.*?)[)]', re.S) #最小匹配
p2 = re.compile(r'[(](.*)[)]', re.S)  #贪婪匹配
print(re.findall(p1, string))
print(re.findall(p2, string))
