"""
Project : Day 011 - Blackjack
Imported Modules : art
"""

import random
from art import logo

def deal_cards():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    """Takes a list of cards and returns the calculated score from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    while sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
        
    return sum(cards)

def compare(u_score, c_score):
    """Takes the user score and the computer score to compare them and return the result(Win, Lose, Draw)"""
    if u_score == c_score:
        return "Draw"
    elif c_score == 0:
        return "Lose, opponent has a Blackjack"
    elif u_score == 0:
        return "Win with a Blackjack"
    elif u_score > 21:
        return "You went over. You Lose"
    elif c_score > 21:
        return "Opponent went over. You Win"
    elif u_score > c_score:
        return "You Win"
    else:
        return "You Lose"

def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    is_game_over = False
    
    for _ in range(2):
        user_cards.append(deal_cards())
        computer_cards.append(deal_cards())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:    
            should_deal = input("\nType 'y' to get another card, type 'n' to pass:").lower()
            if should_deal == 'y':
                user_cards.append(deal_cards())
            elif should_deal == 'n':
                is_game_over = True
            else:
                print("Enter a valid option: ")

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_cards())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computers final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    print("\n" * 100)
    play_game()
print("Please Come Again")
