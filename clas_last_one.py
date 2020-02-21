from tkinter import filedialog

from Drill_App.Questions import Questions
from tkinter import *


class Drill(Questions):
    def __init__(self, path):
        super().__init__(path)
        self.root = Tk()
        self.root.geometry("{}x{}".format(900, 500))

        # create all of the main containers/frames
        self.top_frame = Frame(self.root, bg='grey', width=900, height=45)
        self.question_frame = Frame(self.root, width=900, height=115)
        self.answers_frame = Frame(self.root, width=900, height=320)
        self.check_answers_frame = Frame(self.root, width=900, height=120)
        self.check_answers_frame.grid_columnconfigure(0, weight=1, minsize=600)

        self.top_frame.grid_columnconfigure(2, weight=1, minsize=900)
        self.j = 0
        self.top_frame.grid(row=0, sticky='ew', columnspan=3)
        self.question_frame.grid(row=1, sticky='ew')
        self.answers_frame.grid(row=2, sticky='ew')
        self.check_answers_frame.grid(row=3, sticky='ew')
        self.counts = 0
        self.path_list = {}
        self.var3 = IntVar()
        self.var3.set(0)
        # top_frame widgets
        self.open_file_button = Button(self.top_frame, text="Open File", command=lambda: self.open_file() & self.var3.set(1), bg="grey")
        self.open_file_button.grid(row=0, column=0)
        self.check_button = Checkbutton(self.top_frame, text="Shuffle", command=lambda: self.var3.set(1), bg="grey")
        # Radiobutton variable
        self.var = StringVar()
        self.var.set(None)
        # If the next_question_button is clicked, var2 is set to 1
        self.var2 = IntVar()
        self.text_a = ""
        self.text_b = ""
        self.text_c = ""
        self.text_d = ""

        self.next_question_button = Button(self.top_frame, text="Next Question", width=30, height=2,
                                           command=lambda: self.var2.set(1))
        self.next_question_button.grid(row=0, column=2, sticky="W", padx=20, pady=6)
        self.check_button.grid(row=0, column=1, sticky="W")

        self.question_a = Radiobutton(self.answers_frame, wraplength=800, text=self.text_a, variable=self.var,
                                      value="a", command=lambda: self.check_answer(self.j, "a"))
        self.question_b = Radiobutton(self.answers_frame, wraplength=800, text=self.text_b, variable=self.var,
                                      value="b", command=lambda: self.check_answer(self.j, "b"))
        self.question_c = Radiobutton(self.answers_frame, wraplength=800, text=self.text_c, variable=self.var,
                                      value="c", command=lambda: self.check_answer(self.j, "c"))
        self.question_d = Radiobutton(self.answers_frame, wraplength=800, text=self.text_d, variable=self.var,
                                      value="d", command=lambda: self.check_answer(self.j, "d"))
        self.question_label = Label(self.question_frame, wraplength=800, text=self.questions[self.j], height=5, pady=10,
                                    padx=30)

        self.question_label.grid(row=0, sticky="W", column=0)
        self.question_a.grid(row=0, sticky="W", column=0)
        self.question_b.grid(row=1, sticky="W", column=0)
        self.question_c.grid(row=2, sticky="W", column=0)
        self.question_d.grid(row=3, sticky="W", column=0)

        self.question_frame = Frame(self.root, width=900, height=115)
        self.answers_frame = Frame(self.root, width=900, height=220)
        self.question_frame.grid(row=1, sticky='ew')
        self.answers_frame.grid(row=2, sticky='ew')

    def open_file(self):
        self.root.filename = filedialog.askopenfilename(initialdir="/c", title="Select A File",
                                                        filetypes=(("txt files", "*.txt"), ("all files", "*.*")))
        path = self.root.filename

        if path != "":
            self.path_list[self.counts] = path
            self.counts = self.counts + 1
            self.open_file_questions()
            self.drill(path)

    def check_answer(self, i, ans):
        if self.correct_answers[i] == ans or self.correct_answers[i] == ans.capitalize():
            ans_label = Label(self.check_answers_frame, text="Correct answer", fg="Blue", font=("Helvetica", 18))
            ans_label.grid(row=0, sticky="WENS", pady=25)
        else:
            ans_label = Label(self.check_answers_frame, fg="Red", font=("Helvetica", 18),
                              text="Wrong\nCorrect answer: " + self.correct_answers[i])
            ans_label.grid(row=0, sticky="WENS", pady=25)

        # Disable the radiobutton after we click it.
        self.question_a.configure(state="disabled")
        self.question_b.configure(state="disabled")
        self.question_c.configure(state="disabled")
        self.question_d.configure(state="disabled")

        #
        ans_label.wait_variable(self.var2)
        ans_label.grid_forget()

    def drill(self, path):

        for i in range(len(self.questions)):
            self.j = i
            self.text_a = self.a_answers[i]
            if str(self.text_a).startswith(">>>"):
                self.text_a = self.text_a[3:]

            self.text_b = self.b_answers[i]
            if str(self.text_b).startswith(">>>"):
                self.text_b = self.text_b[3:]

            self.text_c = self.c_answers[i]
            if str(self.text_c).startswith(">>>"):
                self.text_c = self.text_c[3:]

            self.text_d = self.d_answers[i]
            if str(self.text_d).startswith(">>>"):
                self.text_d = self.text_d[3:]

            self.next_question_button.wait_variable(self.var2)

            self.question_label.grid_forget()
            self.question_a.grid_forget()
            self.question_b.grid_forget()
            self.question_c.grid_forget()
            self.question_d.grid_forget()
            self.var.set(None)
            if self.counts != len(self.path_list):
                self.question_label.grid_forget()
                self.question_a.grid_forget()
                self.question_b.grid_forget()
                self.question_c.grid_forget()
                self.question_d.grid_forget()
                break
            if i == len(self.questions) - 1:
                self.question_a.grid_forget()
                self.question_b.grid_forget()
                self.question_c.grid_forget()
                self.question_d.grid_forget()
                self.question_label.grid_forget()

                self.questions.clear()
                self.a_answers.clear()
                self.b_answers.clear()
                self.c_answers.clear()
                self.d_answers.clear()
                self.open_file()


x = Drill("EPE drill.txt")
x.open_file()
x.root.mainloop()
