#!/usr/bin/env python
# coding: utf-8

# # Dynamic Programming
# 
# ## Fibonacci

# In[7]:


cont = [0]
def fiboR(n):
    cont[0] += 1
    if n <= 1:
        return n
    else:
        return fiboR(n - 1) + fiboR(n - 2)
    
n = 10
print("Fibonacci de %d es %d"%(n, fiboR(n)))
print("Iteraciones: %d"%(cont[0]))


# In[6]:


cont = [0]
def fibo(n):
    t = [0]*(n+1)
    def fibofibo(n):
        cont[0] += 1
        if n == 1:
            t[0] = 0
            t[1] = 1
        else:
            fibofibo(n - 1)
            t[n] = t[n-1] + t[n-2]
    
    fibofibo(n)
        
    return t[n]
    
n = 10
print("Fibonacci de %d es %d"%(n, fibo(n)))
print("Iteraciones: %d"%(cont[0]))


# ## Coin master 2000

# In[24]:


import math


# In[25]:


def mincoins(d, p):
    C = [0]*(p + 1)
    M = [0]*(p + 1)
    
    def recu(p):
        if p == 0:
            C[0] = 0
        else:
            recu(p - 1)
            Cother = []
            minimum = math.inf
            moneda = 0
            for di in d:
                if p - di >= 0 and C[p-di] < minimum:
                    minimum = C[p-di]
                    moneda = di
        
            C[p] = 1 + minimum
            M[p] = moneda
            
    recu(p)
    return C, M


# In[26]:


d = [1, 5, 10, 20, 25, 50]
p = 40
C, M = mincoins(d, p)
print(C)
print(M)


# In[ ]:




