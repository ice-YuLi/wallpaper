import tkinter as tk

from PIL import ImageTk, Image
import pickle

# 创建主窗口
window = tk.Tk()
window.title('更换壁纸中。。。')
window.geometry('400x400')

# 添加背景图
canvas = tk.Canvas(window, bg='white')  # 创建画布
image_file = ImageTk.PhotoImage(file='timg.gif')  # 加载图片文件

image = canvas.create_image(0, 0, anchor='nw', image=image_file)  # 将图片置于画布上
canvas.pack()  # 放置画布
window.mainloop()

# root = tk.Tk()
# image_file = tk.PhotoImage(file='timg.gif')
# # image_file = ImageTk.PhotoImage(file='timg.gif')  # 加载图片文件
# panel = tk.Label(root, image = image_file, width = '100',height = '100')
# panel.pack(side = "bottom", fill = "both", expand = "yes")
# root.mainloop()
