from tkinter import *
from tkinter import filedialog

root = Tk()

root.filename = filedialog.askopenfilename(initialdir=r"C:\Users\xxxda\Documents\GitHub\tkinter-demo\texts", \
    title="Select a File", filetypes=(("a file", "a"), ("all files", "*.*")))

my_label = Label(root, text=root.filename).pack()

mainloop()