"""
This module contains the CarManager class used in
Project : Day 23 - Turtle Crossing Game

Standard Library Modules:
    - turtle
    - random
"""

from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5

class CarManager:
    def __init__(self):
        self.all_cars = []
        self.current_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        """Creates a new car and adds it to the list."""
        random_chance = randint(1,6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.penup()
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.setheading(180)
            new_car.color(choice(COLORS))
            random_y = randint(-25,25)*10
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        """Moves the cars forward."""
        for car in self.all_cars:
            car.forward(self.current_speed)

    def clear_cars(self):
        """Removes all cars from the screen and clears the list."""
        for car in self.all_cars:
            car.hideturtle()
        self.all_cars.clear()

    def speed_up(self):
        """Increases the car speed."""
        self.current_speed += MOVE_INCREMENT
