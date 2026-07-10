"""
This module contains the Scoreboard class used in
Project : Day 22 - Ping Pong Game

Standard Library Modules:
    - turtle
"""

from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier",24,"normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 300)
        self.update_score()

    def update_score(self):
        """Displays the current score."""
        self.clear()
        self.write(f"{self.left_score} : {self.right_score}", align= ALIGNMENT, font= FONT)  

    def left_point(self):
        self.left_score += 1
        self.update_score()

    def right_point(self):
        self.right_score += 1
        self.update_score()
