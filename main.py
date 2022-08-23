from question_model import Question
from data import question_data
from ui import QuizzInterface
if __name__ == '__main__':
    question_bank = []
    for question in question_data:
        question_text = question["question"]
        question_answer = question["correct_answer"]
        new_question = Question(question_text, question_answer)
        question_bank.append(new_question)

    quiz_ui = QuizzInterface(question_bank)
