##################
## if/else/nested statement
# Exercise 1: check if a number is Even or Odd number
# # 🚨 Don't change the code below 👇
# number = int(input("Which number do you want to check? "))
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# if number % 2 == 0:
#   print("This is an even number")
# else:
#   print("This is an odd number")

# ######################################################
# # Exercise 2
# # Improve the BMI calculator to give BMI classification, based on the persons BMI
# # 🚨 Don't change the code below 👇
# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# BMI = round(weight / (height ** 2))

# # print output
# # print("Your BMI is ", BMI)

# # give conditions to interprete BMI
# if BMI <  18.5:
#   print("According to the BMI chart, you are underweight")
# elif BMI < 25:
#   print(f"Your BMI is {BMI}, you have a normal weight") 
# elif BMI < 30:
#   print(f"Your BMI is {BMI}, you are slightly overweight")
# elif BMI < 35:
#   print(f"Your BMI is {BMI}, you are obese, work on your weight")
# else:
#   print(f"Your BMI is {BMI}, you are clinically obese, seek medical attention")

# ######################################
# # Exercise 3:
# # calculate if year is Leap or Not
# # 🚨 Don't change the code below 👇
# year = int(input("Which year do you want to check? "))
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# if year % 4 == 0:
#   print(year, "is Leap year")
# elif year % 100 == 0:
#   print(year, "is Leap year")
# elif year % 400 == 0:
#   print(year, "is Leap year")
# else:
#   print(year, "is not a Leap year")

# ######################################################
# # print rollerccoaster price based on age and height
# # exercise 4
# print("Welcome to the Rollercoaster!")
# Height = float(input("What is your Height? "))
# price = 0

# # define acceptable height
# if Height >= 120:
#   print("Congratulations you are qualified to take a ride")
#   age = int(input("how old are you? "))
#   if age < 12:
#     price = 5
#     print("Child ticket price is $", price)
#   elif age <= 18:
#     price = 7
#     print("Youth ticket price is $", price)
#   elif age >= 45 and age <= 55:
#     print("This one is on us!! You have a free ride!")
#   else:
#     price = 12
#     print("Adult ticket price is $",price)
#   want_photo = input("Do you want a picture? [y or n] ")
#   if want_photo == "y":
#     price += 3
#     print("Your ticket price is $", price)
#   else:
#     print("Thanks for your patronage! Enjoy your ride!")
# else:
#     print("Sorry, comeback when you have grown taller")

"""
#####################################
# exercise 5
#  create automatic pizza order program

# pizza orices in $
Small_Pizza = 15
Medium_Pizza = 20
Large_Pizza = 25

# extra toppings
Pepperoni_for_Small_Pizza  = +2
Pepperoni_for_Medium_or_Large_Pizza = +3
Extra_cheese_for_any_size_pizza = +1

pizza_sizes = 'L', 'M', 'S'

price = 0

# print welcome message
print("Welcome to Python Pizza deliveries, can I take your order please!")
size = input("What Pizza size do you want? [l, m, s] ")

if size == "l":
    price += Large_Pizza
    print("Large pizza costs $", Large_Pizza)
elif size == "m":
    price += Medium_Pizza
    print("Medium pizza costs $", Medium_Pizza)
else:
    price += Small_Pizza
    print("Small pizza costs $", Small_Pizza)
want_pepperoni = input("Do you want Pepperoni? [y/n]")
if want_pepperoni == "y":
    if size == "s":
        price = price + 2
        print("Total price is", price)
    else:
        price = price +  3
        print("Total price is", price)
else:
    print("Your total bill is $", price)

want_cheese = input("Do you want extra cheese? [y/n]")
if want_cheese == "y":
    price = price +  1
    print("Total price is $", price)
else:
    print("Your total bill is $", price)

"""
#######################################
# DAY 3 PROJECT
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************
''')
from time import sleep
print("Welcome to Treasure Isalnd."); sleep(2)
print("Your mission is to find the treasure."); sleep(2)
move_1 = input("You\'re at a crossroad, which way do you want to go? Left or Right [L/R] "); sleep(2)
move_1 = move_1.lower()

if move_1 == "l":
    print("you are getting closer to the treasure!"); sleep(2)
    move_2 = input("You\'ve come to a lake, there is an Island in the middle. Do you want to swim or wait for the boat?[S/W] "); sleep(2)  
    move_2.lower()
    if move_2 == "w":
        print("You made it safely on the Island")
        print("You are closer than you think..."); sleep(2)
        move_3 = input("You have three doors, Red, Blue, Yellow [R, B, Y], which one is it? "); sleep(2)
        move_3.lower()
        if move_3 == "r":
            print("Fire!! You are burned by fire!!"); sleep(2)
            print("Game Over!")
        elif move_3 == "b":
            print("You were eaten by a Godzilla"); sleep(2)
            print("Game Over"); sleep(2)
        else:
            print("You found the Treasure!!"); sleep(2)
            print("You Won!!"); sleep(2)
    else:
        print("Ooops sorry..you have been attacked by a Shark!"); sleep(2)
        print("Game Over!")   ; sleep(2)
else:
  print("You fell into a hole, Game Over!"); sleep(2)

