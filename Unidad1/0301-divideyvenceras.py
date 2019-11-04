#!/usr/bin/env python
# coding: utf-8

# In[1]:


def findmax(arr):
    n = len(arr)
    if n == 1:
        return arr[0]
    else:
        m = n // 2
        max1 = findmax(arr[:m])
        max2 = findmax(arr[m:])
        return max1 if max1 > max2 else max2


# In[2]:


import random as rnd


# In[3]:


arr = [rnd.randint(1, 100) for _ in range(10)]
print(arr)
print(findmax(arr))


# In[4]:


n = 10
10**n


# In[ ]:




