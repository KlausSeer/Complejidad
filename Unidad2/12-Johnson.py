#!/usr/bin/env python
# coding: utf-8

# # Johnson

# In[1]:


import math
import heapq as hq


# In[2]:


def bellmanFord(G, s):
    n = len(G)
    d = [math.inf]*n
    d[s] = s
    for _ in range(n-1):
        for u in range(n):
            for v, w in G[u]:
                dist = d[u] + w
                if dist < d[v]:
                    d[v] = dist

    return d


# In[3]:


def dijkstra(G, s):
    n = len(G)
    visited = [False]*n
    dist = [math.inf]*n
    path = [None]*n
    queue = []
    hq.heappush(queue, (0, s))
    while len(queue) > 0:
        g, u = hq.heappop(queue)
        if not visited[u]:
            visited[u] = True
            for v, w in G[u]:
                f = w + g
                if not visited[v] and f < dist[v]:
                    dist[v] = f
                    path[v] = u
                    hq.heappush(queue, (f, v))
                    
    return dist, path


# In[4]:


def johnson(G):
    n = len(G)
    G.append([(n-1, 0)])
    p = bellmanFord(G, n) # n es el vertice que acabamos de agregar
    Gp = [[] for _ in range(n)]
    
    for u in range(n):
        for v, Ce in G[u]:
            Gp[u].append((v, Ce + p[u] - p[v]))
    
    paths = [[] for _ in range(n)]
    for u in range(n):
        _, paths[u] = dijkstra(Gp, u)
        
    return paths


# In[5]:


G = [[(3, 2)],
     [(0, 6), (2, 3)],
     [(0, 4), (3, 5)],
     [(1, -7), (2, -3)]]


# In[6]:


johnson(G)


# In[ ]:




