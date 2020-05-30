from tkinter import *

root = Tk()
root.title("hihihi")

frame = LabelFrame(root, text="hihi", padx=50, pady=50)
frame.pack(padx=100, pady=100)


b = Button(frame, text="hihihihi", command=root.quit)
# b.pack()
b.grid(row=0, column=10)

b2 = Button(frame, text="hi", command=root.quit)
# b.pack()
b2.grid(row=1, column=10)


root.mainloop()