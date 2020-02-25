# make this file and import 4.5.  we have to change the name of 4.5 b/c '4(or any 
# integer) is not a valid python identifyer

import functions_exercise

import functions_exercise as fe 

functions_exercise.is_vowel("a")
fe.is_vowel("c:)

from functions_exercise import cum_sum as cumulative_sum

cumulative_sum([1, 2, 3, 4, 5])

# =============================

import itertools as it

it.product([1, 2, 3], "abc")

list(it.product([1, 2, 3], "abc"))

len(list(it.product([1, 2, 3,], "abc")))

some_combinations = it.product(range(1000), "abcdefghijklmnopqrstuvwxyz")

list(it.islice(some_combinations, 4))

it.combinations("abcd", 2)

list(it.combinations("abcd", 2))

#AB and BA are different permutations,
#but are the same when using combinations

# ===============================

import json

profiles = json.load(open("profiles.json))

#start exploring
profiles[0].keys()

[profile["guid"] for profile in profiles[:4]]

[profile["balance"] for profile in profile[:4]]

# import pprint == is a beatified printing itertool

# total # of users:
len(profiles)

# total number of active users
# 1st, check using [profile["isActive"] for profile in profiles]
# Now get the active profiles and the length of them
len([profile for profile in profiles if profile["isActive"]])

# number of inactive users
len([profile for profile in profiles if profile["isActive] == False])

# Grand total of balances for each user
# make a function!
profile = profiles[0]
def get_profile_banlance(profile):
# next line removes the $ sign and empty spaces
# and replaces them with non-empty spaces
    return float(profile["balance"].replace('$', '').replace(" ", ""))
# now use the function to count the grand total:

sum([get_profile_balance(profile) for profile in profiles])

# average balance per user:
# assign sum above to a variable:

balances = sum([get_profile_balance(profile) for profile in profiles]))
avg_balance = sum(balances) / len(balances)

# User with the lowest balance:
user_with_the_lowest_balance = profiles[0]
for user in profiles[1:]:
    if get_profile_balance(user) < get_profile_balance(user_with_lowest_balance):
        use_with_lowest_balance = user
user_with_the_lowest_balance

#OR:
# B/c in order to sort dictionaries, we need to tell python how to compare them
# the 'key' keyowrd argument speicifes a function that takes in one element of the list
# and returns a value that can be sorted
min(profiles, key=get_profile_balance)

# User with the highest balance:
max(profiles, key=get_profile_balance)

# Most favorite fruit:
# Least common favorite fruit

# Total number of unread messages for all users
profile = profiles[0]
def get_n_unread_messages(profile):
#greeting = profile["greeting"]
#greeting.index("have ") # will give us 25 results
#greeting[greeting.index("have "):] # go from where 'have ' starts and go to end
#int(greeting[greeting.index("have ") + 5:greeting.index("unread")])
    start_index = greeting.index("have ") + 5
    end_index = greeting.index(" unread")
    return int(greeting[start_index:end_index])
sum([get_n_unread_messages(profile) for profile in profiles])