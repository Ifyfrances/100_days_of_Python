# print("Hello World!")

# This code prints the number of characters in a user's name.
"""
name = input('what is your name? ')
print(name)

s = len(name)
print(s)
"""
#EX 2
# print( len( input( "what is your name? ") ) ) 
# add space after ? inorder to have space when function prints question

"""
#Ex 3
# Instructions
# Write a program that switches the values stored in the variables a and b.
# 🚨 Don't change the code below 👇
a = input("a: ")
b = input("b: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

# b = input("a: ")
# a = input("b: ")

c= a
a =b
b= c

#Write your code above this line 👆
####################################

# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)
"""

# Variable quiz
time_until_midnight = "5"
print("There are" + " " + time_until_midnight  + " " + "hours until midnight")

#####################
# PROJECT FOR DAY 1: BAND NAME GENERATOR

from time import sleep
#1. Create a greeting for your program.
print("Hello, Welcome to the Band Name Generator"); sleep(2)
#2. Ask the user for the city that they grew up in.
print("To generate a band name, I will be asking you a few questions"); sleep(2) 
city = input("What city did you grow up in? \n")
#print(city)
#3. Ask the user for the name of a pet.
#input("Do you have a pet? "); sleep(2)
pet_name = input("What is the name of a pet? \n") ; sleep(2)
#print(pet_name)
#4. Combine the name of their city and pet and show them their band name.
print("Your Band Name is" + " " + city+pet_name )
#5. Make sure the input cursor shows on a new line, see the example at:
#   https://band-name-generator-end.appbrewery.repl.run/
