import tkinter as tk
from tkinter import ttk


class Question_Frame(ttk.Frame):
    def __init__(self, container, question_object, **kwargs):
        super().__init__(container, **kwargs)

        self.container = container
        self.question_object = question_object
        self.selected_answer = tk.StringVar()
        self.text_question = None
        self.text_a = "AAA"
        self.text_b = None
        self.text_c = None
        self.text_d = None

        label_question = ttk.Label(self, text=self.text_question)
        self.a_answer = ttk.Radiobutton(self, text=self.text_a, variable=self.selected_answer, value="a")
        self.b_answer = ttk.Radiobutton(self, text=self.text_b, variable=self.selected_answer, value="b")
        self.c_answer = ttk.Radiobutton(self, text=self.text_c, variable=self.selected_answer, value="c")
        self.d_answer = ttk.Radiobutton(self, text=self.text_d, variable=self.selected_answer, value="d")

        label_question.grid(row=0, column=0)
        self.a_answer.grid(row=1, column=0)
        self.b_answer.grid(row=2, column=0)
        self.c_answer.grid(row=3, column=0)
        self.d_answer.grid(row=4, column=0)

    def drill(self):
        for i in range(len(self.question_object.questions)):
            self.text_a = self.a_answer[i]
            if str(self.text_a).startswith(">>>"):
                self.text_a = self.text_a[3:]

            self.text_b = self.b_answer[i]
            if str(self.text_b).startswith(">>>"):
                self.text_b = self.text_b[3:]

            self.text_c = self.c_answer[i]
            if str(self.text_c).startswith(">>>"):
                self.text_c = self.text_c[3:]

            self.text_d = self.d_answer[i]
            if str(self.text_d).startswith(">>>"):
                self.text_d = self.text_d[3:]

