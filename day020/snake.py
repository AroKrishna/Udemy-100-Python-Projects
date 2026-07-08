"""
This module contains the Snake class used in
Project : Day 20 & 21 - Snake Game

Standard Library Modules:
    - turtle
"""

from turtle import Turtle

STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.all_segments= []
        self.create_snake()
        self.head = self.all_segments[0]

    def create_snake(self):
        """Creates the starting segments."""
        for position in STARTING_POSITIONS:
            self.add_segments(position)

    def add_segments(self, position):
        """Creates a new segment at the given position."""
        next_segment = Turtle("square")
        next_segment.color("white")
        next_segment.penup()
        next_segment.goto(position)
        self.all_segments.append(next_segment)

    def extend(self):
        """Adds a new segment to the tail."""
        self.add_segments(self.all_segments[-1].position())

    def move(self):
        """Moves the snake forward."""
        for seg_num in range(len(self.all_segments)-1,0,-1):
            next_segment_position = self.all_segments[seg_num-1].position()
            self.all_segments[seg_num].goto(next_segment_position)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def snake_body_position(self):
        """Returns the positions of all snake segments."""
        return [segment.position() for segment in self.all_segments]
