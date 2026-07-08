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

from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from border import Border
import time

screen = Screen()
screen.setup(width=600, height=600)
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
def start_game():
    global game_started
    game_started = True
    start_text.clear()

screen.listen()

key_functions = {
    "Up" : snake.up,
    "Down" : snake.down,
    "Left" : snake.left,
    "Right" : snake.right,
    "space" : start_game
}

for key in key_functions:
    screen.onkey(key= key, fun= key_functions[key])

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    if game_started :
        snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh(snake)
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail
    for segment in snake.all_segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
