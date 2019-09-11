# encoding: utf-8
import ctypes
# pip install pygubu
from tkinter_test import *
from tkinter_test.filedialog import askdirectory
import os
value = ctypes.windll.user32.MessageBoxW(0, '设置成功，请点击右键查看！！！', '右键快捷菜单设置（更换壁纸）', 1)
print(value)
# application_window = Tk()
# my_file_types = [('all files', '.*'), ('text files', '.txt')]
# filename = ''
# path = StringVar()
# print(path)
# def xz():
#     filename = tkinter.filedialog.askopenfilename(parent=application_window,
#                                         initialdir=os.getcwd(),
#                                         title='Please select a file:',
#                                         filetypes=my_file_types)
#     # filename = tkinter.filedialog.askopenfilename()
#     if filename != '':
#         lb.config(text='您选择的文件是：'+filename)
#     else:
#         lb.config(text='您没有选择任何文件')
#
#
# lb = Label(application_window, text='')
# lb.pack()
# btn = Button(application_window, text='选择.exe文件', command=xz)
# btn.pack()
# application_window.mainloop()
# print(filename)
#
# root = Tk()
# path = StringVar()
#
# def selectPath():
#     path_ = askdirectory()
#     path.set(path_)
#     print(path.get())
#
#
# def submit():
#     print('我是猪')
#     root.destroy()
#
#
# Label(root, text='目标路径:').grid(row=0, column=0)
# Entry(root, textvariable=path).grid(row=0, column=1)
# Button(root, text='路径选择', command=selectPath).grid(row=0, column=2)
# Button(root, text='确定', command=submit).grid(row=0, column=3)
# root.mainloop()



# from tkinter import *
#
# root=Tk()
# root.geometry('80x80+0+0')
# print(root.pack_slaves())
# for i in range(5):
#     Label(root,text='pack'+str(i)).pack()
# print(root.pack_slaves())
#
# root.mainloop()

# ##提醒OK消息框
# win32api.MessageBox(0, '这是一个测试提醒OK消息框', '提醒', win32con.MB_OK)
#
# ##是否信息框
# win32api.MessageBox(0, '这是一个测试是否信息框', '提醒', win32con.MB_YESNO)
#
# ##说明信息框
# win32api.MessageBox(0, '这是一个测试说明信息框', '提醒', win32con.MB_HELP)
#
# ####警告信息框
# win32api.MessageBox(0, '这是一个测试警告信息框', '提醒', win32con.MB_ICONWARNING)
#
# ##疑问信息框
# win32api.MessageBox(0, '这是一个测试疑问信息框', '提醒', win32con.MB_ICONQUESTION)
#
# ##提示信息框
# win32api.MessageBox(0, '这是一个测试提示信息框', '提醒', win32con.MB_ICONASTERISK)
#
# ##确认信息框
# win32api.MessageBox(0, '这是一个测试确认信息框', '提醒', win32con.MB_OKCANCEL)
#
# ##重试信息框
# win32api.MessageBox(0, '这是一个测试重试信息框', '提醒', win32con.MB_RETRYCANCEL)
#
# ##是否取消信息框
# win32api.MessageBox(0, '这是一个测试是否取消信息框', '提醒', win32con.MB_YESNOCANCEL)

# root = 'E:\\test_lj'
# for root, dirs, files in os.walk(root, topdown=False):
    # for name in files:
    #     print(os.path.join(root, name))
    # for name in dirs:
    #     print(os.path.join(root, name))
    # print(root)
    # print(dirs)
    # print(files[0])
    # print(os.path.join('E:\\test_lj', files[0]))
    # os.remove()

    # ls = os.listdir(root)
    # ls_length = len(ls)
    # if ls_length == 2:
    #     print(True)
    # else:
    #     print(False)
# reg_root = win32con.HKEY_CLASSES_ROOT
# # 键的路径（具体路径自行修改）
# reg_path = r'Directory\\Background\\shell\\wallpaper'
#
# # 权限和参数设置
# reg_flags = win32con.WRITE_OWNER | win32con.KEY_WOW64_64KEY | win32con.KEY_ALL_ACCESS
# reg_parent, subkey_name = os.path.split(reg_path)
# # try:
# print(reg_parent)
# print(subkey_name)
# key = win32api.RegOpenKeyEx(reg_root, reg_parent, 0, reg_flags)
# win32api.RegDeleteKeyEx(key, subkey_name)
# win32api.RegCloseKey(key)
# with (win32api.RegOpenKeyEx(reg_root, reg_parent, 0, reg_flags)) as f:
#     print(f)
    # win32api.RegDeleteKeyEx(key, subkey_name)
# except Exception as e:
#     print(e)
# print(reg_parent)
# print(subkey_name)




