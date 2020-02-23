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
        self.text_question = None
        self.text_a = None
        self.text_b = None
        self.text_c = None
        self.text_d = None
        self.j = None
        self.x = 0
        self.question_range = None

        # Style
        # question
        style_question_label = ttk.Style()
        style_question_label.configure("qls.TLabel", background="#bed4f7")
        # answer
        style_answer = ttk.Style()
        style_answer.configure("TRadiobutton", font=("Helvetica", 10,), wraplength=840)

        # Variables
        self.var = tk.IntVar()
        self.next_question_var = tk.IntVar()
        self.selected_answer = tk.StringVar()

        # Labels
        self.label_question = ttk.Label(self, style="qls.TLabel")
        self.a_answer = ttk.Radiobutton(self, variable=self.selected_answer, value="a", command=self.check_answer)
        self.b_answer = ttk.Radiobutton(self, variable=self.selected_answer, value="b", command=self.check_answer)
        self.c_answer = ttk.Radiobutton(self, variable=self.selected_answer, value="c", command=self.check_answer)
        self.d_answer = ttk.Radiobutton(self, variable=self.selected_answer, value="d", command=self.check_answer)

    # Methods
    def check_answer(self):
        if self.selected_answer.get().capitalize() == self.question_object.correct_answers[self.j].capitalize():
            self.label_correct_wrong.config(
                text="Correct answer",
                font=("Helvetica", 16, "bold"),
                foreground="blue")
        else:
            self.label_correct_wrong.config(
                text=f"         Wrong !\nCorrect answer is: {self.question_object.correct_answers[self.j]}",
                font=("Helvetica", 16, "bold"),
                foreground="red")

        self.label_correct_wrong.grid(sticky="NS")

    def drill(self):
        # Every time we click shuffle checkbutton, reset button or we open new file, the question_frame abject is
        # destroyed, that is why we have to put all widgets back to the frame when we call drill method
        self.label_question.grid(row=0, column=0, sticky="WENS")
        self.rowconfigure(0, minsize=120)  # min height for label_question is 120
        self.columnconfigure(0, weight=1)
        ttk.Separator(self, orient="horizontal").grid(row=0, columnspan=6, sticky="SWE")
        self.a_answer.grid(row=1, column=0, sticky="W", pady=(10, 0))
        self.b_answer.grid(row=2, column=0, sticky="W")
        self.c_answer.grid(row=3, column=0, sticky="W")
        self.d_answer.grid(row=4, column=0, sticky="W")

        for i in self.question_range:
            self.label_number_of_question.config(
                text=f"{self.x + 1}/{len(self.question_object.questions)}",
                font=("Helvetica", 15)
            )
            self.j = i
            self.x += 1
            self.text_question = self.question_object.questions[self.question_range[i]]
            self.label_question.config(text=self.text_question, wraplength=840, font=("Helvetica", 14))

            # question A
            self.text_a = self.question_object.a_answers[self.question_range[i]]
            if str(self.text_a).startswith(">>>"):
                self.text_a = self.text_a[3:]
            self.a_answer.config(text=self.text_a)

            # question B
            self.text_b = self.question_object.b_answers[self.question_range[i]]
            if str(self.text_b).startswith(">>>"):
                self.text_b = self.text_b[3:]
            self.b_answer.config(text=self.text_b)

            # question C
            self.text_c = self.question_object.c_answers[self.question_range[i]]
            if str(self.text_c).startswith(">>>"):
                self.text_c = self.text_c[3:]
            self.c_answer.config(text=self.text_c)

            # question D
            self.text_d = self.question_object.d_answers[self.question_range[i]]
            if str(self.text_d).startswith(">>>"):
                self.text_d = self.text_d[3:]
            self.d_answer.config(text=self.text_d)

            # Wait until the next_question button is pressed
            self.next_question_button.wait_variable(self.next_question_var)
            self.label_correct_wrong.config(text="")
            self.selected_answer.set(None)  # unselect selected answer
            self.label_correct_wrong.config(  # we don't want to have old answer(correct or wrong when new question
                text="Answer",                # appears)
                font=("Helvetica", 10, "italic"),
                foreground="black"
            )
            self.label_correct_wrong.grid(sticky="N")
