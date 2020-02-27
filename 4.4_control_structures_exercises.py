#!/usr/bin/env python
# coding: utf-8

# In[2]:


#1a. Prompt the user for a day of the week, and print out whether or not the day is Monday 

prompt = input("Tell me what day it is today: ")

if prompt.lower() == "monday":
    print("You're right!  Today is Monday!")
else:
    print(f"Wait, today is {prompt.capitalize()}?  I thought it was Monday!")
    
# day = input
# day = day.lower() - to make the casing not matter
# continue prompting user for a good input
# while day not in [list days of the week]:
#     print('please type in the full day of the week.')
#     day = input('what day of the week is it')
#     day = day.lower
# if day.lower() == "monday":
#     print("today's monday")
# else:
#     print(f"today's not monday.  it's {day.capitalize()}")


# In[5]:


#1b. Same as above, but tell the user whether or not it is a weekday or a weekend

weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

weekend = ["Saturday", "Sunday"]

prompt = input("Tell me the day, and I'll tell you if it's a weekend or not: ")
if prompt in weekdays:
    print(f"{prompt}?  Shoot.  I was hoping today was a weekend...")
else:
    print(f"That's right, it's {prompt}!  Sleeping in!  You know, now that football season's over.")

# See Ryan's answer in git


# In[16]:


#1c. create three work-related variables and calculate the paycheck (time + 1/2 for over 40hrs)

number_of_hours = float(input("How many hours did you work this week? "))

hourly_rate = float(input("And how much do you charge per hour? "))

total_pay = (number_of_hours * hourly_rate)

if number_of_hours <= int(40):
    print(f"Great job!  Here's ${total_pay}!")
else:
    print(f"Overtime?  Nice.  Enjoy your ${total_pay * 1.5}!")

# Ryan's answer:
# hours_worked = 51
# hourly_rate = 50
# total = 0
# if hours_worked <= 40:
#     total = hourly_rate * hours_worked
# else:
#     #get the number of hours overtime, calculate overtime and add to 40*regular rate
#     overtime_hours = hours_worked - 40
#     overtime_pay = overtime_hours * 1.5 * hourly_rate
#     regular_pay = 40 * hourly_rate
#     total = regular_pay * overtime_pay
# print(f"After working {hours_worked} for an hourly rate of {hourly_rate} with overtime.")
    


# In[24]:


#While loops

#2a1:

i = 5
while i <= 15:
    print(i)
    i += 1

# i = 5 <- starting point
# end = 15 <- ending point
# while i <= end:
#     print(i)
#     i += 1


# In[34]:


#2a2:

i = 2
print(0)
while i %2 == 0 and i <= 100:
    print(i)
    i += 2


# In[32]:


#2a3:

i = 100
while i > -15:
    print(i)
    i -= 5
    


# In[4]:


#2a4

i = 2

while i in range(2, 1000000):
    print(i)
    i += i**2
    
# Ryan's answer:
# i = 2
# while i < 1_000_000:
#     print(i)
#     i *= i


# In[2]:


i = 100
while i >= 5:
    print(i)
    i -= 5


# In[7]:


#2b1 For Loops

user_number = int(input("Give me a number, and we'll outline the times table through 10: "))

times_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in times_nums:
    total = user_number * num
    print(f"{user_number} x {num} = " + str(total))


# In[8]:


#2b2 
n = 9
for i in range(1, 10):
    for j in range(1, i+1):
        print(i, end = "")
    print()

# Ryan's answer:
# for i in range(1,10):
#     print(i * str(i))


# In[5]:


#2c1
#My answer
# user_number = input("Give me an odd number between 1 and 50: ")
# if user_number %2 == 0 or user_number < 1 or user_number > 50:
#     print("Please try again: ")
# if user_number.isdigit():
#     user_number = int(user_number)
#     if user_number % 2 == 1 and user_number > 1 and user_number < 50:
#         #print("So far, so good!")
#         for user_number in range(50):
#             print("Here is an odd number: " + str(user_number))                 
#             continue
#         print(f"Yikes!  Skipping number: {user_number}")
    
## Got stuck
# Ryan's answer:
# 1.) Get an odd number between 1 and 50:
#     user_choice = input("input an odd integer between 1 and 50: ")
#     while (user_choice.isdigit() == False 
#           or int(user_choice) < 1 
#           or int(user_choice) %2 == 0
#           or int(user_choice) > 50): # all these continue prompting the user for valid input based on our conditions
#         print(f"{user_choice} is nice, but we'll ned an odd number between 1 and 50.")
#         user_choice = input ("Please input an odd number between 1 and 50".)
        
#     user_choice = int(user_choice)   
    
#     print(f"{user_choice} is an odd number between 1 and 50.  Thank you.")
    
#     print("The number to skip is", user_choice)
    
#     for i in range(1,50):
#         if i % 2 == 0:
#             continue
#         print(f"{i} is an odd number.")
#         if i == user_choice:
#             print(f"Skipping {i}.")


# In[4]:


#Trying Ryan's answer
user_choice = input("input an odd integer between 1 and 50: ")
while (user_choice.isdigit() == False 
          or int(user_choice) < 1 
          or int(user_choice) %2 == 0
          or int(user_choice) > 50): # all these continue prompting the user for valid input based on our conditions
    print(f"{user_choice} is nice, but we'll ned an odd number between 1 and 50.")
    user_choice = input ("Please input an odd number between 1 and 50.")
        
user_choice = int(user_choice)   
    
print(f"{user_choice} is an odd number between 1 and 50.  Thank you.")
    
print("The number to skip is", user_choice)
    
for i in range(1,50):
    if i % 2 == 0:
        continue
    
    if i == user_choice:
            print(f"Skipping {i}.")
            continue
    print(f"{i} is an odd number.")


# In[6]:


#2c2:
#My answer
user_num = int(input("Give me a positive number and I'll count from zero to that number: "))
for num in user_num: 
    if num < 0:
        print(f"Sorry, but {user_num} is not a positive number.")
        new_user_num = int(input("Please try again: "))
while user_num >= 0 and user_num in range(0, user_num):
    user_number_count = 0
    user_number += 1

#Ryan's answer:
# Revisit the loop above
# user_choice = input("input a positive number: ")
# while (user_choice.isdigit() == False 
#           or int(user_choice) <= 0): 
#            # all these continue prompting the user for valid input based on our conditions
#     print(f"{user_choice} is nice, but we'll need a positive number.")
#     user_choice = input ("Please input a positive number.")


# In[7]:


for i in range(user_choice + 1):
    print(i)


# In[3]:


#2d2 count backwards from a user-provided num
#Ryan's answer:
while user_choice >= 1:
    print(user_choice)
    user_choice -= 1


# In[7]:


#3 FizzBuzz

x = range(1, 101)

#a
print(x)
for num in x:
    if num %3 == 0:
        print("Fizz")
    if num %5 == 0:
        print("Buzz")
    if num %3 == 0 and num %5 == 0:
        print("FizzBuzz")
    else:
        print(num)


# In[ ]:




