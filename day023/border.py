"""
This module contains Border class used in
Project : Day 23 - Turtle Crossing Game

Standard Library Modules:
    - turtle
"""

from turtle import Turtle

class Border(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-300,-300)
        self.pendown()
        self.pensize(3)

        for _ in range(4):
            self.forward(600)
            self.left(90)
