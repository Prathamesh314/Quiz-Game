
THEME_COLOR = "#375362"

from tkinter import *
from quiz_brain import QuizBrain

class Quizller:
    def __init__(self,quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.obj = Tk()
        self.obj.title("Quiz Game")
        self.obj.config(padx=20,pady=20,bg=THEME_COLOR)

        self.score_label = Label(text="Score : 0",font=("Arial",12,"bold"),bg=THEME_COLOR,fg="white")
        self.score_label.grid(row=0,column=1)

        self.canvas = Canvas(width=300,height=250,bg="white")
        self.question_text = self.canvas.create_text((150,125),width=280,text="Let's get ready to solve some questions",font=("Arial",13,"italic"),fill="black")
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)
        true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_img,command=self.true_pressed)
        self.true_button.grid(row=2,column=0)
        false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_img,command=self.false_pressed)
        self.false_button.grid(row=2,column=1)

        self.get_next_quesiton()

        self.obj.mainloop()

    def get_next_quesiton(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score : {self.quiz.score}")
            que_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=que_text)
        else:
            self.canvas.itemconfig(self.question_text,text="You 've reached at the end of the Quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.obj.after(1000, self.get_next_quesiton)