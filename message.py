from tkinter import *
from tkinter import messagebox

root = Tk()

def p():
    # messagebox.showinfo("hihi", "hhihihi")
    # messagebox.showwarning("hihi", "hhihihi")
    # messagebox.showerror("hihi", "hhihihi")
    # messagebox.askquestion("hihi", "hhihihi")
    # messagebox.askokcancel("hihi", "hhihihi")
    respone = messagebox.askyesno("hihi", "hhihihi")
    Label(root, text=respone).pack()



Button(root, text="hihi", command=p).pack()

root.mainloop()