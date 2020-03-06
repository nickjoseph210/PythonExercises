#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
import numpy as np

from pydataset import data


# In[2]:


#1.

mpg = data("mpg")


# In[3]:


mpg


# In[4]:


mpg.describe()


# In[5]:


data("mpg", show_doc=True)


# In[24]:


mpg["average_mileage"] = (mpg.cty + mpg.hwy) / 2



mpg


# In[28]:


mpg["average_mileage"].sort_values()


# In[29]:


mpg.groupby(["manufacturer", "average_mileage"]).sort_values()


# In[12]:


#2 Joining and Merging

# Copy the users and roles dataframes:

users = pd.DataFrame({
    'id': [1, 2, 3, 4, 5, 6],
    'name': ['bob', 'joe', 'sally', 'adam', 'jane', 'mike'],
    'role_id': [1, 2, 3, 3, np.nan, np.nan]
})
users

roles = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['admin', 'author', 'reviewer', 'commenter']
})
roles


users


# In[14]:


roles


# In[16]:


# What do you think a right join would look like?

pd.merge(users, roles, left_on='role_id', right_on='id', how='right')


# In[17]:


# Compare to left join:

pd.merge(users, roles, left_on='role_id', right_on='id', how='left')


# In[18]:


# What would it look like with an outer join?

pd.merge(users, roles, left_on='role_id', right_on='id', how='outer')


# In[ ]:


# What happens if you drop the foriegn keys and try to merge them?

# You can still merge them, but it would have to be along the primary keys


# In[6]:


#3.Getting Data from SQL databases

# Create a function named get_db_url that takes in all the stuff we need for a connection string: username, 
# hostname, password, database name

# we want the following format so we can connect to MYSQL:

#     mysql + mypysql : // user : password @ host / db_name

def get_db_url(user, password, host, db_name=" "):
    return f"mysql+mypysql://{user}:{password}@{host}/{db_name}"

get_db_url("curie_953", "lFtpNAPcC2dZJFzCX5dreZ2pd5aAzfK5", "157.230.209.171")


# In[32]:


get_db_url("curie_953",  "lFtpNAPcC2dZJFzCX5dreZ2pd5aAzfK5", "157.230.209.171", "employees")


# In[7]:


pd.read_sql('SELECT * FROM employees LIMIT 5 OFFSET 50', get_db_url)


# In[38]:


from env import host, user, password

url = f'mysql+pymysql://{user}:{password}@{host}/employees'


# In[35]:


pd.read_sql('SELECT * FROM employees LIMIT 5 OFFSET 50', url)


# In[47]:


from env import host, user, password

pd.read_sql("SELECT * FROM employees LIMIT 5 OFFSET 50", url)


# In[39]:


#3c1: intentionally make a typo in the database url.  What kind of error message do I see?

url = f'mysql+pymysql://{user}:{password}@{host}/empoyees' #misspelled 'employees'

pd.read_sql("SELECT * FROM employees LIMIT 5 OFFSET 50", url)

# Got an operational error, specifically:

# OperationalError: (pymysql.err.OperationalError) 
#     (1044, "Access denied for user 'curie_953'@'%' to database 'empoyees'")


# In[48]:


#3c2: Intentionally make an error in my SQL query.  What's the error message look like?

from env import host, user, password

url = f'mysql+pymysql://{user}:{password}@{host}/employees' 

pd.read_sql("SELECT * FROM employees LIMIT 5 OFSET 50", url) #misspelled 'offset'

# Error I got was:


# ProgrammingError: (pymysql.err.ProgrammingError)
# (1064, "You have an error in your SQL syntax; check the manual that corresponds to 
# your MySQL server version for the right syntax to use near 'OFSET 50' at line 1")
# [SQL: SELECT * FROM employees LIMIT 5 OFSET 50]


# In[ ]:


#So if I get an OPERATIONAL ERROR, that means I did something wrong in the DATABASE URL

#If I get a PROGRAMMING ERROR, that means I have an error with my SQL SYNTAX

# OPERATIONAL ERROR = URL MISTAKE IN CONNECTION STRING
# PROGRAMMING ERROR = SQL SYNTAX MISTAKE


# In[11]:


#3d. Read the employees and titles tables in two separate dataframes

from env import host, user, password

url = f'mysql+pymysql://{user}:{password}@{host}/employees'

pd.read_sql('SELECT * FROM employees LIMIT 5 OFFSET 50', url)  
    
url2 = f'mysql+pymysql://{user}:{password}@{host}/titles'

pd.read_sql("SELECT * FROM titles LIMIT 5 OFFSET 50", url2)


# In[21]:


#4 Chipotle database fun

from env import host, user, password

url = f'mysql+pymysql://{user}:{password}@{host}/chipotle'
    

pd.read_sql("SELECT * FROM item_price LIMIT 5 OFFSET 50", url)


# In[ ]:




