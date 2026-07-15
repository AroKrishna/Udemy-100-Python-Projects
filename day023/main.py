"""
Project : Day 23 - Turtle Crossing Game

Standard Library Modules:
    - time
    - turtle

Local Modules:
    - player
    - car_manager
    - scoreboard
    - border
"""

import time
from turtle import Turtle, Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from border import Border

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Crossing Game")

player = Player()
scoreboard = Scoreboard()
border = Border()
car_manager = CarManager()

# Displays the starting text
start_text = Turtle()
start_text.hideturtle()
start_text.penup()
start_text.goto(0,0)
start_text.write(
        "Press SPACE BAR to Start",
        align="center",
        font=("Courier", 20, "bold")
    )
screen.update()

def start_game():
    start_text.clear()
    screen.onkeypress(key= "space", fun= None)
    game_is_on = True
    while game_is_on:
        time.sleep(0.1)
        screen.update()
        car_manager.create_car()
        car_manager.move_cars()

        # Detect collision with car
        for car in car_manager.all_cars:
            if player.distance(car) < 20:
                game_is_on = False
                scoreboard.game_over()

        # Detect successful crossing
        if player.has_finished():
            scoreboard.update_level()
            player.goto_start()
            car_manager.clear_cars()
            car_manager.speed_up()

screen.listen()
screen.onkeypress(key= "Up", fun= player.go_up)
screen.onkeypress(key= "space", fun= start_game)

screen.exitonclick()
