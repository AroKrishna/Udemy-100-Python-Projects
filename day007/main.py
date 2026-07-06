"""
Project : Day 007 - Hangman Game
Imported Modules:
    - art (ASCII art)
    - hangman_words (Word list)
"""

import random
from art import stages, logo
from hangman_words import word_list

print(logo)
chosen_word = random.choice(word_list)
print("Word:",chosen_word)

gameOver = False
lives = 6
placeholder = ""
correct_letters = []

for letter in chosen_word:
    placeholder += "_"
print("Word to guess :",placeholder)

while not gameOver:

    guess = input("Guess a letter: ").lower()

    display = ""
    
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: ",display)
    
    if display == chosen_word:
        print(f" The word was {chosen_word}")
        print("You Win")
        gameOver = True

    if guess not in chosen_word:
        lives -= 1
    
    print(stages[lives])
    print(f"{"*"*30}{lives}/6 LIVES LEFT{"*"*30}")
    
    if lives == 0:
        gameOver = True
