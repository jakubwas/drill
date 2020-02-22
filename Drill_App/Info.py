import tkinter as tk
from tkinter import ttk
from Drill_App.Question_Frame import Question_Frame


class Info(tk.Frame):
    def __init__(self, container, **kw):
        super().__init__(container, **kw)

        intro_label = ttk.Label(self, text="Drill application")
        intro_label.grid(row=0, column=0)

        go_back_button = ttk.Button(self, text="Back", command=lambda: controller.show_frame())
        go_back_button.grid(row=1, column=0)
