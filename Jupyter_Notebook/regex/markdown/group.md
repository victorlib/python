

```python
def trim(s):
      if s[:1] !=' ' and s[-1:] !=' ':
          return s
      elif s[:1] ==' ':
          return trim(s[1:])
      else:
          return trim(s[:-1])

f2 = open('data2.txt', 'r')
data = f2.readlines()
list1 = []
list2 = []
for line in data:
    last = line.split('=')
    if last:
        str1 = last[0].replace('\n', '')
        str2 = last[1].replace('\n', '')
        str1 = str1.replace(" ", "")
        str2 = str2.replace(" ", "")
        list1.append(str1)
        list2.append(str2)

print(list1)
print(list2)

f = open('data1.txt', 'r')
f2 = open('data3.txt', 'w')


data = f.readlines()
f.close()

for line in data:
    kwrite = True
    for index in range(len(list2)):
        if list2[index] in line:
            line = line.replace(list2[index], 'pointer->'+list1[index])
            print(line)
            f2.write(line)
            kwrite = False
    if (kwrite):
        f2.write(line)
        


```

    ['sa[0]', 'sa[1]', 'sa[2]', 'sa[3]']
    ['_T("liwenxing")', '_T("111")', '_T("2222")', '_T("333")']
    


```python

f2.close()

```

    sdfasfs =pointer->sa[0];
    
