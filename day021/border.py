"""
This module contains the Border class used in
Project : Day 20 & 21 - Snake Game

Standard Library Modules:
    - turtle
"""


from turtle import Turtle


class Border(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(-290, -290)
        self.pendown()
        self.pensize(3)

        for _ in range(4):
            self.forward(580)
            self.left(90)
