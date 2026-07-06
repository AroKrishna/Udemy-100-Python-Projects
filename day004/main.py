"""
Project : Day 004 - Rock Paper Scissors Game
Imported Modules : art
"""

import random
from art import rock, paper, scissors

def display(a):
    if a == 1:
        print(rock)
    elif a == 2:
        print(paper)
    elif a == 3:
        print(scissors)

endGame = False

while not endGame:
    
    user_choice = 1
    while user_choice in [1,2,3]:
        user_choice = int(input("What do you choose? Type 1 for Rock, 2 for Paper or 3 for Scissors :"))
        if user_choice not in [1,2,3]:
            print("Invalid choice \nEnter Again")
    system_choice = random.randint(1,3)

    print("You chose")
    display(user_choice)

    print("System chose")
    display(system_choice)

    if user_choice == 1 and system_choice == 3:
        print("You Win")
    elif user_choice == 2 and system_choice == 1:
        print("You Win")
    elif user_choice == 3 and system_choice == 2:
        print("You Win")
    elif user_choice == system_choice:
        print("It's a Tie")
    else:
        print("You lose")

    play_again = input("Do you wanna play again (yes/no):").lower()
    if play_again == 'no':
        endGame = True
