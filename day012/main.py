"""
Project : Day 012 - Number Guesser
Imported Modules : art
"""

from random import randint
from art import logo

EASY_DIFFICULTY_TURNS = 10
HARD_DIFFICULTY_TURNS = 5

def set_difficulty(difficulty):
    """Inputs the difficulty and returns the number of turns."""

    if difficulty == 'easy':
        return EASY_DIFFICULTY_TURNS
    else:
        return HARD_DIFFICULTY_TURNS

def compare(user_choice, computer_choice, attempts):
    """Compares the user_choice and the computer_choice and returns the number of attempts left."""

    if user_choice > computer_choice:
        print("Too High")
    elif user_choice < computer_choice :
        print("Too Low")
    else:
        print(f"You got it! The answer was {user_choice}.")
        return attempts
    print("Guess Again")
    return attempts - 1

def game():
    """The main game function which ends if turns = 0 or number has been guessed"""
    
    print(logo)

    chosen_number = randint(1,100)
    
    print("Welcome to the Number Guessing Game !\nI'm thinking of a number between 1 and 100.")
    turns = set_difficulty(input("Choose a difficulty. Type 'easy' or 'hard':").lower())
    guess = 0
    while guess != chosen_number:
        print(f"You have {turns} remaining to guess the number")
        guess = int(input("Make a guess: "))
        turns = compare(guess,chosen_number,turns)
        if turns == 0:
            print("You've run out of guesses.")
            return

playAgain = 'yes'
while playAgain == 'yes':
    game()
    playAgain = input("Do you wanna play again ? (yes/no) :").lower()
    if playAgain == 'yes':
        print("\n"*100)
