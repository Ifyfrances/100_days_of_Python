################################
## EXERCISE 1: MODIFY IS LEAP YEAR FCN TO RETURN TRUE IF LEAP AND FALSE IF NOT LEAP YEAR    

# define fcn
def leap_year(year):
    if year % 4 == 0:
        return True
    else:
        return False

print(leap_year(2021))