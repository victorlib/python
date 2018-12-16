

```python
import json
data = {'name' : 'ACME', 'shares' : 100, 'pirce' : 542.23}
json_str = json.dumps(data)
print(json_str)
```

    {"name": "ACME", "shares": 100, "pirce": 542.23}
    

如果你试着去检查JSON 解码后的数据，你通常很难通过简单的打印来确定它
的结构，特别是当数据的嵌套结构层次很深或者包含大量的字段时。为了解决这个问
题，可以考虑使用pprint 模块的pprint() 函数来代替普通的print() 函数。它会按
照key 的字母顺序并以一种更加美观的方式输出。下面是一个演示如何漂亮的打印输
出Twitter 上搜索结果的例子：


```python
import json
import codecs

data = {'name':'李文星', 'shares':100, 'price':542.23}
json_str = json.dumps(data, ensure_ascii=False, indent = 4)
print(json_str)


# Writing Chinese
path = open('chinese.json', 'w', encoding='gb18030')
path.write(json_str)
path.close()

# Writing JSON data
with open('data.json', 'w') as f:
    json.dump(data, f)

# Reading data back
with open('data.json', 'r') as f:
    data = json.load(f)





```

    {
        "name": "李文星",
        "shares": 100,
        "price": 542.23
    }
    

如果你试着去检查JSON 解码后的数据，你通常很难通过简单的打印来确定它
的结构，特别是当数据的嵌套结构层次很深或者包含大量的字段时。为了解决这个问
题，可以考虑使用pprint 模块的pprint() 函数来代替普通的print() 函数。它会按
照key 的字母顺序并以一种更加美观的方式输出。下面是一个演示如何漂亮的打印输
出Twitter 上搜索结果的例子：


```python

#from urllib.request import urlopen
#u = urlopen('http://search.twitter.com/search.json?q=python&rpp=5')
#resp = json.loads(u.read().decode('utf-8'))
#from pprint import pprint
#print(resp)
```

下面是如何将一个JSON 字典转换为一个Python 对象例子：


```python
s = '{"name":"ACME", "shares":100, "price":490.1}'
from collections import OrderedDict
data = json.loads(s, object_pairs_hook=OrderedDict)
print(data)

# 下面是如何将一个JSON 字典转换为一个Python 对象例子：
class JSONObject:
    def __init__(self, d):
        self.__dict__ = d

data = json.loads(s, object_hook=JSONObject)
print(data.name)
data.shares
data.price
```

    OrderedDict([('name', 'ACME'), ('shares', 100), ('price', 490.1)])
    ACME
    




    490.1



最后一个例子中，JSON 解码后的字典作为一个单个参数传递给__init__() 。然
后，你就可以随心所欲的使用它了，比如作为一个实例字典来直接使用它。
在编码JSON 的时候，还有一些选项很有用。如果你想获得漂亮的格式化字符串
后输出，可以


```python
data = {"name": "ACME", "shares": 50, "price": 490.1}
print(json.dumps(data, indent=4))
```

    {
        "name": "ACME",
        "shares": 50,
        "price": 490.1
    }
    

对象实例通常并不是JSON 可序列化的。例如：


```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(2, 3)
json.dumps(p)
```
