from words import commonWords
import random
import string  #Hangman from scratch
               #attach the project with comand line

def get_valid_word(commonWords):

    word = random.choice(commonWords)   #randomly picks up a word from the list
    while ('-' or ' ') in commonWords:
        word = random.choice(commonWords)

    return word

def hangman():
    word = get_valid_word(commonWords)
    word_letters = set(commonWords)   #letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()   #what the user has guessed

    #getting user inpuu
    while len(word_letters) > 0:
        
        #letters used
        #' '.join(['a', 'b', 'cd']) ---> 'a b cd'
        print("you have used these letters", ' '.join(used_letters))
        #what the current word is (ie W - R D)

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word:' ', '.join(word_list))

        user_letter = input("guess a letter:").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
        if user_letter in word_letters:
            word_letters.remove(user_letter)


        elif user_letter in used_letters:
            print("you've used it before, please try again")
    
        else:
            print("Invalid character.please try again.")

# gets here when len(word_letters) == 0


user_input = input('Type something')
print(user_input)
    