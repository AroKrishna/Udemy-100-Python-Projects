"""
Project : Day 19 - Turtle Race
Modules Used:
    - turtle
    - random
"""

from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(width=500, height=400)

colors = ["red", "yellow", "orange", "green", "blue", "purple"]
no_of_turles = len(colors)
all_turtles = []
start_y = -100
finish_line = 220
is_race_on = False

def move_random_distance():
    """All the turtles will move forward a random distance."""
    for current in range(no_of_turles):
        random_distance = randint(0,10)
        all_turtles[current].forward(random_distance)

def race():
    is_race_on = True
    while is_race_on:
        move_random_distance()
        for current in range(no_of_turles):    
            if all_turtles[current].xcor() > finish_line:
                is_race_on = False
                winner = all_turtles[current].fillcolor()
    print("Race Ended")
    print(f"The Winner is {winner} turtle.")
    print(f"You bet on {user_bet}")
    if winner == user_bet:
        print("You won")
    else:
        print("You lost")

for current in range(no_of_turles):
        new_turtle = Turtle("turtle")
        new_turtle.penup()
        new_turtle.color(colors[current])
        new_turtle.goto(x=-230, y=start_y+current*40)
        all_turtles.append(new_turtle)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a colour:")

if user_bet:
    race()
else:
    print("User did not bet")

screen.exitonclick()
