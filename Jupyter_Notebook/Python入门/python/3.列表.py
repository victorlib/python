
# coding: utf-8

# In[13]:


bicycles=['trek', 'redline', 'specialized']
print(bicycles[0].title())
print(bicycles[-1])  
print(bicycles[-3])
bicycles[0] = 'liwenxing'
print(bicycles)
print(bicycles)


# In[9]:


bicycles.append('end')
print(bicycles)


# In[14]:


bicycles.insert(0, 'first')
print(bicycles)


# In[19]:


peoples = ['liwenxing1', 'liwenxing2', 'liwenxing3']
peoples.insert(0, 'liwenxing0')
peoples.insert(2,'liwenxingmid')
peoples.append('liwenxingend')
print(peoples)


# In[20]:


peoples = ['liwenxing0', 'liwenxing1', 'liwenxingmid',
           'liwenxing2', 'liwenxing3', 'liwenxingend']
i = 0
while i<4:
    name_pop = peoples.pop()
    message = "Sorry, " + name_pop + " I can't invite you to have dinner"
    print(message)
    i = i+1

for people in peoples:
    message = people + ", you can still have dinner."
    print(message)

del(peoples[0])
del(peoples[0])
print(peoples)
print("I can only invite two people to have dinner")

