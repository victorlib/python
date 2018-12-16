
# -*- coding: utf-8 -*-  
import json
import re


str3 = r'([\u4e00-\u9fa5]+)\s+(.*)'
re_test = re.compile(str3)


list1 = []
list2 = []
f = open("example1.txt","r", encoding='utf-8')

lines = f.readlines()      #读取全部内容 ，并以列表方式返回
for line in lines:
    m = re_test.match(line)
    if m:
        #return m.group(1)+":"+m.group(2)
        list1.append(m.group(1).strip('\t'))
        list2.append(m.group(2).strip('\t'))

dic = dict(map(lambda x,y:[x,y],list1,list2))
print(dic)

rever_dic = dict(map(lambda x, y:[y,x], list1, list2))
print(rever_dic)

with open('1.json', 'w',  encoding='utf-8') as f:
    jsonstr = json.dumps(dic, ensure_ascii=False, indent=4,separators=(",", ":"))
    jsonstr2 = json.dumps(rever_dic, ensure_ascii=False, indent=4,separators=(",", ":"))
    #json.dump(dic,f)
    print(jsonstr)
    print(jsonstr2)

    

