#!/usr/bin/env python
# coding: utf-8

# # Minimum Spanning Tree
# ## Prim Algorithm

# In[1]:


from graphviz import Graph
import heapq as hq
import math


# In[2]:


def Prim(G):
    n = len(G)
    visited = [False]*n
    dist    = [math.inf]*n
    T       = [-1]*n
    dist[0] = 0
    pqueue  = []
    hq.heappush(pqueue, (0, 0)) # (weight, vertex)
    while len(pqueue) > 0:
        _, u = hq.heappop(pqueue)
        if visited[u]: continue
        visited[u] = True
        for v, w in G[u]:
            if not visited[v] and w < dist[v]:
                T[v] = u
                dist[v] = w
                hq.heappush(pqueue, (w, v))
    return T


# In[3]:


def Dot(T):
    n = len(T)
    dot = Graph()
    for i in range(n):
        dot.node(str(i))
    for i in range(n):
        if T[i] >= 0:
            dot.edge(str(i), str(T[i]))
    dot.graph_attr['rankdir'] = 'BT'
    return dot


# In[4]:


G = [[(1, 1), (2, 5)],
     [(0, 1), (4, 6), (5, 7)],
     [(0, 5), (3, 3), (4, 2)],
     [(2, 3), (4, 4), (5, 1)],
     [(1, 6), (2, 2), (3, 4), (5, 3)],
     [(1, 7), (3, 1), (4, 3)]]


# In[5]:


T = Prim(G)
print(T)
Dot(T)


# In[ ]:




