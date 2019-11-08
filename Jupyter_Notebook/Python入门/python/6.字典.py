
# coding: utf-8

# In[2]:


people = {
    'first_name':'chen',
    'last_name':'jiasheng',
    'age':'22',
    'city':'zhaoqing'
    }
print(people['first_name'].title() + ' ' + people['last_name'])
print('age is '+str(people['age']))
print('from '+people['city'])


# In[3]:


likeNums = {
    'man1':50,
    'man2':110,
    'man3':20,
    'man4':70,
    'man5':60
}
for man in likeNums:
    print(man + ' like number ' + str(likeNums[man]))


# In[5]:


words = {
    'apple':'苹果',
    'banana':'香蕉',
    'red':'红色',
    'blue':'蓝色',
    'peopel':'人'
}

for k,v in words.items():
    print(''+k+':'+v)
    
for k in words.keys():
    print(k)


# In[2]:


alien_0 = {'color':'green', 'points':5}
alien_1 = {'color':'yellow', 'points':10}
alien_2 = {'color':'red','points':15}

aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)


# #### 6-7

# In[5]:


people1 = {
    'first_name':'chen',
    'last_name':'jiasheng',
    'age':22,
    'city':'zhaoqing'
}
people2 = {
    'first_name':'zhang',
    'last_name':'san',
    'age':21,
    'city':'hangzhou'
}
people3 = {
    'first_name':'li',
    'last_name':'si',
    'age':32,
    'city':'chongqing'
}
peoples = [people1, people2, people3]

for p in peoples:
    for k, v in p.items():
        print(k+':'+str(v))
    print()


# #### 6-8

# In[7]:


wangcai = {
    'type':'dog',
    'owner':'县长'
}
xiaoduo = {
    'type':'dog',
    'owner':'anjasx'
}
xiaomei = {
    'type':'cat',
    'owner':'翠花'
}

pets = [wangcai, xiaoduo, xiaomei]
for pet in pets:
    for k,v in pet.items():
        print(k+':'+v)
    print()


# #### 6-9

# In[9]:


favorite_places = {
    'xiaozhang':['mexicro', 'us', 'england'],
    'xiaomei':['canada', 'china'],
    'xiaoqiang':['indian']
}
for name, places in favorite_places.items():
    print(name+'喜欢的地方有: ')
    for place in places:
        print(place)
    print()


# #### 6-10

# In[10]:


likeNums = {
    'man1':[20, 123,122],
    'man2':[123,134,145],
    'man3':[16,98,90,56,123],
    'man4':[46,23,57],
    'man5':[97,26,18]
}
for man, nums in likeNums.items():
    print(man + 'like nums: ')
    for num in nums:
        print(num)
    print()


# In[12]:


citys = {
    'hangzhou':{
        'country':'china',
        'population':1700,
        'fact':'internet'
    },
    'chongqing':{
        'country':'China',
        'population':4700,
        'fact':'huoguo'
    },
    'shanghai':{
        'country':'China',
        'population':2700,
        'fact':'big city'
    }
}

for name,val in citys.items():
    print(name.title())
    for k,v in val.items():
        print(k+':'+str(v))
    print()

