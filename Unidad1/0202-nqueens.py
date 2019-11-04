#!/usr/bin/env python
# coding: utf-8

# In[1]:


def draw(board):
    n = len(board)
    print("%s+"%("+---"*n))
    for i in range(n):
        for j in range(n):
            if board[i] == j:
                print("| Q ", end="")
            else:
                print("|   ", end="")
        print("|")
        print("%s+"%("+---"*n))


# In[2]:


draw([1, 3, 0, -1])


# In[3]:


def check(board, row, col):
    n = len(board)
    for i in range(row):
        if board[i] == col:
            return False
        d = row - i
        if board[i] + d == col:
            return False
        if board[i] - d == col:
            return False
    return True


# In[4]:


def nqueens(board, row):
    n = len(board)
    if row < n:
        for col in range(n):
            if check(board, row, col):
                board[row] = col
                nqueens(board, row + 1)
    else:
        draw(board)


# In[5]:


n = 4
board = [-1]*n
nqueens(board, 0)


# In[15]:


print("hola "*5)


# In[21]:


print("%d  %f  %s"%(1, 5.6, "hola"))

