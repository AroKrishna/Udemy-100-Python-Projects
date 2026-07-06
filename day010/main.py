"""
Project : Day 010 - Calculator
Imported Modules : art
"""

from art import logo

def add(num1, num2):
    return num1+num2
def sub(num1, num2):
    return num1-num2
def mul(num1, num2):
    return num1*num2
def div(num1, num2):
    return num1/num2

operations = {
    "+" : add,
    "-" : sub,
    "*" : mul,
    "/" : div
}

while True:
    print(logo)
    end_calculation = False
    first_num = float(input("What's the first number?: "))
    while not end_calculation:
        operation_symbol = input("+\n-\n*\n/\nPick an operation ")
        next_num = float(input("What's the next number?: "))
        result = operations[operation_symbol](first_num,next_num)
        print(f"{first_num} {operation_symbol} {next_num} = {result}")
        choice = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
        if choice == 'n':
            end_calculation = True
            print("\n" * 100)
        first_num = result
