#!/usr/bin/env python
# coding: utf-8

# In[55]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt

plt.figure(figsize=(20, 10))

#1
x = [i for i in range(1, 10)]
y1 = [i + 1 for i in x] 

#2
import math

x = [i for i in range(1, 10)]
y2 = [math.log(i) for i in range(1, 10)]


#3
x = [i for i in range(1, 10)]
y3 = [i for i in x] 

#4

x = [i for i in range(1, 10)]
y4 = [i*math.log(i) for i in x]

#5
x = [i for i in range(1, 10)]
y5 = [i**2 for i in x]

#6
x = [i for i in range(1, 10)]
y6 = [(2**i + 1) for i in x] 

#7
x = [i for i in range(1, 10)]
y7 = [math.factorial(i) for i in x]

#8

x = [i for i in range(1, 10)]
y8 = [(i^i +1) for i in x]

plt.plot(x, y1, label='(1)', color='sienna')
plt.plot(x, y2, label='log n', color='teal')
plt.plot(x, y3, label='(n)', color='royalblue')
plt.plot(x, y4, label='n log n', color='r')
plt.plot(x, y5, label='n^2', color='blueviolet')
plt.plot(x, y6, label='2^n', color='lawngreen')
plt.plot(x, y7, label='(n!)', color='indigo')
plt.plot(x, y8, label='n^n', color='fuchsia')


plt.xlabel('Elements')
plt.ylabel('Operations')
plt.title('Big O Notation')
plt.legend()
plt.show()


# In[53]:


#2
import math


#2
x = [i for i in range(1, 10)]
y = [math.log(i) for i in range(1, 10)]


plt.plot(x,y)


plt.xlabel('Elements')
plt.ylabel('Operations')
plt.title('Big O Notation')
plt.text(2, 4, 'log n')
plt.show()

# label the curve "O(log n)"


# In[36]:


#3

x = [i for i in range(15)]
y = [i for i in x] 


plt.plot(x,y)


plt.xlabel('Elements')
plt.ylabel('Operations')
plt.title('Big O Notation')
plt.text(10, 4, '(n)')
plt.show()


# In[18]:


#4

y = [i*log(i) for i in x]

plt.plot(x,y)


plt.xlabel('Elements')
plt.ylabel('Operations')
plt.title('Big O Notation')

plt.show()



# and label it "O(n log n)"


# In[28]:


#5

x = [i for i in range(15)]
y = [i**2 for i in x]

plt.plot(x,y)


plt.xlabel('Elements')
plt.ylabel('Operations')
plt.title('Big O Notation')
plt.text(10, 25, 'n^2')
plt.show()

# and label it "O(n^2)"


# In[26]:


#6

x = [i for i in range(11)]
y = [(2**i + 1) for i in x] 

plt.plot(x,y)


plt.xlabel('Elements')
plt.ylabel('Operations')
plt.title('Big O Notation')
plt.text(3, 600, '2^n')
plt.show()


# In[25]:


#7
x = [i for i in range(13)]
y = [factorial(i) for i in x]

plt.plot(x,y)


plt.xlabel('Elements')
plt.ylabel('Operations')
plt.title('Big O Notation')
plt.text(3, 12, '\(n!\)')
plt.show()


# In[24]:


#8
x = [i for i in range(8)]
y = [(i^i +1) for i in x]

plt.plot(x,y)


plt.xlabel('Elements')
plt.ylabel('Operations')
plt.title('Big O Notation')
plt.text(3, 12, "n^n")
plt.show()

# label it "O(n^n)"


# In[ ]:




