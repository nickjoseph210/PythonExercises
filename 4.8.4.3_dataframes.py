#!/usr/bin/env python
# coding: utf-8

# In[64]:


import pandas as pd
import numpy as np


# In[2]:


from pydataset import data


# In[15]:


np.random.seed(123)

students = ['Sally', 'Jane', 'Suzie', 'Billy', 'Ada', 'John', 'Thomas',
            'Marie', 'Albert', 'Richard', 'Isaac', 'Alan']

# randomly generate scores for each student for each subject
# note that all the values need to have the same length here
math_grades = np.random.randint(low=60, high=100, size=len(students))
english_grades = np.random.randint(low=60, high=100, size=len(students))
reading_grades = np.random.randint(low=60, high=100, size=len(students))

df = pd.DataFrame({'name': students,
                   'math': math_grades,
                   'english': english_grades,
                   'reading': reading_grades})

type(df)


# In[16]:


print(df)


# In[20]:


#a

df['passing_math'] = df.math > 65

df


# In[21]:


#b.

df['passing_english'] = df.english > 65

df


# In[27]:


#c.

# sort by passing_english, then by student name...

df.sort_values(by='name').sort_values(by='passing_english')


# In[29]:


#d. Sort the English grades first by passing_english, then by actual grade

df.sort_values(by="english").sort_values(by="passing_english")


# In[51]:


#e.
df['overall_grade'] = df.mean(axis=1,)
df


# In[6]:


#2.
from pydataset import data


# In[7]:


mpg = data("mpg")


# In[8]:


#a.
mpg


# In[59]:


#b.
mpg.info()


# In[60]:


#c.
mpg.describe()


# In[15]:


#d and e
mpg.rename(columns={'cty' : 'city'}, {'hwy' : 'highway'})


# #f.
# mpg.query('cty' > 'highway')

# In[11]:


#g.
mpg['mileage_difference'] = mpg.hwy - mpg.cty
mpg


# In[16]:


#h.
mpg.diff(axis=0)


# In[ ]:


#i.


# In[ ]:


#j.


# In[ ]:


#k.


# In[ ]:


#l


# In[ ]:


#3

