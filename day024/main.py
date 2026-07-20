"""
Project : Day 24 - Mail Merge
"""

PLACEHOLDER = "[name]"

with open("Input/Letters/starting_letter.txt") as letter_file:
    letter = letter_file.read()

with open("Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

for name in names:
    striped_name = name.strip()
    with open(f"Output/ReadyToSend/letter_for_{striped_name}.txt", "w") as completed_letter:
        edited_letter = letter.replace(PLACEHOLDER, striped_name)
        completed_letter.write(edited_letter)
