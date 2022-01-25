############### Blackjack Project #####################
############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.

import random
import os # inorder to use th e clear function
from blackjack_art import logo


def deal_card():
    """returns a random card from the card deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card_dealt = random.choice(cards)
    return card_dealt 

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

def calculate_score(cards):
    """ takes a list o cards and return the score calculated from the cards """
    sum_cards = sum(cards)
    
    #Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) 
    #and return 0 instead of the actual score. 0 will represent a blackjack in our game.
    if len(cards) == 2 and sum_cards == 21:
        return 0
    #Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, 
    # remove the 11 and replace it with a 1. You might need to look up append() and remove().

    if 11 in cards and sum_cards > 21:
        #replace 11 with 1
        sum_cards.pop(11)
        sum_cards.append(1)
        return sum_cards  
#print(calculate_score(user_cards))
#print(calculate_score(computer_cards))
    
#Hint 13: Create a function called compare() and pass in the user_score and 
# computer_score. If the computer and user both have the same score, 
# then it's a draw. If the computer has a blackjack (0), then the user loses. 
# If the user has a blackjack (0), then the user wins. If the user_score is over 21, 
# then the user loses. If the computer_score is over 21, then the computer loses.
# If none of the above, then the player with the highest score wins.

def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over. Uou lose"
    if user_score == computer_score:
        return "It's a draw"
    elif computer_score == 0:
        return "You lose, computer has blackjack"
    elif user_score == 0:
        return "You win with a blackjack!"
    elif user_score > 21:
        return "You went over. You lose"
    elif computer_score > 21:
        return "You Win, your opponent went over"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"
def play_game():
    
    print(logo)  
    
    #Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
    
    user_cards = []
    computer_cards = []
    game_over = False

    for i in range(2):
        # new_card = deal_card(), then append to user and computer card
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    #print("User cards =>", user_cards)
    #print("Computer cards =>",computer_cards)
            
#Hint 11: The score will need to be rechecked with every new card 
# drawn and the checks in Hint 9 need to be repeated until the game ends.
    while not game_over:
        #Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) 
        # or if the user's score is over 21, then the game ends.
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
    #Hint 10: If the game has not ended, ask the user if they want to draw another card. 
    # If yes, then use the deal_card() function to add another card to the user_cards List. 
    # If no, then the game has ended.
        deal_more_cards = input("Do you want to draw another card? Type 'y' to deal or 'n' to pass ")
        if deal_more_cards == 'y':
            user_cards.append(deal_card())
        else:
            game_over = True
    #Hint 12: Once the user is done, it's time to let the computer play. 
    # The computer should keep drawing cards as long as it has a score less than 17.
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    print(f" Your final hand: {user_cards}, final score: {user_score}")
    print(f" Computer's hand: {computer_cards}, final score: {computer_score}")
    
    print(compare(user_score, computer_score))

     
#Hint 14: Ask the user if they want to restart the game. If they answer yes, 
# clear the console and start a new game of blackjack and show the logo from art.py.
restart_game = True
ask_user = input("Do you want to restart the game? 'y' or 'n' ")
while ask_user == "y":
    clear() 
else:
    restart_game = False
print("Goodbye")
play_game()
