"""
Project : Day 015 - Coffee Machine Project 
"""

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

def are_resources_sufficient(drink):
    """Takes the choice of drink and checks whether the available resources are sufficient"""
    for ingredient in drink["ingredients"]:
        if resources[ingredient] < drink['ingredients'][ingredient]:
            print(f"Sorry there is not enough {ingredient}")
            return False
    return True

def is_transaction_successful(money, price):
    """Returns whether transaction is successfull."""
    if money >= price:
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        return False
    
def process_payment(money, price):
    """Processes the payment and updates the resources."""
    resources["money"] += price
    if money > price:
        print(f"Here is ${money - price:.2f} dollars in change.")

def prepare_coffee(drink):
    """Takes the choice of the drink and updates the available resources"""
    for ingredient in drink["ingredients"]:
        resources[ingredient] -= drink["ingredients"][ingredient]

working = True
while working:
    choice = input("What would you like? (Espresso - $1.5, Latte - $2.5, Cappuccino - $3.0) :").lower()
    if choice == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money : ${resources['money']:.2f}")
    elif choice == 'off':
        working = False
    elif choice in MENU:
        drink = MENU[choice]
        if are_resources_sufficient(drink):
            print("Please insert coins.")
            quarters = int(input("How many quarters:"))
            dimes = int(input("How many dimes:"))
            nickels = int(input("How many nickels:"))
            pennies = int(input("How many pennies:"))
            total = 0.25*quarters + 0.1*dimes + 0.05*nickels + 0.01*pennies
            if is_transaction_successful(total, drink['cost']):
                process_payment(total, drink['cost'])
                prepare_coffee(drink)
                print(f"Here is your {choice} ☕. Enjoy!")
    else:
        print("Invalid choice. Please choose a valid option from the MENU!  ")
