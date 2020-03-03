#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


# 1.
series = pd.Series(["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", 
                    "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", 
                    "papaya"])

# a. naming of the variable that holds the series to 'fruits'

fruits = series
fruits


# In[4]:


#b. sees what 'describe()' returns for a series of strings

fruits.describe()


# In[5]:


#c. returns only the unique names in the series

fruits.unique()


# In[6]:


#d. determines how many times each value occurs in the series

fruits.value_counts()


# In[27]:


#e. determine the most frequently occurring fruit names from the series

fruits.mode() # the zero on the left indicates its original index in the series list


# In[28]:


#f. determine the least frequently occuring fruit names from the series

fruits.unique().min()[:]


# In[29]:


#g. the code to get the longest string from the series of fruits

fruits.astype('str').max()


# In[30]:


#h. find the fruits with five or more letters in the name
fruits.str.len() 


# In[31]:


#i. capitalize all the fruit strings in the series
def new_fruit(fruit):
    return fruit.capitalize()

fruits.apply(new_fruit)


# In[32]:


#j. count the letter "a" in all the fruits (use string vectorization)
fruits.apply(lambda x: x.count('a')).sum()


# In[41]:


#k. output the number of vowels in each and every fruit

fruits.str.lower().str.count(r'[aeiou]')


# In[42]:


#l. use .apply method along with lambda function to find the fruit(s) containing two or more 'o' letters in name
fruits.apply(lambda x: x.count('o')).sum()


# In[53]:


#m. write the code to get fruits only with the name 'berry' in them
fruits.str.contains('berry')
fruits[fruits.str.contains('berry')]


# In[54]:


#n. write the code to get fruits only with the name 'apple' in them
fruits[fruits.str.contains('apple')]


# In[57]:


#o. which fruit has the highest amounts of vowels
fruits[fruits.str.lower().str.count(r'[aeiou]')]


# In[3]:


#2 
series = pd.Series(['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', 
                        '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45', 
                        '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', 
                        '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', 
                        '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23'])


# In[20]:


series


# In[4]:


# what is the data type of the series?
type(series)


# In[24]:


#3
grades = pd.Series([60, 86, 75, 62, 93, 71, 60, 83, 95, 78, 65, 72, 69, 81, 96, 80, 85, 92, 82, 78])
grades


# In[25]:


# lowest grade

grades.min()


# In[26]:


# highest grade

grades.max()


# In[27]:


# mean grade

grades.mean()


# In[28]:


# median grade

grades.median()


# In[7]:


# plot histogram of the scores
import matplotlib.pyplot as plt

grades.plot.hist()


# In[40]:


# convert each of the numbers above to a letter grade

def Letter_Grade(grade):
    if grade >= 90:
        result = ['A']
    elif grade >= 80:
        result = ['B']
    elif grade >= 70:
        result = ['C']
    elif grade >= 60:
        result = ['D']
    else:
        result = ['F']
    return result

grades.apply(Letter_Grade)


# In[ ]:


#Write the code necessary to implement a curve. I.e. that grade closest to 100 should be converted to a 100, 
# and that many points should be given to every other score as well.


# In[50]:


#4:
series = pd.Series(['hnvidduckkqxwymbimkccexbkmqygkxoyndmcxnwqarhyffsjpsrabtjzsypmzadfavyrnndndvswreauxovncxtwzpwejilzjrmmbbgbyxvjtewqthafnbkqplarokkyydtubbmnexoypulzwfhqvckdpqtpoppzqrmcvhhpwgjwupgzhiofohawytlsiyecuproguy'])


# In[80]:


series.describe()


# In[88]:


def breakdown(string):
    for letter in len(string):
        list(letter)
    return string

series.apply(breakdown)


# In[60]:


letzgo = 'hnvidduckkqxwymbimkccexbkmqygkxoyndmcxnwqarhyffsjpsrabtjzsypmzadfavyrnndndvswreauxovncxtwzpwejilzjrmmbbgbyxvjtewqthafnbkqplarokkyydtubbmnexoypulzwfhqvckdpqtpoppzqrmcvhhpwgjwupgzhiofohawytlsiyecuproguy'
listgo = list(letzgo)
print(listgo)


# In[95]:


def is_vowel(str):
    """ 
    Returns True or False indicating if the string being passed into the function is a vowel
    """
    vowels = 'AEIOUaeiou'
    for letter in str:
        if letter in vowels:
            print('True')
        else:
            print('False')

series.apply(is_vowel)


# In[ ]:




