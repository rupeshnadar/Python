#!python3

# Game: Rock Paper Scissors

import random
import sys

choice = ["rock", "paper", "scissors"]

def winner(computerChoice, userChoice):
    result = "lost"
    if userChoice == computerChoice:
        result = "tie"
    if computerChoice == "rock" and userChoice == "paper" or \
        computerChoice ==  "paper" and userChoice == "scissors" or \
        computerChoice == "scissors" and userChoice == "rock":
        result = "won"
    return result

def play():
    # get input from user
    userChoice = None
    while userChoice not in choice:
        userChoice = input("Enter your choice: ")

        # check if user wants to quit
        if userChoice == "quit":
            sys.exit()

    computerChoice = random.choice(choice)

    # output result
    print(f"Computer chose: {computerChoice}")
    print(f"You {winner(computerChoice, userChoice)}\n\n")

if __name__ == "__main__":
    while True:
        play()

