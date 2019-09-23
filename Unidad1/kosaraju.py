#!/usr/bin/env python
# coding: utf-8

# # Strongly connected components

# In[8]:


import heapq as hq

def kosaraju(G):
    n = len(G)
    
    # 1. grafo reverso
    Grev = [[] for _ in range(n)]
    for u in range(n):
        for v in G[u]:
            Grev[v].append(u)
            
    # 2. dfs para encontrar F
    d = [None]*n
    f = []
    cc = [0]
    
    def dfs1(u):
        cc[0] += 1
        d[u] = cc[0]
        for v in Grev[u]:
            if d[v] == None:
                dfs1(v)
        cc[0] += 1
        hq.heappush(f, (-cc[0], u))
        
    for u in range(n):
        if d[u] == None:
            dfs1(u)
            
    # 3. dfs para los scc
    visited = [False]*n
    scc = []
    
    def dfs2(u, comps):
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                dfs2(v, comps)
        comps.append(u)
        
    while len(f) > 0:
        _, u = hq.heappop(f)
        if not visited[u]:
            comps = []
            dfs2(u, comps)
            scc.append(comps)
    
    return scc


# In[9]:


G = [[2, 4],
     [0, 2],
     [4, 5],
     [5, 7],
     [],
     [1, 7],
     [2, 4, 5],
     [6],]


# In[10]:


kosaraju(G)


# In[13]:


G = [[2],
     [0],
     [1, 6],
     [],
     [6],
     [3, 7],
     [5],
     [],]


# In[14]:


kosaraju(G)


# In[ ]:




