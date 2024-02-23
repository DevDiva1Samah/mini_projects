import random
import math


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = input("guess a number between 1 and {x}: ")
        if guess < random_number:
            print("sorry, guess again. too low")
        elif guess > random_number:
            print("sorry, too high!")
        
        print("Yay! congrats! you have guessed the number {random_number}")

guess(10)