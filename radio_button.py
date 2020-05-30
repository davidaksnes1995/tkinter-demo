from tkinter import *

root = Tk()

# r = IntVar()
# r.set(1)

MODES = [
    ("A", "a"),
    ("V", "v"),
    ("I", "i"),
    ("L", "l"),
]

alphabeta = StringVar()
alphabeta.set("A")

for upp, low in MODES:
    Radiobutton(root, text=upp, variable=alphabeta, value=low).pack(anchor=W)

def click(value):
    myLabel = Label(root, text=value)
    myLabel.pack()

# myLabel1 = Label(root, text=alphabeta.get())
# myLabel1.pack()

myButton = Button(root, text="hihi", command=lambda: click(alphabeta.get()))
myButton.pack()

# Radiobutton(root, text="op1", Variable=r, value=1, command=lambda: click(1)).pack()

root.mainloop()