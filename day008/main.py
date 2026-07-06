"""
Project : Day 008 - Caesar Cipher
Imported Modules : art
"""

from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

def caeser(original_text, shift_amount, encode_or_decode):
    output_text=''
    if encode_or_decode == 'decode':
        shift_amount *= -1

    for letter in original_text:
        if letter not in alphabet:
            output_text += letter
        else:
            letter_index = alphabet.index(letter)
            output_text += alphabet[letter_index+shift_amount]

    print(f"Here is the {encode_or_decode}d result: {output_text}")

choice = 'yes'
while choice == 'yes':
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:").lower()
    text = input("Type your message:").lower()
    shift = int(input("Type the shift number:"))
    shift = shift%24
    caeser(text,shift,direction)
    choice = input("Type 'yes' if you want to go again. Otherwise, type 'no':" ).lower()
