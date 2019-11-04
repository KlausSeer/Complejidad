#!/usr/bin/env python
# coding: utf-8

# In[6]:


def tonum(word, ch2dig):
    l = len(word)
    num = 0
    for ch in word:
        l = l - 1
        num += 10**l * ch2dig[ch]
    return num


# In[16]:


def solve(a, b, c, chars, digs, ch2dig):
    n = len(chars)
    if n == 0:
        na = tonum(a, ch2dig)
        nb = tonum(b, ch2dig)
        nc = tonum(c, ch2dig)
        return na + nb == nc
    else:
        char = chars[-1]
        for i in range(len(digs)):
            ch2dig[char] = digs[i]
            if solve(a, b, c, chars[:n-1], digs[:i]+digs[i+1:], ch2dig):
                #print(ch2dig)
                na = tonum(a, ch2dig)
                nb = tonum(b, ch2dig)
                nc = tonum(c, ch2dig)
                print(na, nb, nc)
                return True
        return False


# In[22]:


"""
SEND + MORE = MONEY
"""
a = 'SEND'
b = 'MORE'
c = 'MONEY'
#chars = {ch:-1 for ch in (a + b + c)}
chars = list(set(ch for ch in (a + b + c)))
print(chars)


# In[24]:


solve(a, b, c, chars, [i for i in range(10)], {})


# In[ ]:




