
# coding: utf-8

# In[15]:


import json

file_name = "Contorl_Access"
with open(file_name+".txt") as f:
    dict = json.load(f)
    for key in dict:
        print('map_array_[2][_T("'+key+'")]'+'='+'_T("'+dict[key]+'");')

