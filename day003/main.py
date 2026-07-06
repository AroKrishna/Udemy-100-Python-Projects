"""
Project : Day 003 - Treasure Island
Imported Modules : art
"""

from art import logo

print(logo)
print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
choice1 = input("You're at a cross road. Where do you want to go?\n\tType \"Left\" or \"Right\" :").lower()
if choice1 == 'left':
    print("You've come to a lake. There is an island in the middle of the lake.")
    choice2 = input("\tType 'wait' to wait for a boat. Type 'swim' to swim across: ").lower()
    if choice2 == 'wait':
        print("You arrive at the island unharmed. There is a house with 3 doors: ")
        choice3 = input("\tOne red, one yellow and one blue. Which colour do you choose :").lower()
        if choice3 == 'red':
            print("It's a room full of fire.")
        elif choice3 == 'blue':
            print("You enter a room of beasts.")
        elif choice3 == 'yellow':
            print("You found the treasure!\nYou Win!")
            exit()
        else:
            print("Game Over.")
    else:
        print("You get attacked by an angry trout.")

else:
    print("You fell into a hole.")

print("Game Over")
