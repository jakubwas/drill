import tkinter as tk
from tkinter import ttk
from Drill_App.Questions import Questions
from Drill_App.Top_Frame import Top_Frame
from Drill_App.Question_Frame import Question_Frame


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("600x400")
        self.title("Drill")
        self.columnconfigure(0, weight=1)

        questions_object = Questions()

        container = ttk.Frame(self)
        container.grid(padx=10, pady=10, sticky="EW")
        container.columnconfigure(0, weight=1)

        question_frame = Question_Frame(container, questions_object)
        question_frame.grid(row=1, column=0, sticky="NSWE")

        top_frame = Top_Frame(container, questions_object, question_frame)
        top_frame.grid(row=0, column=0, sticky="NSWE")

root = MainWindow()
root.mainloop()
