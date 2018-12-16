
# coding: utf-8

# In[2]:


import os.path

def read_into_buffer(filename):
    buf = bytearray(os.path.getsize(filename))
    with open(filename, 'rb') as f:
        f.readinto(buf)
    return buf



# In[5]:


# Write a simple file
with open('sample.bin', 'wb') as f:
    f.write(b'Hello World')

buf = read_into_buffer('sample.bin')
print(buf)


# In[6]:


buf[0:5]


# In[7]:


with open('newsample.bin', 'wb') as f:
    f.write(buf)


# ### 5.11 文件路径名的操作

# In[2]:


import os
path = '/Users/beazley/Data/data.csv'


# In[14]:


# Get the last component of the path
os.path.basename(path)


# In[15]:


# Get the directory name
os.path.dirname(path)


# In[16]:


# Join path cpmponents together
os.path.join('tmp', 'data', os.path.basename(path))


# In[4]:


# Expand the user's home directory
path = '~/Data/data.csv'
os.path.expanduser(path)


# In[7]:


# Split the file extension
os.path.splitext(path)


# 对于任何的文件名的操作，你都应该使用os.path 模块，而不是使用标准字符串
# 操作来构造自己的代码。特别是为了可移植性考虑的时候更应如此，因为os.path 模
# 块知道Unix 和Windows 系统之间的差异并且能够可靠地处理类似Data/data.csv 和
# Data\data.csv 这样的文件名。其次，你真的不应该浪费时间去重复造轮子。通常最好
# 是直接使用已经为你准备好的功能。

# ### 5.12 测试文件是否存在

# In[10]:


import os
os.path.exists('/etc/passwd')
os.path.exists('data')


# ### 你还能进一步测试这个文件时什么类型的。在下面这些测试中，如果测试的文件不存在的时候，结果都会返回False：

# In[11]:


# Is a regular file
os.path.isfile('/etc/passwd')


# In[12]:


# Is a directory
os.path.isdir('data')


# In[15]:


# Is a symbolic link
os.path.islink('usr/local/bin/python3')


# In[16]:


# Get the file linked to
os.path.realpath('/usr/local/bin/python3')


# In[17]:


os.path.getsize('data')


# In[18]:


os.path.getmtime('data')


# In[19]:


import time
time.ctime(os.path.getmtime('data'))


# 使用os.path 来进行文件测试是很简单的。在写这些脚本时，可能唯一需要注意
# 的就是你需要考虑文件权限的问题，特别是在获取元数据时候。比如：
