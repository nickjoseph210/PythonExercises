#!/usr/bin/env python
# coding: utf-8

# In[8]:


from matplotlib import pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[30]:


#x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#y = x**2

x = [i for i in range (11)] # list comp for the range of nums on x axis; value x
y = [(i**2 - i) for i in x] # list comp for the maths required; y-axis

plt.plot(x, y)

plt.text(-4.5, 0, "Point of Origin (0,0)") # moved from (0,0 because it looked ugly)

plt.show()


# In[3]:


# for y = square root of x
x = [i for i in range (11)]
y = [(i \sqrt{i}) for i in x]
plt.plot(x, y)
plt.xlabel('x-value')
plt.ylabel('y = \sqrt{x}')
plt.title('Chart 1: x v. y')
plt.show()


# In[ ]:




