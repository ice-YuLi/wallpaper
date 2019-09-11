# encoding: utf-8
import ctypes
# pywin32
import win32api
import win32con
# pip install pygubu
from tkinter_test import *
from tkinter_test.filedialog import askdirectory

root = Tk()
path = StringVar()


def set_reg(full_path):
    reg_root = win32con.HKEY_CLASSES_ROOT
    # 键的路径（具体路径自行修改）
    reg_path = "Directory\\Background\\shell\\wallpaper"
    reg_path_children = reg_path + "\\command"
    # 权限和参数设置
    reg_flags = win32con.WRITE_OWNER | win32con.KEY_WOW64_64KEY | win32con.KEY_ALL_ACCESS
    try:
        # 判断注册表中键值是否存在
        key = win32api.RegOpenKeyEx(reg_root, reg_path, 0, reg_flags)
    except Exception as e:
        print(e)
        key = None
    key_flag = False
    if key is None:
        key_flag = True
    else:
        key_flag = False
    if key_flag:
        try:
            # 直接创建（若存在，则为获取）
            key, _ = win32api.RegCreateKeyEx(reg_root, reg_path, reg_flags)
            win32api.RegSetValueEx(key, '', 0, win32con.REG_SZ, '更换壁纸')
            key, _ = win32api.RegCreateKeyEx(reg_root, reg_path_children, reg_flags)
            win32api.RegSetValueEx(key, '', 0, win32con.REG_SZ, full_path)
            ctypes.windll.user32.MessageBoxW(0, '设置成功，请点击右键查看！！！', '右键快捷菜单设置（更换壁纸）', 0)
        except Exception as e:
            print(e)
            ctypes.windll.user32.MessageBoxW(0, '设置设置失败，为什么啊！！！', '右键快捷菜单设置（更换壁纸）', 0)
    else:
        value = ctypes.windll.user32.MessageBoxW(0, '更换壁纸快捷键已经存在，点击确认替换', '右键快捷菜单设置（更换壁纸）', 1)
        if value is 1:
            key, _ = win32api.RegCreateKeyEx(reg_root, reg_path_children, reg_flags)
            win32api.RegSetValueEx(key, '', 0, win32con.REG_SZ, full_path)
            ctypes.windll.user32.MessageBoxW(0, '设置成功，请点击右键查看！！！', '右键快捷菜单设置（更换壁纸）', 0)
        else:
            ctypes.windll.user32.MessageBoxW(0, '操作已取消', '右键快捷菜单设置（更换壁纸）', 0)
            pass


def select_path():
    path_ = askdirectory()
    path.set(path_)
    print(path.get())


def submit():
    full_path = path.get()
    if path.get():
        set_reg(full_path)
    else:
        ctypes.windll.user32.MessageBoxW(0, '路径不能为空，请选择.exe文件', '右键快捷菜单设置（更换壁纸）', 0)


def create_box():
    Label(root, text='目标路径:').grid(row=0, column=0)
    Entry(root, textvariable=path).grid(row=0, column=1)
    Button(root, text='路径选择', command=select_path).grid(row=0, column=2)
    Button(root, text='确定', command=submit).grid(row=0, column=3)
    root.mainloop()


if __name__ == "__main__":
    create_box()