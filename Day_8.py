
# You are painting a wall. The instructions on the paint can says that **1 can of paint can cover 5 square meters** of wall. 
# Given a random height and width of wall, 
# calculate how many cans of paint you'll need to buy.

## Area calc
# area = height * width
# coverage = **1 can of paint can cover 5 square meters**
# number of cans = area/coverage

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