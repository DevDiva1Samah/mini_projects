# the player must guess a hidden word by guessing once a letter at time 
#each correct guess reveals the positions of the letter in the word
#the player has a limited number of incorrect guesses before the game ends
import random
import string
import words


def get_valid_word(words):

    word = random.choice(words)
    while ' ' in words or '- ' in words:
        word = random.choice(words)       
    
    return word
    

def hangman():