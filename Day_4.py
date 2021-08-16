##############################################
##############################################
# You are going to write a program which will select a random name from a list of names. 
# The person selected will have to pay for everybody's food bill.
# Bankers Roulette
'''
import random
from time import sleep
print("Welcome to Bankers Roulette!");sleep(1)
print("Let\'s find out who is going to pay the bills today!");sleep(1.5)
# Split string method
names_string = input("Give me everybody's names, separated by a comma.\nAdd a space after the comma: ")
names = names_string.split(", ")

#Write your code below this line 
#print(names)
#count names entered
num_names = len(names)
#print(num_names)
# pick random number
random_choice = random.randint(0, num_names - 1 )
#print(random_choice)
who_will_pay = names[random_choice]
print(who_will_pay, "is going to buy the meal today!")

# who will pay = random.choice(names)

'''
###################################################
###################################################
# Treasure Map
# Don't change the code below 
'''
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# Don't change the code above 

#Write your code below this row 
# when a number is input, e.g.23 
# 2=horizontal row selected, 3=vertical column selected
horizontal = int(position[0]) # wrap into int to convert str to int so that python can process it
vertical = int(position[1]) # columns

row_selected = map[vertical - 1]
row_selected[horizontal - 1] = "X"


#Write your code above this row 

# Don't change the code below 
print(f"{row1}\n{row2}\n{row3}")
'''
#################################################
#################################################
# CREATE ROCK, PAPER, SCISSORS GAME 

'''
import random
print("Welcome to Rock, Paper, Scissors")
print()
rock = '''
Rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
Paper
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
Scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print(rock, paper, scissors)
print()
print("Rules of the Game:")
print("Rock wins against scissors.\nScissors wins against paper.\nPaper wins against rock.")
print()

minNum = 0
maxNum = 2

choices = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors\n"))

if user_choice < minNum or user_choice > maxNum:
  print("You typed invalid number, you lose!")
else:
  print("You choose:")
  print(choices[user_choice])
    
  random_index = random.randint(0, 2)
  cpu_choice = random_index
  print("Computer chose:")
  print(choices[cpu_choice])

  if user_choice == 0 and cpu_choice == 2:
    print("You win!")
  elif cpu_choice == 0 and user_choice == 2:
    print("You loose")
  elif cpu_choice > user_choice:
    print("You loose")
  elif user_choice > cpu_choice:
    print("You win!")
  elif cpu_choice == user_choice:
    print("It's a draw")
'''
###########################################################
###########################################################