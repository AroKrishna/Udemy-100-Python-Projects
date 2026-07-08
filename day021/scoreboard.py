"""
This module contains the Scoreboard class used in
Project : Day 20 & 21 - Snake Game

Standard Library Modules:
    - turtle
"""

from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier",15,"normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.current_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,300)
        self.update_scoreboard()

    def update_scoreboard(self):
        """Displays the current score."""
        self.write(f"Score = {self.current_score}", align= ALIGNMENT, font= FONT)

    def increase_score(self):
        """Increases the current score and displays it."""
        self.current_score += 1
        self.clear()
        self.update_scoreboard()
    
    def game_over(self):
        """Displays the Game Over text."""
        self.goto(0,0)
        self.write(f"GAME OVER",align= ALIGNMENT, font= FONT)
