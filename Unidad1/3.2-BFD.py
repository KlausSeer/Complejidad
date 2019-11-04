#!/usr/bin/env python
# coding: utf-8

# In[4]:


def bfs(G, s):
    n = len(G)
    path = [None]*n
    visited = [False]*n
    queue = [s]
    visited[s] = True
    while len(queue) > 0:
        u = queue[0]
        queue = queue[1:]
        for v in G[u]:
            if not visited[v]:
                queue.append(v)
                path[v] = u
                visited[v] = True
    return path


# In[2]:


G = [[3],
     [3],
     [],
     [5, 7],
     [6],
     [6, 7],
     [2, 4, 7],
     []]


# In[5]:


bfs(G, 0)


# In[ ]:




