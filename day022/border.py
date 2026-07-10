"""
This module contains the Border class used in
Project : Day 22 - Ping Pong Game

Standard Library Modules:
    - turtle
"""

from turtle import Turtle

class Border(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.pensize(3)

        # Top & Bottom
        self.color("white")
        self.draw_line(-390, 290, 390, 290)
        self.draw_line(-390, -290, 390, -290)

        # Left & Right
        self.color("red")
        self.draw_line(-390, -290, -390, 290)
        self.draw_line(390, -290, 390, 290)

    def draw_line(self, x1, y1, x2, y2):
        self.penup()
        self.goto(x1, y1)
        self.pendown()
        self.goto(x2, y2)
