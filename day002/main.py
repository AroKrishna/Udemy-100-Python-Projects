"""
Project : Day 002 - Tip Calculator
"""

print("Welcome to the tip calculator!")
total_bill = int(input("What was the total bill? $"))
tip_percentage = int(input("How much tip would you like to give? 10, 12, 15? "))
people = int(input("How many people to split the bill? "))
result = ( total_bill + (total_bill / 100 * tip_percentage) ) / people
print(f"Each person should pay: ${result}")