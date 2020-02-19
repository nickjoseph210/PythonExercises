"""
Data Types, Operators, and Variables Exercises
------------------------------------------------
Identify the folowing data Types

1 - 99.9
 Float
2 - "False"
 String
3 - False
 Boolean
4 - '0'
 String
5 - 0
 Integer
6 - True
 Boolean
7 - "True"
 String
8 - [{}]
 Dictionary in a list
9 - {a: []}
 List in a Dictionary
-----------------------------------------------
What Data Type would best represent:

Q: A term or phrase typed into a search box?
A: A String

Q: If a user is logged in?
A: Boolean

Q: Whether or not a coupon code is valid?
A: Boolean

Q: An email address typed into a registration form?
A: String

Q: The price of a product?
A: Float

Q: A matrix?
A: Nested lists

Q: The email address collected from a registration form?
A: Boolean

Q: Information about applicants to Codeup's Data Science program?
A: Strings, Integers
--------------------------------------------
For each of the following code blocks, read the expression and predict the result of 
what evaluating it would be, then execute the expression in your Python REPL:

'1' + 2 - Error prediction.  Can't concatenate a string and an Integer
6 % 4 - Result would be 2, as it's the remainder of 6 / 4
type(6 % 4) - Integer
type(type(6%4)) - data type 'VALUE'
'3 + 4 is' + 3 + 4 - Error about concatenating strings and Integers
0 < 0 - True evaluation
'False' == False - False evaluation - a string is not a Boolean
True == 'True' - False evaluation - booleans do not equal strings
5 >= -5 - True
!False or False - False, because not False does not = False
True or '42' - True evaluation because one of two criteria are met
!True && !False - False evaluation: not true is NOT a condition of not false
6 % 5 - Integer (1)
5 < 4 and 1 == 1 - False, because both conditions are NOT true
"codeup" == "codeup" and "codeup" == "Codeup" - False; the last condition is NOT true
4 >= 0 and 1 !== 1 - Invalid syntax because '!==' is NOT a comparison Operators
6 % 3 == 0 - True
5 % 2 != 0 - True
[1] + 2 - Error; can't concatenate list index with Integer
[1] + [2] - [1, 2]
[1]*2 - [1, 1]
[1] * [2] - Error; can't multiply lists
[] + [] == [] - True 
{} + {} - Error - can't add empty dictionaries
----------------------------------------------
You've rented some movies for the kids: 'The Little Mermaid' for 3 nights, 'Brother Bear' for 5 days, 
and 'Hercules' for 1 day.  If the price for the movies is $3 / day, how much will you have to pay?
lit_merm = 3 * 3
bro_bear = 3 * 5
herc = 3 * 1
total = lit_merm + bro_bear + herc
print(total)

You're a contractor for 3 companies: Google, Amazon, and Facebook.  They all pay you different hourly rates.
Google pays $400 / hr, Amazon $380 / hr , and Facebook $350 / hr.  How much will you get paid this week if 
you worked 10 hours for Facebook, 6 hours for Google, and 4 hours for Amazon?
goog_pay = 400 * 6
amaz_pay = 380 * 4
face_pay = 350 * 10
totsPay = goog_pay + amaz_pay + face_pay
print(totsPay)

A student can only enroll in a class if it is not full.  Plus, she can only do it if the class doesn't 
conflict with her schedule:
class_max_size = 10
curr_class_size = 8
class_time = 2
student_class_times = [9, 10, 1, 3]
if curr_class_size < class_max_size and class_time != student_class_times:
    print("This student can sign up for her class!")
else:
    print("Sorry, Kid.  You're outta luck.")

A product offer is only good if a person buys more than two items and if the offer is not expired.
Premium members don't need to buy a minimum no. of products to get the offer:
import datetime
current_date_time = datetime.datetime(2020, 2, 19)
coupon_good_date = datetime.datetime(2020, 3, 01)
items_purchased = 4
min_items_needed = 2
prem_mem_no = 7
cust_mem_no = range(1, 20)
if current_date_time < coupon_good_date and items_purchased > min_items_needed:
    print("Conratulations!  You just got this product offer!")
if current_date_time < coupon_good_date and prem_mem_no in cust_mem_no:
    print("Thank you for your premium membership!  Please enjoy this product offer: ")
else:
    print("We're sorry, but this transaction does not qualify you for the current promotion.")

---------------------------------------------
Use the following code to execute the instructions below:
"""
username = 'codeup'
password = 'notastrongpassword'

"""
Create a variable that holds a bool for each of the following:

a.) the password must be at least 5 characters

length = len(username) >= 5

b.) the username cannot be more than 20 characters:

u_length = len(username) <= 20

c.) the password must NOT be the same as the username:

troof = len(username) != len(password)


