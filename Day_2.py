
## DATA TYPES

"""
num_char = len(input("what is your name? "))
#the output of num_cahr is integer hence, cant be concatenated with a string
# the best option is to cast it or convert it to a string before printing
new_num_char = str(num_char) # cast integer data type to a string
print("the length of you name is " + new_num_char + " charcters")


# Write a program that adds the digits in a 2 digit number. 
# e.g. if the input was 35, then the output should be 3 + 5 = 8

# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆
print(type(two_digit_number))

# convert the two digits inputed into int by slicing using their subscript
# stings can be accesed using subscript, using input function turns it to a string
first_digit = int(two_digit_number[0]) # first digit has subscript zero
second_digit = int(two_digit_number[1]) # 2nd digit will take 1 as subscript

# add the two digits
two_digit_number =  first_digit + second_digit
print(two_digit_number)
"""
####################################

# MATHEMATICAL FUNCTIONS
# Whenever you are dividing you always get floating point number
# you can add .0 to the denominator to cancel the float
# 2 to the power of 2 can be 2 ** 2 (** is used for exponent)
# PEMDAS (Parenthesis, Exponents, Multiplication, Division, Addition, Substraction)
# in actual division, python goes from Left to Right. not minding the function there
# moving from left to right, python prioritises parenthesis()

#################################################
"""
Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
The BMI is a measure of some's weight taking into account their height. e.g. If a tall person and a short person both weigh the same amount, the short person is usually more overweight.
"""
# The BMI is calculated by dividing a person's weight (in kg) 
# by the square of their height (in m):

# expected output (weight_kg/(height_m)**2)

height = input("What is your height in meters (m)?: ")
weight = input("What is your weight in Kg?: ")

# cast data type to float
height = float(height)
weight = int(weight)

#calcualte BMI
BMI = (weight/(height ** 2))
BMI_as_int = int(BMI) # gives a calculation that is not a float
BMI_as_int = str(BMI_as_int) # in order to concatenate it with string, you cast type as string

#print results
print("Your Body Mass Index is " + BMI_as_int) 


#########
# using int removes the numbers after the decimal place, 
# hence it is better to use the round() to round it to nearest whole number
# or to desired number of figures round(2)
# //(flow division)= can also be used to remove floats during division 
# modulus(%) gives the remainder as output
# +=, -=, /= if you manipulate a value based on its previous value

"""
# f-string is used instead of converting values into string before concatenating
# f-string is used together with {} ({to input variables into a string})
score = 0
height = 1.8
Iswinning = True
print(f"Your score is {score}, your height is {height}, you are winning is {Iswinning}")
"""

"""
# DAY2 PROJECT
# Create a program using maths and f-Strings 
# that tells us how many days, weeks, months we have left if we live until 90 years old.
# It will take your current age as the input and output a message with our time left in this format:
# OUTPUT: You have x days, y weeks, and z months left. 

# input current age
current_age = input("How old are you? ")

# postulated year
week_year = 52
month_year = 12
days_year = 365
# cast age as int from current age
current_age = int(current_age)
remaining_years = 90 - current_age
weeks_remaining = remaining_years * 52
days_remaining = remaining_years * 365
months_remaining = remaining_years * 12
print(remaining_years, weeks_remaining, days_remaining, months_remaining)
print(f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months remaining")
"""
# DAY 2 PROJECT 2
#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python

# Write a code that calcualtes Tip
from time import sleep
print("Welcome to Tip Calculator"); sleep(1)
bill = input("What is the total amount spent? $" )
tip_percent = input("What percentage of tip would you like to give?  10, 15, 20? ")

# convert bill to float and tip to int
bill = float(bill)
tip_percent = int(tip_percent)
tip_percentage = (bill * tip_percent)/100
print(tip_percentage)
total_bill = round(bill + tip_percentage, 2) # round accepts 2 arguments round(number to be rounded, number of decimals)
# bill with_tip = tip_percent / 100 * bill + bill

# how much will each person pay
num_persons = input("How many people will split the bill? ")
#each person pays
num_persons = int(num_persons)
each_person = total_bill/num_persons
each_person = "{:.2f}".format(each_person)
print(f"Each persons should pay ${each_person} ")

# answer is $33.6
# $33.60 can be achieved using .format function to add 0 at the back of 6
# "{:.2f}".format(each_person)