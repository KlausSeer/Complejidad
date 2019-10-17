#!/usr/bin/env python
# coding: utf-8

# In[22]:


def crib(N):
    c = [i for i in range(0, N)]
    c[0], c[1] = None, None
    for i in range(N):
        if c[i] != None:
            for j in range(i + i, N, i):
                c[j] = None
            yield c[i]
        i += 1


# In[24]:


primos100 = crib(100)
print(primos100)
for item in primos100:
    print(item)


# In[25]:


def generador():
    for i in range(10, ):
        yield i


# In[26]:


for num in generador():
    print(num)


# In[ ]:




