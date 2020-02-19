# 17 list comprehension problems in python

fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

# Example for loop solution to add 1 to each number in the list
numbers_plus_one = []
for number in numbers:
    numbers_plus_one.append(number + 1)

# Example of using a list comprehension to create a list of the numbers plus one.
numbers_plus_one = [number + 1 for number in numbers]

# Example code that creates a list of all of the list of strings in fruits and uppercases every string
output = []
for fruit in fruits:
    output.append(fruit.upper())

#Ex1: Rewrite the above example code where uppercased_fruits holds the output in caps
uppercased_fruits = [fruit.upper() for fruit in fruits]

#Ex2: Create a variable named 'capitalized fruits' and use list comp to get their 
#first letters capitalized
capitalized_fruits = [fruit.title() for fruit in fruits]

#Ex3: Create 'fruits_with_more_than_two_vowels' 
fruits_with_more_than_two_vowels = [
    fruits for fruit in fruits if
    fruit.count("a") +
    fruit.count("e") +
    fruit.count("i") +
    fruit.count("o") + 
    fruit.count("u") > 2
]
fruits_with_more_than_two_vowels
#Ex4: Create 'fruits with only two vowels'
fruits_with_only_two_vowels

#Ex5: Create 'fruits with more than 5 characters'
 fruits_with_more_than_five_characters = [fruit for fruit in fruits if len(fruit) > 5]

#Ex6: make a list that contains each fruit with exactly five characters
fruits_with_five_characters = [fruit for fruit in fruits if len(fruit) == 5]

#Ex7: make a list for fruits with less than 5 characters
fruits_with_less_than_five_characters = [fruit for fruit in fruits if len(fruit) < 5]

#Ex8: list containing the number of characters in each fruit
letter_count = [len(fruit) for fruit in fruits]

#Ex9: fruits with letter a variable
fruits_with_letter_a = [fruit for fruit in fruits if "a" in fruit]

#Ex10: make even_numbers variable that only holds the even numbers
en = [number for number in numbers if number % 2 == 0]

#Ex11: make odd_numbers like above
on = [number for number in numbers if number % 2 == 1]

#Ex12: positive numbers
positive_numbers = [number for number in numbers if number > 0]

#Ex13: negative numbers
negative_numbers = [number for number in numbers if number < 0]

#Ex14: list of numbers with more than two numerals
more_than_two = [number for number in numbers if len(str(abs(number))) >= 2] # abs drops the minus sign off

#Ex15: numbers_squared variable that squares each number
numbers_squared = [number**2 for number in numbers]

#Ex16: odd_negative_numbers that has only odd AND negative nums
odd_negative_numbers = [number for number in numbers if number % 2 ==1 and number < 0]

#Ex17: numbers_plus_five variable that returns the list of nums + 5
numbers_plus_five = [(number+5) for number in numbers]

#Bonus: 'primes' variable that returns only the prime numbers in the list
primes = [prime_numbers for numbers in numbers if numbers]
def isPrime(numbers):
    for number in numbers:
        if number > 2 and number %2 == 0
            return number
        else:
            return False
            
