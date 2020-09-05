#!/usr/bin/env python
# coding: utf-8

# In[1]:


p = open("//Users/vinayreddymeka/Desktop/example.txt", 'r') # opens text file from user defined location
j = p.read() # reads the file 
i = j.split() # converts the string into the list
i= [element.upper() for element in i] ; i # converts all lower case to uypper case
print(i) # prints the list i
a = [] # creates empty lists
b = []
for k in i:
    if k not in a:
        a.append(k) # appends k to list a
        count = 0
        for h in i:
            if h == k:
                count += 1
        b.append(k)
        b.append(count)
        m = ' '.join([str(elem) for elem in b]) # converts list to string
print(m)
outF = open("//Users/vinayreddymeka/Desktop/example.txt", 'a') # writes output to the external file
#for line in m:
outF.write(m +"\n") # writes the output in a new line
outF.close()


# In[ ]:





# In[ ]:





# In[ ]:




