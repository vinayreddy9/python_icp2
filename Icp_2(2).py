#!/usr/bin/env python
# coding: utf-8

# In[1]:


def start() :
    a = int(input("Enter a non negative integer : ")) # reads a non negative integer from user
    if (a < 0):
        print(" You have entered a negative integer: ")
        return start()
    else:
        i = 0
        while a != 0:
            if (a % 2 == 0):
                a = a/2
                i = i+1
            else:
                a = a - 1
                i = i + 1
        print(a)
        print(i)
start()


# In[ ]:




