import random
import words
import string 


def get_valid_word(words):   #here where we choosed the secret word

    word = random.choice(words)
    
    while (' ' or ',') in words:  #white and underscores
        return word
    
def Hangman():

    word = get_valid_word(words)   #like here we just call our function
    letters = set(words)
    alaphabet = set(string.ascii_uppercase(words))
    user_letter = ()

    #implement a loop
    while user_guess_letter:    #to do from scratch again!!!!







    f"you have these lives {} and you spent all you chances"
   