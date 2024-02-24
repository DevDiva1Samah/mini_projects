import random


def play():

    user = input("choose 'r' for rock, 'p' for paper, 's' for scissors: ")
    computer = random.choice(['r', 'p', 's']) #the computer will choose randomly from these choice

    if user == computer:
        return "it's a tie"

    if is_win(user, computer):
        return 'you won!'
    
    elif is_win(computer, user):  #we don't evenn need that line
        return 'you lost!'

def is_win(player, opponent):

    #return true if the player wins
    # r > s, s > p, p > r 

    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
    



print(play())