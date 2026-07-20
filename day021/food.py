"""
This module contains the Food class used in
Project : Day 20 & 21 - Snake Game

Standard Library Modules:
    - turtle
    - random
"""


from turtle import Turtle
from random import randint


class Food(Turtle):
    def __init__(self, snake):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.penup()
        self.refresh(snake)

    def refresh(self, snake):
        """Moves the food to a random unoccupied position."""        
        while True:
            random_x = randint(-14, 14) * 20
            random_y = randint(-14, 14) * 20
            if (random_x, random_y) not in snake.body_position():
                self.goto(random_x, random_y)
                break
