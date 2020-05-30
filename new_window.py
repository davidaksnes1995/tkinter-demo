from tkinter import *

root = Tk()

myLabel = Label(root, text="hihi")
myLabel.pack()

def open():
    # the code below is all contained in top
    top = Toplevel()
    myLabe2 = Label(top, text="hihihihi")
    myLabe2.pack()
    Button(top, text="hihi", command=top.destroy).pack()



btn = Button(root, text="hihikkkkkk", command=open)
btn.pack()

# the code below is all contained in top
# top = Toplevel()
# myLabe2 = Label(top, text="hihihihi")
# myLabe2.pack()


mainloop()