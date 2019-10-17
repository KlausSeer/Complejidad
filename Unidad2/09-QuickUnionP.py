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
            if self.sets[i] >= 0:
                dot.edge(str(i), str(self.sets[i]))
        dot.graph_attr['rankdir'] = 'BT'
        return dot


# In[17]:


class DisjointSetP(Dottable):
    def __init__(self, n):
        self.N = n
        self.sets = [-1 for _ in range(n)]
        
    def Find(self, a):
        x = a
        while self.sets[x] >= 0:
            x = self.sets[x]
        return x
    
    """def Find(self, x):
        if x == self.sets[x]:
            return x
        else:
            return self.Find(self.sets[x])"""
    
    def Union(self, a, b):
        pa = self.Find(a)
        pb = self.Find(b)
        if self.sets[pa] < self.sets[pb]:
            self.sets[pb] = pa
        elif self.sets[pb] < self.sets[pa]: 
            self.sets[pa] = pb
        else:
            self.sets[pb] -= 1
            self.sets[pa] = pb


# In[18]:


ds = DisjointSetP(10)


# In[19]:


ds.Dot()


# In[20]:


ds.Union(3, 4)
ds.Dot()


# In[21]:


ds.Union(4, 9)
ds.Dot()


# In[22]:


ds.Union(8, 0)
ds.Dot()


# In[23]:


ds.Union(2, 3)
ds.Dot()


# In[24]:


ds.Union(5, 6)
ds.Dot()


# In[25]:


ds.Union(5, 9)
ds.Dot()


# In[26]:


ds.Union(7, 3)
ds.Dot()


# In[27]:


ds.Union(4, 8)
ds.Dot()


# In[28]:


ds.Union(6, 1)
ds.Dot()


# In[ ]:




