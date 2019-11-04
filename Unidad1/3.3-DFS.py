#!/usr/bin/env python
# coding: utf-8

# In[12]:


def dfs(G, s):
    n = len(G)
    path = [None]*n
    visited = [False]*n
    stack = [s]
    while len(stack) > 0:
        u = stack.pop()
        if visited[u]: continue
        visited[u] = True
        for v in reversed(G[u]):
            if not visited[v]:
                stack.append(v)
                path[v] = u
    return path


# In[13]:


G = [[3],
     [3],
     [],
     [5, 7],
     [6],
     [6, 7],
     [2, 4, 7],
     []]


# In[14]:


dfs(G, 0)


# In[23]:


def dfs(G, s):
    n = len(G)
    path = [None]*n
    visited = [False]*n
    
    def dfs_r(G, u):
        if not visited[u]:
            visited[u] = True
            for v in G[u]:
                if not visited[v]:
                    path[v] = u
                    dfs_r(G, v)
                
    dfs_r(G, s)
    return path


# In[24]:


dfs(G, 0)


# In[ ]:




