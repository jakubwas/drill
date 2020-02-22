import tkinter as tk
from tkinter import ttk, filedialog
from Drill_App.Question_Frame import Question_Frame
from Drill_App.Info import message


class Top_Frame(ttk.Frame):
    def __init__(self, main_window_root, container, question_object, **kwargs):
        super().__init__(container, **kwargs)
        self.main_window_root = main_window_root
        self.columnconfigure(4, weight=1)
        self.question_object = question_object
        self.question_frame = None
        self.container = container

        self.button_open_file = ttk.Button(self, text="Open file", command=self.open_file, width=10)
        self.button_next_question = ttk.Button(
            self,
            text="Next question",
            width=35,
            command=lambda: self.question_frame.next_question_var.set(1))

        self.window_size_variable = tk.StringVar()

        self.window_size = ttk.Combobox(
            self,
            textvariable=self.window_size_variable,
            values=("900x400", "900x450", "900x500", "900x550", "900x600", "900x650"),
            state="readonly",
            width=8
        )
        self.window_size.bind("<<ComboboxSelected>>", self.change_window_size)

        self.shuffle_answers = ttk.Checkbutton(self, text="Shuffle answers")
        self.shuffle_questions = ttk.Checkbutton(self, text="Shuffle questions")
        self.label_number_of_question = ttk.Label(self)
        self.label_correct_wrong = ttk.Label(self, text="Answer", font=("Helvetica", 10), foreground="black")
        self.info_button = ttk.Button(self, width=5, text="Info", command=message)
        self.label_number_of_question_text = ttk.Label(self, text="Number of Question")

        self.button_open_file.grid(row=0, column=0, padx=(0, 10), sticky="W", pady=(0, 3))
        self.button_next_question.grid(row=0, rowspan=2, column=2, sticky="NEWS", padx=(10, 10))
        self.window_size.grid(row=1, column=0, sticky="W", pady=(0, 10))
        self.shuffle_answers.grid(row=0, column=1, sticky="W")
        self.shuffle_questions.grid(row=1, column=1, sticky="W", padx=(0, 10))
        self.label_number_of_question_text.grid(row=0, column=3, sticky="NW")
        self.label_number_of_question.grid(row=1, column=3)
        self.label_correct_wrong.grid(row=0, rowspan=2, column=4, sticky="N")
        self.info_button.grid(row=0, rowspan=2, column=5, sticky="E", padx=(15, 7))

        #  horizontal separators
        ttk.Separator(self, orient="horizontal").grid(row=2, columnspan=6, sticky="WE", pady=(5, 15))
        #  vertical separators
        ttk.Separator(self, orient="vertical").grid(column=1, row=0, rowspan=2, sticky="ESN")
        ttk.Separator(self, orient="vertical").grid(column=4, row=0, rowspan=2, sticky="WSN", padx=(5, 5))
        ttk.Separator(self, orient="vertical").grid(column=4, row=0, rowspan=2, sticky="ESN", padx=(5, 5))

        self.path = None

    def change_window_size(self, event):
        self.main_window_root.geometry(self.window_size_variable.get())

    def open_file(self):
        self.path = filedialog.askopenfilename(initialdir="/c", title="Select A File",
                                               filetypes=(("txt files", "*.txt"), ("all files", "*.*")))
        if self.path != "":
            if type(self.question_frame) is Question_Frame:
                self.question_frame.destroy()
            self.question_object.open_file_questions(self.path)
            self.question_frame = Question_Frame(self.container)
            self.question_frame.grid(row=1, column=0, sticky="NEWS")
            self.question_frame.question_object = self.question_object
            self.question_frame.next_question_button = self.button_next_question
            self.question_frame.label_number_of_question = self.label_number_of_question
            self.question_frame.label_correct_wrong = self.label_correct_wrong
            self.question_frame.drill()
