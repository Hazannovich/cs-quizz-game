from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ('Arial', 20, 'italic')


class QuizzInterface:

    def __init__(self, question_bank):
        self.quiz = QuizBrain(question_bank)
        self.window = Tk()
        self.window.title("Quizzer")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.canvas = Canvas(self.window, width=300, height=250, bg='white')
        self.text = self.canvas.create_text(150, 125, fill='black', text=f"Q.1: {self.quiz.q_text}",
                                            font=FONT, width=295)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        true_img = PhotoImage(file="images/true.png")
        false_img = PhotoImage(file="images/false.png")
        self.true_btn = Button(image=true_img, highlightthickness=0, command=self.press_true)
        self.true_btn.grid(column=0, row=2)
        self.false_btn = Button(image=false_img, highlightthickness=0, command=self.press_false)
        self.false_btn.grid(column=1, row=2)
        self.score_text = Label(self.window, text=f"score: {self.quiz.score} / 0", bg=THEME_COLOR,
                                fg='white',
                                font=FONT)
        self.score_text.grid(column=1, row=0)
        self.action = self.window.after(300, self.canvas_default)
        self.window.mainloop()

    def print_question(self):
        if self.quiz.still_has_questions():
            self.quiz.next_question()
            self.canvas.itemconfig(self.text, text=f"Q.{self.quiz.question_number}: "
                                                   f"{self.quiz.q_text}")
        else:
            self.canvas.itemconfig(self.text, text=f"Congrats! Your Final Score is {self.quiz.score} Out of "
                                                   f"{self.quiz.question_number}")
            self.true_btn.config(state=DISABLED)
            self.false_btn.config(state=DISABLED)

    def update_score(self):
        self.score_text.config(text=f"score: {self.quiz.score} / {self.quiz.question_number}")

    def press_true(self):
        is_right = self.quiz.check_answer("true")
        self.update_score()
        self.give_feedback(is_right)
        self.print_question()

    def press_false(self):
        is_right = self.quiz.check_answer("false")
        self.update_score()
        self.give_feedback(is_right)
        self.print_question()

    def give_feedback(self, is_right):
        self.window.after_cancel(self.action)
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.action = self.window.after(300, self.canvas_default)

    def canvas_default(self):
        self.canvas.config(bg='white')
