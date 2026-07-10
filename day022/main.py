"""
Project : Day 22 - Ping Pong Game

Standard Library Modules:
    - turtle
    - time

Local Modules:
    - paddle
    - ball
    - scoreboard
    - border
"""

from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from border import Border
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.title("Ping Pong Game")
screen.bgcolor("black")
screen.tracer(0)

screen.listen()

left_paddle = Paddle(-350,0)
right_paddle = Paddle(350,0)
ball = Ball()
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

key_functions = {
    "Up" : right_paddle.go_up,
    "Down" : right_paddle.go_down,
    "w" : left_paddle.go_up,
    "s" : left_paddle.go_down,
    "space" : start_game
}

for key in key_functions:
    screen.onkeypress(key= key, fun= key_functions[key])

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)

    if game_started:
        ball.move()

    # Detect collision with the top and bottom walls.
    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.bounce_y()
    
    # Detect collision with left paddle
    if ball.x_move < 0 and -350 <= ball.xcor() <= -330 and ball.distance(left_paddle) < 50:
        ball.bounce_x()
    
    # Detect collision with right paddle
    if ball.x_move > 0 and 330 <= ball.xcor() <= 350 and ball.distance(right_paddle) < 50:
        ball.bounce_x()
    
    # Ball misses right paddle
    if ball.xcor() > 380 :
        ball.reset_position()
        scoreboard.left_point()

    # Ball misses left paddle
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.right_point()
    
screen.exitonclick()
