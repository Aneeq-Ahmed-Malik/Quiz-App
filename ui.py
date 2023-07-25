from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.quest_text = self.canvas.create_text(150, 125, font=("Arial", 15, "italic"), width=280)
        self.canvas.itemconfig(self.quest_text, fill=THEME_COLOR)

        true_img = PhotoImage(file="./images/true.png")
        false_img = PhotoImage(file="./images/false.png")

        self.true_btn = Button(image=true_img, highlightthickness=0, bg=THEME_COLOR, command=self.tick)
        self.true_btn.grid(column=0, row=2)

        self.false_btn = Button(image=false_img, highlightthickness=0, bg=THEME_COLOR, command=self.cross)
        self.false_btn.grid(column=1, row=2)

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white", font=("Courier", 12))
        self.score_label.grid(column=1, row=0)

        self.get_new_question()
        self.window.mainloop()

    def get_new_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():

            q_text = self.quiz.next_question()
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.quest_text, text=q_text)

        else:
            self.canvas.itemconfig(self.quest_text, text="You've reached at the end of the quiz.")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def tick(self):

        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def cross(self):

        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):

        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_new_question)
