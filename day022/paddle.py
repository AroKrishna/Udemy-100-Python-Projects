"""
This module contains the Paddle class used in
Project : Day 22 - Ping Pong Game

Standard Library Modules:
    - turtle
"""

from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.penup()
        self.setposition(x= x_cor, y= y_cor)

    def go_up(self):
        """Moves the paddle upwards by 20 pixels without crossing the boundary"""
        if self.ycor() < 230:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def go_down(self):
        """Moves the paddle downwards by 20 pixels without crossing the boundary"""
        if self.ycor() > -230:    
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)
