import random

# create list to pick from
# word_list = ["aardvark", "baboon", "camel"]
from hangman_words import word_list

# - Randomly choose a word from the word_list 
# and assign it to a variable called chosen_word
chosen_word = random.choice(word_list)


# create an empty list called display
display = []

#- Ask the user to guess a letter and 
# assign their answer to a variable called guess. Make guess lowercase.
guess = input("Guess a letter: ").lower()
word_length = len(chosen_word)

# set lives to the number of times to draw the hangman
lives = 6

from hangman_art import logo
print(logo)
# For each letter in the chosen_word, add a "_" to 'display'.
# So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] 
# with 5 "_" representing each letter to guess.

for _ in range(word_length):
    display += "_"
# print(display)    

# - Use a while loop to let the user guess again. The loop should only stop once the user 
# has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). 
# Then you can tell the user they've won.

end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    
# check guesses letter  
# Loop through each position in the chosen_word;
# If the letter at that position matches 'guess' then reveal 
# that letter in the display at that position.
# e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #- If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1. 
    #If lives goes down to 0 
    # then the game should stop and it should print "You lose.    
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose")
# Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

#- Check if the letter 
# the user guessed (guess) is one of the letters in the chosen_word.

# print(display)    

if "_" not in display:
    end_of_game = True
    print("You won")

from hangman_art import stages
print(stages[lives])