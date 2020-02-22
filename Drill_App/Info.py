from tkinter import messagebox


def message():
    title = "About"
    text = "The aim of this app is to help student to prepare to their tests.\n\n" \
           "Sample text file\n\n" \
           "1. What is the capitol of Australia?\n\n" \
           "a) Vienna\n\n" \
           ">>>b) Canberra\n\n" \
           "c) Sydney\n\n" \
           "d) Cracow\n\n" \
           "EMPTY LINE\n\n" \
           "2. Next question\n\n" \
           "...\n\n" \
           "                                      Created by Jakub Was\n\n" \
           "                                      email: wasjakub3237@gmail.com"
    messagebox.showinfo(title, text)
