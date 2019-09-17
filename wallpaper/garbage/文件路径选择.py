# encoding: utf-8
import tkinter
from tkinter.filedialog import askdirectory

# top = tkinter.Tk()
# # 进入消息循环
# top.mainloop()
#
root = tkinter.Tk()
path = tkinter.StringVar()

def selectPath():
    path_ = askdirectory()
    path.set(path_)
    print(path.get())


def submit():
    print('我是猪')
    root.destroy()


tkinter.Label(root, text='目标路径:').grid(row=0, column=0)
tkinter.Entry(root, textvariable=path).grid(row=0, column=1)
tkinter.Button(root, text='路径选择', command=selectPath).grid(row=0, column=2)
tkinter.Button(root, text='确定', command=submit).grid(row=0, column=3)
root.mainloop()