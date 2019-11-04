#!/usr/bin/env python
# coding: utf-8

# # Minimum Spanning Tree
# ## Kruskal Algorithm

# In[1]:


from graphviz import Graph
import heapq as hq
import math


# In[2]:


class Disjointset:
    def __init__(self, n):
        self.N = n
        self.D = [-1 for _ in range(n)]

    def Find(self, x):
        if self.D[x] < 0: return x
        else:
            self.D[x] = self.Find(self.D[x])
            return self.D[x]
    
    def Union(self, a, b):
        pa, pb = self.Find(a), self.Find(b)
        if self.D[pa] < self.D[pb]:
            self.D[pa] += self.D[pb]
            self.D[pb] = pa
        else:
            self.D[pb] += self.D[pa]
            self.D[pa] = pb
            
    def IsSameSet(self, a, b):
        return self.Find(a) == self.Find(b)


# In[3]:


def Kruskal(G):
    n = len(G)
    E = []
    for u in range(n):
        for v, w in G[u]:
            hq.heappush(E, (w, u, v))
            
    ds = Disjointset(n)
    T = [-1]*n
    while n > 1:
        _, u, v = hq.heappop(E)
        if not ds.IsSameSet(u, v):
            ds.Union(u, v)
            T[v] = u
            n -= 1
    return T


# In[4]:


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


# In[5]:


G = [[(1, 1), (2, 5)],
     [(0, 1), (4, 6), (5, 7)],
     [(0, 5), (3, 3), (4, 2)],
     [(2, 3), (4, 4), (5, 1)],
     [(1, 6), (2, 2), (3, 4), (5, 3)],
     [(1, 7), (3, 1), (4, 3)]]


# In[6]:


T = Kruskal(G)
print(T)
Dot(T)


# In[ ]:




