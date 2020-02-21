import tkinter as tk
from tkinter import ttk


class Question_Frame(ttk.Frame):
    def __init__(self, container, **kwargs):
        super().__init__(container, **kwargs)

        self.container = container  # Main window
        self.next_question_button = None
        self.label_correct_wrong = None
        self.question_object = None
        self.selected_answer = tk.StringVar()
        self.text_question = None
        self.text_a = None
        self.text_b = None
        self.text_c = None
        self.text_d = None

        self.label_question = ttk.Label(self)
        self.a_answer = ttk.Radiobutton(self, variable=self.selected_answer, value="a")
        self.b_answer = ttk.Radiobutton(self, variable=self.selected_answer, value="b")
        self.c_answer = ttk.Radiobutton(self, variable=self.selected_answer, value="c")
        self.d_answer = ttk.Radiobutton(self, variable=self.selected_answer, value="d")

        self.var = tk.IntVar()
        self.next_question_var = tk.IntVar()

    def drill(self):
        self.label_question.grid(row=0, column=0, sticky="W")
        self.a_answer.grid(row=1, column=0, sticky="W")
        self.b_answer.grid(row=2, column=0, sticky="W")
        self.c_answer.grid(row=3, column=0, sticky="W")
        self.d_answer.grid(row=4, column=0, sticky="W")

        for i in range(len(self.question_object.questions)):

            self.text_question = self.question_object.questions[i]
            self.label_question.config(text=self.text_question)

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

    def check_answer(self):
        pass