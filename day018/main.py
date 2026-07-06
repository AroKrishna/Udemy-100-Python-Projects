"""
Project : Day 18 - Hirst Painting
Modules Used:
    - turtle
    - random
"""

from turtle import Turtle, Screen, colormode
from random import choice

colors_list= [(199, 175, 118), (125, 36, 24), (187, 158, 50), (170, 105, 56), (5, 57, 83), 
          (108, 67, 85), (39, 36, 35), (86, 142, 58), (20, 123, 176), (110, 161, 175), 
          (75, 39, 47), (9, 67, 47), (64, 153, 137), (133, 41, 43), (184, 98, 80), 
          (179, 201, 186), (210, 200, 113), (179, 175, 177), (151, 176, 164), (93, 142, 156), 
          (28, 80, 59), (17, 78, 98), (213, 184, 173), (145, 116, 121), (176, 197, 202)]

timmy = Turtle()
colormode(255)
timmy.speed(0)
timmy.penup()
timmy.hideturtle()

start_x = -235
start_y = -235

for row in range(10):
    timmy.goto(start_x, start_y+row*50)
    for _ in range(10):
        timmy.dot(20,choice(colors_list))
        timmy.forward(50)
    
screen = Screen()
screen.exitonclick()