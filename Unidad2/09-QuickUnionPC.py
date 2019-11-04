#!/usr/bin/env python
# coding: utf-8

# In[1]:


from graphviz import Digraph, Source


# In[2]:


class Dottable:
    def Dot(self):
        dot = Digraph()
        for i in range(self.N):
            dot.node(str(i))
        for i in range(self.N):
            if self.sets[i] != i:
                dot.edge(str(i), str(self.sets[i]))
        dot.graph_attr['rankdir'] = 'BT'
        return dot


# In[3]:


class DisjointSetPC(Dottable):
    def __init__(self, n):
        self.N = n
        self.sets = [i for i in range(n)]

    def Find(self, x):
        if x == self.sets[x]:
            return x
        else:
            antepasado = self.Find(self.sets[x])
            self.sets[x] = antepasado
            return antepasado
    
    def Union(self, a, b):
        pa = self.Find(a)
        pb = self.Find(b)
        if pa != pb:
            self.sets[pb] = pa


# In[4]:


ds = DisjointSetPC(10)
ds.Dot()


# In[5]:


ds.Union(3, 4)
ds.Dot()


# In[6]:


ds.Union(4, 9)
ds.Dot()


# In[7]:


ds.Union(8, 0)
ds.Dot()


# In[8]:


ds.Union(2, 3)
ds.Dot()


# In[9]:


ds.Union(5, 6)
ds.Dot()


# In[10]:


ds.Union(5, 9)
ds.Dot()


# In[11]:


ds.Union(7, 3)
ds.Dot()


# In[12]:


ds.Union(4, 8)
ds.Dot()


# In[13]:


ds.Union(6, 1)
ds.Dot()


# In[ ]:




