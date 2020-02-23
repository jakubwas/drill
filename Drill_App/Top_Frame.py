import tkinter as tk
from tkinter import ttk, filedialog
from Drill_App.Question_Frame import Question_Frame
from Drill_App.Info import message
import random


class Top_Frame(ttk.Frame):
    def __init__(self, main_window_root, container, question_object, **kwargs):
        super().__init__(container, **kwargs)

        self.main_window_root = main_window_root  # self.main_window_root is type MainWindow
        self.columnconfigure(4, weight=1)  # column with label_correct_wrong
        self.question_object = question_object
        self.question_frame = None
        self.container = container  # container is the main frame created inside main_window_root where all other frames
        #                             have been put
        self.path = None
        # Style:
        # Checkbutton style
        style_checkbutton = ttk.Style()
        style_checkbutton.configure("TCheckbutton", background="#d9d9de", font=("Helvetica", 8, "bold"))
        # Button style
        style_button = ttk.Style()
        style_button.configure("TButton", background="#031a85", foreground="#0014c2", font=("Helvetica", 9, "bold"))
        # Separator style
        line_style = ttk.Style()
        line_style.configure("TSeparator", background="#000000")

        # Variables
        self.window_size_variable = tk.StringVar()
        # shuffle questions variable, when value="yes" the checkbutton is selected
        self.shuffle_var = tk.StringVar()
        self.shuffle_var.set("no")

        # Buttons
        self.button_open_file = ttk.Button(self, text="Open file", command=self.open_file, width=14)
        self.button_next_question = ttk.Button(
            self,
            text="Next question",
            width=32,
            command=lambda: self.question_frame.next_question_var.set(1))
        self.button_reset = ttk.Button(self, text="Reset", command=self.shuffle_command)
        self.info_button = ttk.Button(self, width=5, text="Info", command=message)

        # Labels
        self.label_number_of_question = ttk.Label(self)
        self.label_correct_wrong = ttk.Label(self, text="Answer", font=("Helvetica", 10, "italic"), foreground="black")
        self.label_number_of_question_text = ttk.Label(self, text="Number of Question", font=("Helvetica", 9, "italic"))

        # Combobox
        self.window_size = ttk.Combobox(
            self,
            textvariable=self.window_size_variable,
            values=("900x400", "900x450", "900x500", "900x550", "900x600", "900x650"),
            state="readonly",
            width=7
        )
        self.window_size.bind("<<ComboboxSelected>>", self.change_window_size)  # window_size command

        # Checkbutton
        self.shuffle_questions = ttk.Checkbutton(self, text="  Shuffle", variable=self.shuffle_var,
                                                 onvalue='yes', offvalue='no',
                                                 command=self.shuffle_command)

        # Layout
        self.button_open_file.grid(row=0, column=0, sticky="W", padx=(0, 10))
        self.button_next_question.grid(row=0, rowspan=2, column=2, sticky="NEWS", padx=(10, 5), pady=(0, 3))
        self.button_reset.grid(row=0, column=1, sticky="W", padx=(10, 10))
        self.info_button.grid(row=0, rowspan=2, column=5, sticky="E", padx=(10, 10), pady=(10, 10))

        self.label_number_of_question_text.grid(row=0, column=3, sticky="NW", padx=(0, 5))
        self.label_number_of_question.grid(row=1, column=3)
        self.label_correct_wrong.grid(row=0, rowspan=2, column=4, sticky="N")

        self.window_size.grid(row=1, column=0, sticky="W", pady=(4, 4))
        self.shuffle_questions.grid(row=1, column=1, sticky="WE", padx=(10, 10))

        # Separator
        # horizontal
        ttk.Separator(self, orient="horizontal").grid(row=2, columnspan=6, sticky="WE")
        # vertical
        ttk.Separator(self, orient="vertical").grid(column=0, row=0, rowspan=2, sticky="ESN")
        ttk.Separator(self, orient="vertical").grid(column=1, row=0, rowspan=2, sticky="ESN")
        ttk.Separator(self, orient="vertical").grid(column=4, row=0, rowspan=2, sticky="WSN")
        ttk.Separator(self, orient="vertical").grid(column=4, row=0, rowspan=2, sticky="ESN")

    # Methods
    def config_label_answer(self):
        self.label_correct_wrong.config(
            text="Answer",
            font=("Helvetica", 10, "italic"),
            foreground="black"
        )
        self.label_correct_wrong.grid(sticky="N")

    def quest(self):
        pass

    def shuffle_command(self):
        if type(self.question_frame) is Question_Frame:  # when we select shuffle checkbutton, we want to clean the
            #                                              question_frame if exist
            self.question_frame.destroy()

        self.question_frame = Question_Frame(self.container)
        self.question_frame.grid(row=1, column=0, sticky="NEWS")
        self.question_frame.question_object = self.question_object
        self.question_frame.next_question_button = self.button_next_question
        self.question_frame.label_number_of_question = self.label_number_of_question
        self.question_frame.label_correct_wrong = self.label_correct_wrong
        self.question_frame.question_range = list(range(0, len(self.question_frame.question_object.questions), 1))
        if self.shuffle_var.get() == "yes":
            random.shuffle(self.question_frame.question_range)
        self.config_label_answer()
        self.question_frame.drill()

    def change_window_size(self, event):
        self.main_window_root.geometry(self.window_size_variable.get())

    def open_file(self):
        self.path = filedialog.askopenfilename(initialdir="/c", title="Select A File",
                                               filetypes=(("txt files", "*.txt"), ("all files", "*.*")))
        if self.path != "":
            self.config_label_answer()
            if type(self.question_frame) is Question_Frame:
                self.question_frame.destroy()
            self.question_object.open_file_questions(self.path)
            self.shuffle_command()
