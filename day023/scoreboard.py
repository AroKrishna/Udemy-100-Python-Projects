"""
This module contains Scoreboard class used in
Project : Day 23 - Turtle Crossing

Standard Library Modules:
    - turtle
"""

from turtle import Turtle

FONT = ("Courier", 24, "normal")
SCOREBOARD_POSITION = (-220, 260)

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(SCOREBOARD_POSITION)
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(f"Level: {self.level}", align= "center",font= FONT)

    def update_level(self):
        self.level += 1
        self.display_score()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align= "center" ,font= FONT)
