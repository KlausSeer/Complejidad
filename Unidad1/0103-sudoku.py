#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math


# In[2]:


int(math.sqrt(9))


# In[3]:


def checkSudoku(t):
    n = len(t)
    m = int(math.sqrt(n))
    for i in range(n):
        ch = [False]*n
        for j in range(n):
            ch[t[i][j] - 1] = True
        for j in range(n):
            if not ch[j]:
                return False
        ch = [False]*n
        for j in range(n):
            ch[t[j][i] - 1] = True
        for j in range(n):
            if not ch[j]:
                return False
            
    for i in range(m):
        for j in range(m):
            ch = [False]*n
            for k in range(n):
                p = k // m
                q = k % m
                ch[t[i*m + p][j*m + q] - 1] = True
            for j in range(n):
                if not ch[j]:
                    return False
    
    return True


# In[4]:


t = [[1, 2, 3, 4],
     [3, 4, 1, 2],
     [4, 3, 2, 1],
     [2, 1, 4, 3]]


# In[5]:


checkSudoku(t)


# In[6]:


def getline(line):
    return [int(n) for n in line.split(' ')]


# In[7]:


def getmatrix():
    res = []
    while True:
        line = input("Ingrese una fila:")
        if line == "":
            return res
        res.append(getline(line))


# In[8]:


getmatrix()


# In[9]:


def readSudoku(filename):
    with open(filename) as f:
        t = []
        for line in f:
            t.append(getline(line))
    return t


# In[10]:


checkSudoku(readSudoku('sudoku1.txt'))


# In[11]:


checkSudoku(readSudoku('sudoku2.txt'))


# In[12]:


[i for i in range(10)]


# In[13]:


[i+1 for i in range(10)]


# In[14]:


[i*2 for i in range(10)]


# In[15]:


[i**2 for i in range(10)]


# In[16]:


[math.sqrt(i) for i in range(10)]


# In[17]:


a = "1 2 3 4"
b = a.split(' ')
c = [int(n) for n in b]


# In[18]:


print(a)
print(b)
print(c)


# In[ ]:




