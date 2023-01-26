THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain
GREEN = "#8FBC8F"
RED = "#FF6A6A"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        self.canvas = Canvas(background="white", height=250, width=300)
        self.question_text = self.canvas.create_text(150, 125, text="Question", fill=THEME_COLOR,
                                                     font=("arial", 12, "italic"), width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, rowspan=2, pady=50)

        self.score = 0
        self.score_label = Label(text=f"score = {self.score}", background=THEME_COLOR, foreground="white")
        self.score_label.grid(column=1, row=0)

        true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_img, highlightthickness=0, command=self.ans_true)
        self.true_button.grid(column=0, row=3)

        false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.ans_false)
        self.false_button.grid(column=1, row=3)

        self.ans = ""
        self.time = self.window.after(0, self.next_q)

        self.window.mainloop()

    def next_q(self):
        # self.window.after_cancel(self.time)
        self.canvas.config(background="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else :
            self.true_button.config(state= "disabled")
            self.false_button.config(state="disabled")

    def ans_true(self):
        self.ans = self.quiz.check_answer("True")
        self.check_ans()

    def ans_false(self):
        self.ans = self.quiz.check_answer("False")
        self.check_ans()

    def check_ans(self):
        if self.ans:
            self.correct_ans()
        else:
            self.wrong_ans()

    def correct_ans(self):
        self.canvas.config(background=GREEN)
        self.score += 1
        self.score_label["text"] = f"score = {self.score}"
        # print("You got it right!")
        self.time = self.window.after(600, self.next_q)

    def wrong_ans(self):
        self.canvas.config(background=RED)
        self.score_label["text"] = f"score = {self.score}"
        # print("That's wrong.")
        self.time = self.window.after(600, self.next_q)
