#!/usr/bin/env python
# coding: utf-8

# In[1]:


# creating empty lists
a = []
b = []


# In[2]:


c = int(input("Enter the no. of students height you want to convert ")) # Reads input from user


# In[3]:


# Converts feet to cm
for i in range(0, c):
    j = float(input())  # Reads input as a float
    a.append(j)  # The input is append to the list a
    d = float(j*30.48) # feet is converted to cm
    e = round(d, 1)# round up to one decimal value
    b.append(e)  # The output is stored to list b
print(" Entered height in feet are" ,a) # prints the input list a in feet
print("converted height in cm", b) # prints the output list b in cm


# In[ ]:




