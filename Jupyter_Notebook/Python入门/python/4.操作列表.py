
# coding: utf-8

# In[1]:


magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)


# In[4]:


magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I cant't wait to see.\n")

print("Thnak you , everyone, That was a greate magic show!")


# In[6]:


even_numbers = list(range(2,11,3))
print(even_numbers)


# In[11]:


squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
    
    #print(square)
min(squares)
max(squares)
sum(squares)


# In[12]:


nums = [num**2 for num in range(1,11)]
print(nums)


# In[15]:


for i in range(1,21):
    #print(i)


# In[14]:


nums = [num for num in range(1, 1000000)]
sum(nums)


# In[18]:


vs = [v**3 for v in range(1,11)]
print(vs)


# In[20]:


print(vs[-3:])


# In[22]:


my_foods = ['pizza', 'falafel', 'carrot caek']
friend_foods = my_foods[:]
my_foods[0] = 'banana'
print(my_foods)
print(friend_foods)

