"""
This is module contains the QuizBrain Class used in
Project : Day 17 - True False Quiz
"""

class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        """Returns True if there are questions left. Otherwise, returns False"""
        return self.question_number < len(self.question_list)

    def next_question(self):
        """Displays the question, collects the user's answer and evaluates it."""
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_ans = input(f"Q{self.question_number}. {current_question.text} (True/False): ")
        self.check_answer(user_ans, current_question.ans)

    def check_answer(self, user_ans, correct_ans):
        """Checks whether the user's answer is correct.
        Displays the correct answer and the current score."""
        if user_ans.lower() == correct_ans.lower():
            print("You are right.")
            self.score += 1
        else:
            print("You are wrong.")
        print(f"The correct answer is : {correct_ans}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
