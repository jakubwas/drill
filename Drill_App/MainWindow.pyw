import tkinter as tk
from tkinter import ttk
from Questions import Questions
from Top_Frame import Top_Frame


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("900x500")
        self.title("Drill")
        self.columnconfigure(0, weight=1)
        self.resizable(False, False)

        questions_object = Questions()

        container = ttk.Frame(self)
        container.grid(padx=3, pady=3, sticky="EW")
        container.columnconfigure(0, weight=1)

        self.top_frame = Top_Frame(self, container, questions_object)
        self.top_frame.grid(row=0, column=0, sticky="NEWS")


root = MainWindow()
root.mainloop()
