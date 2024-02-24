import random


def guess_number(x):

    random_number = random.randint(0, x)
    guess = 0
    while guess != random_number:
        guess = int(input("guess a number to be compared from  to x: "))
        if guess > random_number:
            print("oups! it's too high")
        elif guess < random_number:
            print("oups! you guessing is too high")
        
    
    print("yaaay you're on the top of the world")

def computer_guess(x):
                        #random.randint throws an error if arg1 = arg2
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  #could be high b/c  low = high 
        feedback = input(f"is {guess} too high (H), too low (L), or correct 'c'")
        if feedback == 'H':
            high = guess - 1
        elif feedback == 'L':
            low = guess + 1
    print("yay the computer guessed your number, {guess}, correctly! ")

guess_number(7)
computer_guess(7)