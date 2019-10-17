#!/usr/bin/env python
# coding: utf-8

# In[5]:


import heapq as hq
import math


# In[28]:


def ucs(G, s, t):
    n = len(G)
    visited = [False]*n
    weight  = [math.inf]*n
    path    = [None]*n
    queue   = []
    
    hq.heappush(queue, (0, s))
    weight[s] = 0
    
    while len(queue) > 0:
        g, u = hq.heappop(queue)
        if visited[u]:
            continue
        if u == t:
            break
        visited[u] = True
        for v, w in G[u]:
            if not visited[v]:
                f = g + w
                if f < weight[v]:
                    weight[v] = f
                    path[v]   = u
                    hq.heappush(queue, (f, v))
                    
    return path, weight


# In[34]:


G = [[(3, 10), (4, 1)],
     [(3, 5), (4, 5)],
     [(3, 4), (4, 15)],
     [(0, 10), (1, 5), (2, 4)],
     [(0, 1), (1, 5), (2, 15)]]


# In[35]:


path, weights = ucs(G, 4, 3)
names = ['A', 'B', 'C', 'G', 'S']


# In[26]:


last = 3
while last != None:
    print(names[last])
    last = path[last]


# In[27]:


print(path, weights)


# In[36]:


print(path, weights)


# In[ ]:




