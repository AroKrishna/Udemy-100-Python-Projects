"""
Project : Day 005 - Password Generator
"""

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

letter_count = int(input("How many letters would you like in your password? :"))
symbol_count = int(input("How many symbols would you like? :"))
number_count = int(input("How many numbers would you like? :"))

rand_letters = []
rand_symbols = []
rand_numbers = []
unshuffled_pass = []

for item in range(letter_count):
    rand_letters.append(random.choice(letters))

for item in range(symbol_count):
    rand_symbols.append(random.choice(symbols))

for item in range(number_count):
    rand_numbers.append(random.choice(numbers))

unshuffled_pass = rand_letters + rand_symbols + rand_numbers

print(unshuffled_pass)
random.shuffle(unshuffled_pass)

shuffled_password = "".join(unshuffled_pass)

print(unshuffled_pass)

print("Your password is :",shuffled_password)