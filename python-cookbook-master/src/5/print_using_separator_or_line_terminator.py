
# coding: utf-8

# In[1]:


print('ACME', 50, 91.5)


# In[2]:


print('ACME', 50, 91.5, sep=',')


# In[3]:


print('ACME', 50, 91.5, sep=',', end='!!\n')


# In[5]:


# 使用end 参数也可以在输出中禁止换行。比如：
for i in range(5):
    print(i, end=' ')


# 当你想使用非空格分隔符来输出数据的时候，给print() 函数传递一个sep 参数
# 是最简单的方案。有时候你会看到一些程序员会使用str.join() 来完成同样的事情。
# 比如：

# In[7]:


print(','.join(('ACME', '50', '91.5')))


# In[11]:


# str.join() 的问题在于它仅仅适用于字符串。这意味着你通常需要执行另外一些转换才能让它正常工作。比如：
row = ('ACME', 50, 91.5)
#print(','.join(row))  #error
print(','.join(str(x) for x in row))
print(*row, sep=',')

