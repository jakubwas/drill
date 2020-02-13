import tkinter as tk
from tkinter import filedialog

import Questions

root = tk.Tk()
root.geometry("900x500")
root.resizable(0, 0)


#  Methods

def open_file():
    root.filename = filedialog.askopenfilename(initialdir="/c", title="Select A File",
                                               filetypes=(("txt files", "*.txt"), ("all files", "*.*")))
    path = root.filename
    return path


_path_ = open_file()
ques = Questions.Questions(_path_)
ques.open_file()
#  Buttons

open_file_button = tk.Button(root, text="Open File", command=open_file).grid(row=0, column=0, sticky="NW")

var = tk.StringVar()
var.set(None)
var2 = tk.IntVar()

next_question_button = tk.Button(root, text="Next Question", width=30, height=2, command=lambda: var2.set(1))
next_question_button.grid(row=0, column=1, sticky="W", padx=20)


def check_answer(i, ans, question_a, question_b, question_c, question_d):

    if ques.correct_answers[i] == ans or ques.correct_answers[i] == ans.capitalize():
        ans_label = tk.Label(root, text="Correct answers.", fg="Blue", font=("Helvetica", 18))
        ans_label.grid(row=7, column=1, sticky="W")
    else:
        ans_label = tk.Label(root,fg="Red", font=("Helvetica", 18), text="Wrong, correct answer is " + ques.correct_answers[i])
        ans_label.grid(row=7, column=1, sticky="W")
    question_a.configure(state="disabled")
    question_b.configure(state="disabled")
    question_c.configure(state="disabled")
    question_d.configure(state="disabled")
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

        question_label = tk.Label(root, wraplength=800, text=ques.questions[i], height=5, pady=10)
        question_a = tk.Radiobutton(root, wraplength=800, text=text_a, variable=var, value="a", command =lambda: check_answer(i, "a", question_a, question_b, question_c, question_d))
        question_b = tk.Radiobutton(root, wraplength=800, text=text_b, variable=var, value="b", command =lambda: check_answer(i, "b", question_a, question_b, question_c, question_d))
        question_c = tk.Radiobutton(root, wraplength=800, text=text_c, variable=var, value="c", command =lambda: check_answer(i, "c", question_a, question_b, question_c, question_d))
        question_d = tk.Radiobutton(root, wraplength=800, text=text_d, variable=var, value="d", command =lambda: check_answer(i, "d", question_a, question_b, question_c, question_d))

        question_label.grid(row=1, sticky="W", column=1)
        question_a.grid(row=3, sticky="W", columnspan=2)
        question_b.grid(row=4, sticky="W", columnspan=2)
        question_c.grid(row=5, sticky="W", columnspan=2)
        question_d.grid(row=6, sticky="W", columnspan=2)
        root.grid_columnconfigure(1, minsize=900)
        next_question_button.wait_variable(var2)

        question_label.grid_forget()
        question_a.grid_forget()
        question_b.grid_forget()
        question_c.grid_forget()
        question_d.grid_forget()
        var.set(None)


drill()
root.mainloop()
