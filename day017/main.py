"""
Project : Day 17 - True False Quiz
Imported Modules:
    -question_model
    -quiz_brain
    -data
    -art
"""

from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
from art import logo

question_bank = []

for question in question_data:
    question_text = question["text"]
    question_ans = question["answer"]
    question_bank.append(
        Question(question_text, question_ans)
    )

def game():
    print(logo)
    quiz = QuizBrain(question_bank)
    while quiz.still_has_questions():
        quiz.next_question()
    print("You have finished the quiz.")
    print(f"Your final score is {quiz.score}/{quiz.question_number}")

play_again = 'y'
while play_again == 'y':
    game()
    play_again = input("Do you want to play again ? (y/n) :").lower()
    if play_again == 'y':
        print("\n"*100)
