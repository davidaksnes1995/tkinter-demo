from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("icon, image, exit")
root.iconbitmap(r'C:\Users\xxxda\Documents\GitHub\tkinter-demo\icon\\favicon.ico')

button_quit = Button(root, text="Exit", command=root.quit)
button_quit.pack()

root.mainloop()