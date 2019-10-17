#!/usr/bin/env python
# coding: utf-8

# In[1]:


from graphviz import Digraph, Source


# In[7]:


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


# In[9]:


class DisjointSetQF(Dottable):
    def __init__(self, n):
        self.N = n
        self.sets = [i for i in range(n)]
        
    def Find(self, a):
        return self.sets[a]
    
    def Union(self, a, b):
        pa = self.Find(a)
        pb = self.Find(b)
        for i in range(self.N):
            if self.sets[i] == pa:
                self.sets[i] = pb


# In[10]:


ds = DisjointSetQF(10)


# In[11]:


ds.Dot()


# In[12]:


ds.Union(3, 4)
ds.Dot()


# In[13]:


ds.Union(4, 9)
ds.Dot()


# In[14]:


ds.Union(8, 0)
ds.Dot()


# In[15]:


ds.Union(2, 3)
ds.Dot()


# In[16]:


ds.Union(5, 6)
ds.Dot()


# In[17]:


ds.Union(5, 9)
ds.Dot()


# In[18]:


ds.Union(7, 3)
ds.Dot()


# In[19]:


ds.Union(4, 8)
ds.Dot()


# In[20]:


ds.Union(6, 1)
ds.Dot()


# In[ ]:




