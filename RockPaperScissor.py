import random

def play():
    user = input("What's your choice?'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return "It's a tie!"

    winning_combinations = {
        'r': 's',
        'p': 'r',
        's': 'p',
    }

    if user in winning_combinations and winning_combinations[user] == computer:
        return "You won!"

    return "You lost!"


