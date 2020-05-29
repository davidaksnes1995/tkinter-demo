from tkinter import *

root = Tk()


# display text
my_laber1 = Label(root, text="testing1")
my_laber2 = Label(root, text="testing2")

my_laber1.grid(row=10, column=12)
my_laber2.grid(row=100, column=12)
# my_laber1.pack()

# button
def myClick1():
    my_label3 = Label(root, text="hihihihi")
    # my_label3.grid(row=11, column=12)
    my_label3.pack()

def displaying():
    print('hi')

# my_button = Button(root, text="haisdgnaosg", state=DISABLED, padx=50, pady=50)
# my_button = Button(root, text="haisdgnaosg", padx=50, pady=50, command=myClick, fg="blue", bg="red")
# my_button.pack()
# my_button.grid(row=12, column=12)

# text input
e = Entry(root, width=50, bg="yellow", fg="black", borderwidth=30)
# e.pack()
e.grid(row=40, column=40)
e.insert(0, "Enter your name: ")
# e.get()

def myClick():
    my_label3 = Label(root, text=e.get())
    my_label3.grid(row=12, column=123)

# my_button = Button(root, text="haisdgnaosg", state=DISABLED, padx=50, pady=50)
my_button = Button(root, text="haisdgnaosg", padx=50, pady=50, command=myClick, fg="blue", bg="red")
# my_button.pack()
my_button.grid(row=12, column=12)

root.mainloop()