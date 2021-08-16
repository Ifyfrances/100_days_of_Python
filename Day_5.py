#######################
# FOR LOOP
# Loops to execute the same line of code multiple times
'''
fruits = ["Apple", "Peach", "Pear"]
#fruits = fruits.split(", ") # converts fruits to string
for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")
'''
###################################
###################################
# EXERCISE 1
# Calcualte Average Height for students

# average_height = sum(student_heights)/total number of students
'''
student_heights = [180, 124, 165, 173, 189, 169, 146]
total_height = 0
number_students = 0
for height in student_heights:
    total_height = total_height + height
print(total_height)
    
for student in student_heights:
    number_students += 1
print(number_students)  

average_height = round(total_height/number_students)
print(average_height)
'''
#########################################
#########################################
'''
# EXERCISE 2
# Find the highest score

student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
highest_score = 0

for score in student_scores:
    if score > highest_score:
        highest_score = score
print(highest_score)
'''
#######################################
#######################################
# Range(start, stop, steps), stop-specified stop excludes the sprcified number
# EXERCISE 3
'''
total = 0
for number in range(1, 101): # number between 1 to 10 excluding 10
    total += number
print(total)
 
# You are going to write a program that calculates the sum of 
# all the even numbers from 1 to 100 
# Thus, the first even number would be 2 and the last one is 100

sum_even = 0

for number in range(2, 102, 2):
  # print(number)
  sum_even += number
print(sum_even)
'''   
########################################################
########################################################
# EXERCISE 4
# write a program that automatically prints the solution to the FizzBuzz game.
# Your program should print each number from 1 to 100 in turn.
# When the number is divisible by 3 then instead of printing the number it should print "Fizz".
# `When the number is divisible by 5, then instead of printing the number it should print "Buzz".` 
# `And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"`
'''
for number in range(1, 101):
    #print(number)
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
'''
################################################
################################################
# You are going to write a program that calculates the sum of 
# all the even numbers from 1 to 100 inclusive
# Thus, the first even number would be 2 and the last one is 100
'''
sum_even = 0

# even numbers are numbers when divided by 2 has no remainder
for number in range(2, 101):
    if number % 2 == 0:
        sum_even = sum_even + number
print(sum_even)
print("The sum of even number between 1 to 100 is", sum_even)

# OR
sum_even = 0

for number in range(2, 101, 2):
  # print(number)
  sum_even += number
print("The sum of even number between 1 to 100 is", sum_even)

'''
################################################################
################################################################
# DAY 5 PROJECT
# Build PyPassword Generator

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# create an empty list to store the selected random numbers or symbols
# using a list in order to be able to shuffle the numbers and avoid following a sequence

password_list = []

for letter in range(1, nr_letters + 1):
    random_letter = random.choice(letters)
    password_list.append(random_letter)
for symbol in range(1, nr_symbols + 1):
    random_symbol = random.choice(symbols)
    password_list.append(random_symbol)
for number in range(1, nr_numbers + 1):
    random_number = random.choice(numbers)
    password_list.append(random_number)
print(password_list) # prints password but as list

# shuffle the list
random.shuffle(password_list)
print(password_list)

# convert the list to regular strings

# create empty list
password = ""

for char in password_list:
    password = password + char
print("Your password is", password)


