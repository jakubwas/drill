from tkinter import filedialog

import Questions
from tkinter import *

root = Tk()
root.geometry("{}x{}".format(900, 500))

# create all of the main containers/frames
top_frame = Frame(root, bg='grey', width=900, height=45)
question_frame = Frame(root, width=900, height=115)
answers_frame = Frame(root, width=900, height=220)
check_answers_frame = Frame(root, width=900, height=120)
check_answers_frame.grid_columnconfigure(0, weight=1, minsize=900)

top_frame.grid_columnconfigure(2, weight=1, minsize=900)

top_frame.grid(row=0, sticky='ew', columnspan=3)
question_frame.grid(row=1, sticky='ew')
answers_frame.grid(row=2, sticky='ew')
check_answers_frame.grid(row=3, sticky='ew')


def open_file():
    root.filename = filedialog.askopenfilename(initialdir="/c", title="Select A File",
                                               filetypes=(("txt files", "*.txt"), ("all files", "*.*")))
    path = root.filename
    return path


_path_ = open_file()
ques = Questions.Questions(_path_)
ques.open_file()
var3 = IntVar()
var3.set(0)

# top_frame widgets
open_file_button = Button(top_frame, text="Open File", command=open_file, bg="grey")
open_file_button.grid(row=0, column=0)
check_button = Checkbutton(top_frame, text="Shuffle", command=lambda: var3.set(1), bg="grey")
# Radiobutton variable
var = StringVar()
var.set(None)

# If the next_question_button is clicked, var2 is set to 1
var2 = IntVar()

next_question_button = Button(top_frame, text="Next Question", width=30, height=2, command=lambda: var2.set(1))
next_question_button.grid(row=0, column=2, sticky="W", padx=20, pady=6)
check_button.grid(row=0, column=1, sticky="W")


def check_answer(i, ans, question_a, question_b, question_c, question_d):
    if ques.correct_answers[i] == ans or ques.correct_answers[i] == ans.capitalize():
        ans_label = Label(check_answers_frame, text="Correct answer", fg="Blue", font=("Helvetica", 18))
        ans_label.grid(row=0, sticky="WENS", pady=25)
    else:
        ans_label = Label(check_answers_frame, fg="Red", font=("Helvetica", 18),
                          text="Wrong\nCorrect answer: " + ques.correct_answers[i])
        ans_label.grid(row=0, sticky="WENS", pady=25)

    # Disable the radiobutton after we click it.
    question_a.configure(state="disabled")
    question_b.configure(state="disabled")
    question_c.configure(state="disabled")
    question_d.configure(state="disabled")

    #
    ans_label.wait_variable(var2)
    ans_label.grid_forget()


def drill():
    for i in range(len(ques.questions)):

        text_a = ques.a_answers[i]
        if str(text_a).startswith(">>>"):
            text_a = text_a[3:]

        text_b = ques.b_answers[i]
        if str(text_b).startswith(">>>"):
            text_b = text_b[3:]

        text_c = ques.c_answers[i]
        if str(text_c).startswith(">>>"):
            text_c = text_c[3:]

        text_d = ques.d_answers[i]
        if str(text_d).startswith(">>>"):
            text_d = text_d[3:]

        question_label = Label(question_frame, wraplength=800, text=ques.questions[i], height=5, pady=10, padx=30)

        question_a = Radiobutton(answers_frame, wraplength=800, text=text_a, variable=var, value="a",
                                 command=lambda: check_answer(i, "a", question_a, question_b, question_c, question_d))
        question_b = Radiobutton(answers_frame, wraplength=800, text=text_b, variable=var, value="b",
                                 command=lambda: check_answer(i, "b", question_a, question_b, question_c, question_d))
        question_c = Radiobutton(answers_frame, wraplength=800, text=text_c, variable=var, value="c",
                                 command=lambda: check_answer(i, "c", question_a, question_b, question_c, question_d))
        question_d = Radiobutton(answers_frame, wraplength=800, text=text_d, variable=var, value="d",
                                 command=lambda: check_answer(i, "d", question_a, question_b, question_c, question_d))

        question_label.grid(row=0, sticky="W", column=0)
        question_a.grid(row=0, sticky="W", column=0)
        question_b.grid(row=1, sticky="W", column=0)
        question_c.grid(row=2, sticky="W", column=0)
        question_d.grid(row=3, sticky="W", column=0)
        next_question_button.wait_variable(var2)

        question_label.grid_forget()
        question_a.grid_forget()
        question_b.grid_forget()
        question_c.grid_forget()
        question_d.grid_forget()
        var.set(None)


drill()
root.mainloop()
