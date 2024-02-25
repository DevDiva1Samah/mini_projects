import random
import words
import string



def guess_valid_word(words):

    word = random.choice(words)
    user = input("guess a valid word that exists in words").upper()

    while (' ' or ',') in words:
        return word
    
def 