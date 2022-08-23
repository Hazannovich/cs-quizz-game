import html


class QuizBrain:

    def __init__(self, q_list):
        self.score = 0
        self.question_list = q_list
        self.question_number = 1
        self.current_question = self.question_list[self.question_number - 1]
        self.q_text = html.unescape(self.current_question.text)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        self.q_text = html.unescape(self.current_question.text)

    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False
