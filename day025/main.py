"""
Project : Day 25 - U.S States Game

Imported Libraries :
    - turtle
    - pandas
"""


from turtle import Turtle, Screen
import pandas

turtle = Turtle()
screen = Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data["state"].to_list()
guessed_states = []
game_is_on = True

def display_state(answer):
    state_data = data[data["state"] == answer]
    x_coord = state_data["x"].item()
    y_coord = state_data["y"].item()

    text = Turtle()
    text.hideturtle()
    text.penup()
    text.goto(x_coord, y_coord)
    text.write(answer)

while game_is_on :
    answer_state = screen.textinput(title= f"{len(guessed_states)}/50 States Correct",
                                    prompt= "What is another state name ?").title()
    if answer_state in all_states:
        display_state(answer_state)
        guessed_states.append(answer_state)

    elif answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("missed_states.csv")
        game_is_on = False
        break
    
    if len(guessed_states) == 50:
        game_is_on = False
        print("You Won")

screen.exitonclick()
