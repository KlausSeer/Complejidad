#!/usr/bin/env python
# coding: utf-8

# In[6]:


def stringmatch(t, p):
    l = len(p)
    n = len(t)
    resultados = []
    for i in range(n):
        match = True
        for j in range(l):
            if t[i + j] != p[j]:
                match = False
                break
        if match:
            resultados.append(i)
    return resultados


# In[8]:


stringmatch("abracadabracalamazoo", "rac")


# In[ ]:




