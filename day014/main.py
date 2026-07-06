"""
Project : Day 014 : Higher Lower Game
Imported Modules:
    - data
    - art
"""

from random import choice
from Day014.data import data
from Day014.art import logo, vs

def compare(a_followers, b_followers, user_guess):
    """Takes the follower count and the user's guess and return if they got it right."""
    if a_followers > b_followers:
        return user_guess == 'a'
    else:
        return user_guess == 'b'

def game():
    game_over = False
    score = 0
    completed_names = []

    dict_a = choice(data)
    completed_names.append(dict_a['name'])
    print(logo)
    while not game_over:

        available_names = [item for item in data if item['name'] not in completed_names]

        if not available_names:
            print("Congratulation! You've completed the game!")
            print(f"Final Score : {score}")
            break

        dict_b = choice(available_names)
        completed_names.append(dict_b['name'])
        
        print(f"Compare A: {dict_a['name']}, a {dict_a['description']}, from {dict_a['country']}.")
        print(vs)
        print(f"Against B: {dict_b['name']}, a {dict_b['description']}, from {dict_b['country']}.")

        user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        print("\n"*100)
        print(logo)
        result = compare(dict_a['follower_count'],dict_b['follower_count'],user_guess)
        if result:
            score += 1
            print(f"You're right! Current score: {score}.")
            dict_a = dict_b            
        else:
            game_over = True
            print(f"Sorry, that's wrong. Final score: {score}")

play_again = 'y'
while play_again == 'y':
    game()
    play_again = input("Do you want to play again ? (y/n) :").lower()
    if play_again == 'y':
        print("\n"*100)