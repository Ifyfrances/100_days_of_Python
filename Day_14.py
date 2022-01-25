from h_vs_l_art import logo, vs
from h_vs_l_game_data import data
import random
#from replit import clear

def get_random_account():
    """Get data from random account"""
    return random.choice(data)

def format_data(account):
    
    """Format acount data to printable format"""
    # create a function to avoid repeating for both a and b
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"

def check_answers(guess, a_followers, b_followers):
    """Check followers agianst user's guess and returns True if they got it right
    Or False if the got it wrong"""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"
# display art
def game():
    print(logo)
    score = 0
    game_should_continue = True
    
    # generate random account from game data
    account_a = get_random_account()
    account_b = get_random_account()

    while game_should_continue:
        account_a  == account_b
        account_b = get_random_account()
        
        while account_a == account_b:
            account_b = get_random_account()

    # format acount data to printable format
    # create a function to avoid repeating for both a and b
    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Compare B: {format_data(account_b)},")

    # ask user to guess
    guess = input("Who has more followers? Type 'A' or 'B' : ").lower()

    # check if guess is correct or not 
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    
    #give user feedback if they are right or wrong
    is_correct = check_answers(guess, a_follower_count, b_follower_count)
    
    clear()
    print(logo)
    
    #track score
    if is_correct:
        score += 1
    #the game repeats itself when guessed correctly
    # make account at position B go to position A
    # the game resets after each round. whether wrong or right
        print(f"You're right! Current score: {score}.")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final score: {score}")
game()
