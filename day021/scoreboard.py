"""
This module contains the Scoreboard class used in
Project : Day 20 & 21 - Snake Game

Standard Library Modules:
    - pathlib
    - turtle
"""


from pathlib import Path
from turtle import Turtle

DATA_FILE = Path(__file__).parent / "data.txt"

ALIGNMENT = "center"
FONT = ("Courier",15,"normal")
GAME_OVER_FONT = ("Courier", 28, "bold")
MESSAGE_FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.current_score = 0

        """Reads the contents of the fle and stores it as an integer."""
        with DATA_FILE.open("r") as data:
            self.high_score = int(data.read())
            
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,300)
        self.update_scoreboard()

        self.game_over_text = Turtle()
        self.game_over_text.hideturtle()
        self.game_over_text.color("white")
        self.game_over_text.penup()

    def update_scoreboard(self):
        """Displays the current score."""
        self.clear()
        self.write(f"Score : {self.current_score}  High Score : {self.high_score}", align= ALIGNMENT, font= FONT)

    def increase_score(self):
        """Increases the current score and displays it."""
        self.current_score += 1
        self.update_scoreboard()
    
    def reset(self):
        """Resets the score and updates the highscore."""
        if self.current_score > self.high_score:
            self.high_score = self.current_score

            """Modifies the contents of the file."""
            with DATA_FILE.open("w") as data:
                data.write(str(self.high_score))

        self.current_score = 0
        self.update_scoreboard()

    def game_over(self):
        """Displays the game over message."""        
        self.clear_game_over()

        self.game_over_text.goto(0, 20)
        self.game_over_text.write(
            "GAME OVER",
            align="center",
            font= GAME_OVER_FONT
        )

        self.game_over_text.goto(0, -40)
        self.game_over_text.write(
            "Press SPACE to Play Again\nPress ESC to Quit",
            align="center",
            font= MESSAGE_FONT
        )

    def clear_game_over(self):
        """Clears the game over message."""
        self.game_over_text.clear()
