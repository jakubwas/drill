from tkinter import ttk, filedialog
from Drill_App.Question_Frame import Question_Frame


class Top_Frame(ttk.Frame):
    def __init__(self, container, question_object, question_frame, **kwargs):
        super().__init__(container, **kwargs)

        self.columnconfigure(3, weight=1)
        self.question_object = question_object
        self.question_frame = question_frame
        self.container = container

        self.button_open_file = ttk.Button(self, text="Open file", command=self.open_file)
        #  button_add_file = ttk.Button(self, text="Add file")
        self.button_next_question = ttk.Button(
            self,
            text="Next question",
            width=35,
            command=lambda: self.question_frame.next_question_var.set(1))

        self.shuffle_answers = ttk.Checkbutton(self, text="Shuffle answers")
        self.shuffle_questions = ttk.Checkbutton(self, text="Shuffle questions")
        self.label_number_of_question = ttk.Label(self, text=f"Number of Question")
        self.label_correct_wrong = ttk.Label(self)

        self.button_open_file.grid(row=0, column=0, padx=(0, 10))
        self.button_next_question.grid(row=0, rowspan=2, column=2, sticky="NEWS", padx=(10, 10))
        self.shuffle_answers.grid(row=0, column=1, sticky="W")
        self.shuffle_questions.grid(row=1, column=1, sticky="W")
        self.label_number_of_question.grid(row=0, rowspan=2, column=3, sticky="W")
        self.label_correct_wrong.grid(row=0, rowspan=2, column=3, sticky="WE")
        ttk.Separator(self, orient="horizontal").grid(row=2, columnspan=5, sticky="WE", pady=(5, 5))

        self.path = None

    def open_file(self):
        self.path = filedialog.askopenfilename(initialdir="/c", title="Select A File",
                                               filetypes=(("txt files", "*.txt"), ("all files", "*.*")))
        if self.path != "":
            self.question_frame.destroy()
            self.question_object.open_file_questions(self.path)
            self.question_frame = Question_Frame(self.container)
            self.question_frame.grid(row=1, column=0, sticky="NEWS")
            self.question_frame.question_object = self.question_object
            self.question_frame.next_question_button = self.button_next_question
            self.question_frame.label_correct_wrong = self.label_correct_wrong
            self.question_frame.drill()

