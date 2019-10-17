#!/usr/bin/env python
# coding: utf-8

# In[7]:


def wordCountInLine(line):
    line = line.strip()
    c = 1
    for ch in line:
        if ch == ' ':
            c += 1
    return c


# In[5]:


def wordCount(text, i, f):
    if i == f:
        return wordCountInLine(text[i])
    else:
        m = (i + f) // 2
        return wordCount(text, i, m) + wordCount(text, m+1, f)


# In[9]:


with open('spam.txt') as file:
    text = file.read()
    text = text.strip().split('\n')
    print(wordCount(text, 0, len(text) - 1))


# In[ ]:




