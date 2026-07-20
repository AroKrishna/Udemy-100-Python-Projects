"""
Project : Day 20 & 21 - Snake Game

Standard Library Modules:
    - turtle
    - time

Local Modules:
    - snake
    - food
    - scoreboard
    - border
"""


import time
from turtle import Turtle, Screen

from snake import Snake
from food import Food
from scoreboard import Scoreboard
from border import Border


screen = Screen()
screen.setup(width=600, height=650)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food(snake)
scoreboard = Scoreboard()
border = Border()

# Displays the start message
start_text = Turtle()
start_text.hideturtle()
start_text.color("white")
start_text.penup()
start_text.goto(0,20)
start_text.write(
    "Press SPACE BAR to Start",
    align="center",
    font=("Courier", 20, "bold")
)

game_started = False
game_over = False

def start_game():
    global game_started, game_over

    if game_over:
        snake.reset()
        food.refresh(snake)
        scoreboard.clear_game_over()
        game_over = False

    game_started = True
    start_text.clear()

def quit_game():
    global game_is_on
    game_is_on = False
    screen.bye()

screen.listen()

key_functions = {
    "Up" : snake.up,
    "Down" : snake.down,
    "Left" : snake.left,
    "Right" : snake.right,
    "space" : start_game,
    "Escape" : quit_game
}

for key, function in key_functions.items():
    screen.onkey(function, key)

game_is_on = True
while game_is_on:

    screen.update()
    time.sleep(0.1)

    if game_started:
        snake.move()

        # Detect collision with food
        if snake.head.distance(food) < 15:
            food.refresh(snake)
            snake.extend()
            scoreboard.increase_score()

        # Detect collision with wall or tail
        if snake.hit_wall() or snake.hit_tail():
            scoreboard.reset()
            game_started = False
            game_over = True
            scoreboard.game_over()
