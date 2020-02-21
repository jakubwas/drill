import tkinter as tk
from tkinter import ttk


class Question_Frame(ttk.Frame):
    def __init__(self, container, **kwargs):
        super().__init__(container, **kwargs)

        self.container = container  # Main window
        self.next_question_button = None
        self.label_correct_wrong = None
        self.label_number_of_question = None
        self.question_object = None
        self.selected_answer = tk.StringVar()
        self.text_question = None
        self.text_a = None
        self.text_b = None
        self.text_c = None
        self.text_d = None
        self.j = None

        self.label_question = ttk.Label(self)
        self.a_answer = ttk.Radiobutton(self, variable=self.selected_answer, value="a", command=self.check_answer)
        self.b_answer = ttk.Radiobutton(self, variable=self.selected_answer, value="b", command=self.check_answer)
        self.c_answer = ttk.Radiobutton(self, variable=self.selected_answer, value="c", command=self.check_answer)
        self.d_answer = ttk.Radiobutton(self, variable=self.selected_answer, value="d", command=self.check_answer)

        # Style


        # Variables
        self.var = tk.IntVar()
        self.next_question_var = tk.IntVar()

    def check_answer(self):
        if self.selected_answer.get().capitalize() == self.question_object.correct_answers[self.j].capitalize():
            self.label_correct_wrong.config(
                text="Correct answer.",
                font=("Helvetica", 16),
            )
        else:
            self.label_correct_wrong.config(
                text=f"         Wrong !\nCorrect answer is: {self.question_object.correct_answers[self.j]}",
                font=("Helvetica", 16)
                )
        self.label_correct_wrong.grid(sticky="NS")

    def drill(self):
        self.label_question.grid(row=0, column=0, sticky="W")
        self.a_answer.grid(row=1, column=0, sticky="W")
        self.b_answer.grid(row=2, column=0, sticky="W")
        self.c_answer.grid(row=3, column=0, sticky="W")
        self.d_answer.grid(row=4, column=0, sticky="W")

        for i in range(len(self.question_object.questions)):
            self.label_number_of_question.config(
                text=f"{i+1}/{len(self.question_object.questions)}",
                font=("Helvetica", 15)
            )
            self.j = i
            self.text_question = self.question_object.questions[i]
            self.label_question.config(text=self.text_question, wraplength=980, font=("Helvetica", 14))

            self.text_a = self.question_object.a_answers[i]
            if str(self.text_a).startswith(">>>"):
                self.text_a = self.text_a[3:]
            self.a_answer.config(text=self.text_a)

            self.text_b = self.question_object.b_answers[i]
            if str(self.text_b).startswith(">>>"):
                self.text_b = self.text_b[3:]
            self.b_answer.config(text=self.text_b)

            self.text_c = self.question_object.c_answers[i]
            if str(self.text_c).startswith(">>>"):
                self.text_c = self.text_c[3:]
            self.c_answer.config(text=self.text_c)

            self.text_d = self.question_object.d_answers[i]
            if str(self.text_d).startswith(">>>"):
                self.text_d = self.text_d[3:]
            self.d_answer.config(text=self.text_d)

            self.next_question_button.wait_variable(self.next_question_var)
            self.label_correct_wrong.config(text="")
            self.selected_answer.set(None)
            self.label_correct_wrong.config(
                text="Answer",
                font=("Helvetica", 10)
            )
            self.label_correct_wrong.grid(sticky="N")
