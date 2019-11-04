#!/usr/bin/env python
# coding: utf-8

# In[5]:


import random as rnd


# In[6]:


def randomAM(n):
    return [[rnd.randint(0, 1) for _ in range (n)] for _ in range(n)]


# In[7]:


randomAM(5)


# In[8]:


import graphviz as gv

def drawAM(G):
    dot = gv.Digraph(comment='Nada')
    n = len(G)
    for u in range(n):
        dot.node(str(u), str(u))
    
    for u in range(n):
        for v in range(n):
            if G[u][v] == 1:
                dot.edge(str(u), str(v))
    dot.graph_attr['rankdir'] = 'BT'
    return dot


# In[16]:


drawAM(randomAM(7))


# In[21]:


def randomAL(n):
    return [sorted([rnd.randint(0, n-1) for _ in range(rnd.randint(0,n))]) for _ in range(n)]


# In[22]:


randomAL(5)


# In[23]:


def drawAL(G):
    dot = gv.Digraph(comment='Nada')
    n = len(G)
    for u in range(n):
        dot.node(str(u), str(u))
    
    for u in range(n):
        for v in G[u]:
            dot.edge(str(u), str(v))
    dot.graph_attr['rankdir'] = 'BT'
    return dot


# In[25]:


G = randomAL(7)
print(G)
drawAL(G)


# In[ ]:




