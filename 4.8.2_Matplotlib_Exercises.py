#!/usr/bin/env python
# coding: utf-8

# In[4]:


from matplotlib import pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[31]:


#x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#y = x**2

x = [i for i in range (11)] # list comp for the range of nums on x axis; value x
y = [(i**2 - i) for i in x] # list comp for the maths required; y-axis

plt.plot(x, y)

# plt.text(-4.5, 0, "Point of Origin (0,0)") # moved from (0,0 because it looked ugly)
plt.annotate("Origin 0,0", xy=(0, 0), xytext=(-2.5, 7), arrowprops={'facecolor': 'red'})
plt.show()


# In[15]:


# for y = square root of x
x = [i for i in range (11)]
y = [i**0.5 for i in x]
plt.plot(x, y)
plt.xlabel('x-value')
plt.ylabel(r'$y = \sqrt{x}$')
plt.title('Chart 1: Ex versus Why')
plt.show()

# for y = x^3
x = [i for i in range(11)]
y = [i**3 for i in x]
plt.plot(x,y)
plt.xlabel('x-value')
plt.ylabel('y = x^3')
plt.title('Chart 2: Why = Ex Cubed')
plt.show()

import math

# for y = tan(x)
x = [i for i in range(11)]
y = [math.tan(i)for i in range(11)]

plt.plot(x, y)
plt.xlabel('x-value')
plt.ylabel('$\ tan$')
plt.title('Tangent of Ex')
plt.show()

# for y = 2^x
x = [i for i in range(11)]
y = [(2**i + 1) for i in x] 

plt.plot(x, y)
plt.xlabel('x-value')
plt.ylabel('$2^x$')
plt.title('Exponential Function')
plt.show()


# In[23]:


import math

# for y = square root of x

all_x = [i for i in range (11)]
y = [i**0.5 for i in x]
plt.plot(x, y)

# for y = x^3
y = [i**3 for i in x]
plt.plot(x,y)

# for y = tan(x)
y = [math.tan(i)for i in range(11)]
plt.plot(x,y)

# for y = 2^x
y = [(2**i + 1) for i in x] 
plt.plot(x,y)


plt.xlabel('x-value')
plt.ylabel('y-values')
plt.title('Chart 5: Total Plots')

plt.show()

# # for y = x^3
# x = [i for i in range(11)]
# y = [i**3 for i in x]
# plt.plot(x,y)
# plt.xlabel('x-value')
# plt.ylabel('y = x^3')
# plt.title('Chart 2: Why = Ex Cubed')
# plt.show()

# import math

# # for y = tan(x)
# x = [i for i in range(11)]
# y = [math.tan(i)for i in range(11)]

# plt.plot(x, y)
# plt.xlabel('x-value')
# plt.ylabel('$\ tan$')
# plt.title('Tangent of Ex')
# plt.show()

# # for y = 2^x
# x = [i for i in range(11)]
# y = [(2**i + 1) for i in x] 

# plt.plot(x, y)
# plt.xlabel('x-value')
# plt.ylabel('$2^x$')
# plt.title('Exponential Function')
# plt.show()


# In[ ]:




