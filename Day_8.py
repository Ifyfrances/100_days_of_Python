
# You are painting a wall. The instructions on the paint can says that **1 can of paint can cover 5 square meters** of wall. 
# Given a random height and width of wall, 
# calculate how many cans of paint you'll need to buy.

## Area calc
# area = height * width
# coverage = **1 can of paint can cover 5 square meters**
# number of cans = area/coverage
'''
import math

# Ask the user for random height and width input using the input function
# convert it to integer
height = int(input("What is the height of the wall in m? "))
width = int(input("What is the width of the wall in m? "))
coverage = 5

# define a function that does the calculation
def paint_calc(height, width, coverage):
    area = height * width
    num_of_cans = math.ceil(area/coverage)  # covert to nearest whole number, aints are not sold in decimals
    # import math and use ceil
    print(f"You will need {num_of_cans} number of cans")
paint_calc(height, width, coverage)
'''

##############################################################
# Prime Numbers
# write a function that checks whether if the number pssed into it is a prime number or not
'''
num = int(input("Check this number: "))
def if_prime(num):
    Is_prime = True
    for i in range(2, num):
        if num % i == 0:  # clearly not a primer number
            Is_prime = False
            #print(f"{num} Is a prime number")
    if Is_prime:
        print(f"{num} is a Prime number")
    else:
        print(f"{num} Is not a Prime number")
if_prime(num)
'''
##############################################################
##############################################################

## Ceasar Cipher  - Text Encryption Project
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z''a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt or 'decode' to decrypt:\n")
text = input("What word do you want to encrypt?\n")
shift = int(input("Type the desired number of shifts:\n"))

def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"The encrypted text is {cipher_text}")

## Ceasar Cipher2  - Text decryption Project
def decrypt(cipher_text, shift_amount):
    plain_text = ""
    for letter in cipher_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        new_letter = alphabet[new_position]
        plain_text += new_letter
    print(f"The decrypted text is {cipher_text}")
    
if direction == "encode":
    encrypt(plain_text=text, shift_amount=shift)   
else:
    decrypt(cipher_text=text, shift_amount=shift)

# call the two function
encrypt(plain_text=text, shift_amount=shift)       
decrypt(cipher_text=text, shift_amount=shift)

## ## Ceasar Cipher 3  - Re-organise code to merge both into a single function

# Combine the encrypt() and decrypt() functions into a single function called caesar(). 

def caesar(input_text, shift_amount, cipher_direction):
    start_text = ""
    for letter in input_text:
        position = alphabet.index(letter)
        if cipher_direction == "encode":
          new_position = position + shift_amount
        else:
          new_position = position - shift_amount
        start_text += alphabet[new_position]
    print(f"The {cipher_direction}d text is {start_text}")  

#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
caesar(input_text=text, shift_amount=shift, cipher_direction=direction)
       
  ## ## Ceasar Cipher 4  - Re-organise to retain characters, spaces and numbers as inputed
def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"Here's the {cipher_direction}d result: {end_text}")

## Import and print the logo from art.py when the program starts.
from art import logo
print(logo) 

## ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.

should_continue = True
while should_continue:

  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n")) 
   
  
## What if the user enters a shift that is greater than the number of letters in the alphabet?
  shift = shift % 26
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

  result = input("Type 'yes' if you want to go again. Otherwise type 'no'\n")
  if result == 'no':
    should_continue = False
    print("Goodbye")
    
