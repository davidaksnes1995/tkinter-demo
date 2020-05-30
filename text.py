from os import listdir
from os.path import isfile, join

from tkinter import *

root = Tk()

abs_path = r"C:\Users\xxxda\Documents\GitHub\tkinter-demo\texts"
file_names = [f for f in listdir(abs_path) if isfile(join(abs_path, f))]

status = Label(root, text="File 1 of " + str(len(file_names)), bd=1, relief=SUNKEN, anchor=E)

file_lable = Label(root, text=file_names[0])
file_lable.grid(row=0, column=0, padx=10, pady=10, columnspan=3)


def back(text_number):
    global file_lable
    global button_forward
    global button_back

    file_lable.grid_forget()
    file_lable = Label(root, text=file_names[text_number - 1])
    button_forward = Button(root, text=">>", command=lambda: forward(text_number + 1))
    button_back = Button(root, text="<<", command=lambda: back(text_number - 1))

    status = Label(root, text="File " + str(text_number) + " of " + str(len(file_names)), bd=1, relief=SUNKEN, anchor=E)

    if text_number == 1:
        button_back = Button(root, text="<<", state=DISABLED)

    file_lable.grid(row=0, column=0, padx=10, pady=10, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)
    status.grid(row=3, column=0, columnspan=3, sticky=W+E)


def forward(text_number):
    global file_lable
    global button_forward
    global button_back

    file_lable.grid_forget()
    file_lable = Label(root, text=file_names[text_number - 1])
    button_forward = Button(root, text=">>", command=lambda: forward(text_number + 1))
    button_back = Button(root, text="<<", command=lambda: back(text_number - 1))

    status = Label(root, text="File " + str(text_number) + " of " + str(len(file_names)), bd=1, relief=SUNKEN, anchor=E)

    if text_number == 3:
        button_forward = Button(root, text=">>", state=DISABLED)

    file_lable.grid(row=0, column=0, padx=10, pady=10, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)
    status.grid(row=3, column=0, columnspan=3, sticky=W+E)


button_back = Button(root, text="<<", state=DISABLED)
button_exit = Button(root, text="Exit", command=root.quit)
button_forward = Button(root, text=">>", command=lambda: forward(2))

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2, pady=10)
status.grid(row=3, column=0, columnspan=3, sticky=W+E)

root.mainloop()