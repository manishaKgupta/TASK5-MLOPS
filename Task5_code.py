#!/usr/bin/env python
# coding: utf-8

# In[17]:


import pandas as pd
import numpy as np
dataset=pd.read_csv('db.csv')
dataset.columns = ['IP','status']
status=dataset['status']
IP=dataset['IP']
data = dataset.values
type(data)
IP_set= []
for i in data:
    if i[1]==404:
        IP_set.append(i[0])
Ip = np.array(IP_set)
from collections import Counter
c = Counter(IP_set)
Block_IP=[]
for i in c:
    if c[i]>=3:
        Block_IP.append(i)
arr = np.array(Block_IP)
with open("Block_ip_file.txt", "w") as f:
    for s in Block_IP:
        f.write(str(s) +"\n")


# In[ ]:




