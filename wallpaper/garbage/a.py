
from tkinter import *
from tkinter.filedialog import askopenfilename


def choosepic():
    path_ = askopenfilename()
    path.set(path_)
    img_gif = PhotoImage(file='xxx.gif')
    l1.config(image=img_gif)


root = Tk()
path = StringVar()
Button(root, text='选择图片', command=choosepic).pack()
e1 = Entry(root, state='readonly', text=path)
e1.pack()
l1 = Label(root)
l1.pack()
root.mainloop()