import tkinter as tk
from tkinter import ttk


class Question_Frame(ttk.Frame):
    def __init__(self, container, question_object, **kwargs):
        super().__init__(container, **kwargs)

        self.container = container
        self.question_object = question_object
        self.selected_answer = tk.StringVar()
        self.text_question = None
        self.text_a = None
        self.text_b = None
        self.text_c = None
        self.text_d = None

        self.label_question = ttk.Label(self, text=self.text_question)
        self.a_answer = ttk.Radiobutton(self, text=self.text_a, variable=self.selected_answer, value="a")
        self.b_answer = ttk.Radiobutton(self, text=self.text_b, variable=self.selected_answer, value="b")
        self.c_answer = ttk.Radiobutton(self, text=self.text_c, variable=self.selected_answer, value="c")
        self.d_answer = ttk.Radiobutton(self, text=self.text_d, variable=self.selected_answer, value="d")

        self.label_question.grid(row=0, column=0, sticky="W")
        self.a_answer.grid(row=1, column=0, sticky="W")
        self.b_answer.grid(row=2, column=0, sticky="W")
        self.c_answer.grid(row=3, column=0, sticky="W")
        self.d_answer.grid(row=4, column=0, sticky="W")

        self.var = tk.IntVar()

    def drill(self):
        pass
