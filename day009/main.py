"""
Project : Day 009 - Secret Auction
Imported Modules : art
"""

from art import logo

print(logo)

data = {}
EndBid = 'False'
while EndBid != True:
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    data[name] = bid
    choice = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
    if choice == 'no':
        EndBid = True
    print("\n" * 100)

highest_bidder = ''
highest_bid = 0
for key in data:
    if data[key] > highest_bid:
        highest_bid = data[key]
        highest_bidder = key

print(f"The winner is {highest_bidder} with a bid of {highest_bid}")
