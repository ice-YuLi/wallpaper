# encoding: utf-8
import time
import threading
from tkinter import *
import win32api
import win32con
import win32gui
import requests
import json
import random
import os, sys
import ctypes
from downloadPicture import download_picture


replace_wallpaper_flag = True
set_reg_flag = True


def replace_wallpaper():
    global replace_wallpaper_flag
    bmp_file = download_picture()
    # 设置壁纸 方法一: 图片格式必须为BMP
    key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER, "Control Panel\\Desktop", 0, win32con.KEY_SET_VALUE)
    win32api.RegSetValueEx(key, "WallpaperStyle", 0, win32con.REG_SZ, "2")
    win32api.RegSetValueEx(key, "TileWallpaper", 0, win32con.REG_SZ, "0")
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, bmp_file, 1 + 2)
    win32api.RegCloseKey(key)
    replace_wallpaper_flag = False
    # 设置壁纸 方法二: 对格式没有要求
    # ctypes.windll.user32.SystemParametersInfoW(20, 0, bmpFile, 0)  # 设置桌面壁纸


def set_reg():
    global set_reg_flag
    # full_path = sys.argv[0]
    full_path = sys.executable
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
            win32api.RegSetValueEx(key, 'Icon', 0, win32con.REG_SZ, full_path)
            win32api.RegCloseKey(key)
            key, _ = win32api.RegCreateKeyEx(reg_root, reg_path_children, reg_flags)
            win32api.RegSetValueEx(key, '', 0, win32con.REG_SZ, full_path)
            win32api.RegCloseKey(key)
            set_reg_flag = False
        except Exception as e:
            win32api.RegCloseKey(key)
            ctypes.windll.user32.MessageBoxW(0, '设置设置失败，为什么啊！！！', '右键快捷菜单设置（更换壁纸）', 0)
            set_reg_flag = False
    else:
        value, key_type = win32api.RegQueryValueEx(key, 'Icon')
        win32api.RegCloseKey(key)
        if value != full_path:
            key, _ = win32api.RegCreateKeyEx(reg_root, reg_path, reg_flags)
            win32api.RegSetValueEx(key, 'Icon', 0, win32con.REG_SZ, full_path)
            win32api.RegCloseKey(key)
            key, _ = win32api.RegCreateKeyEx(reg_root, reg_path_children, reg_flags)
            win32api.RegSetValueEx(key, '', 0, win32con.REG_SZ, full_path)
            win32api.RegCloseKey(key)
        set_reg_flag = False


def update_progress_bar():
    for percent in range(1, 101):
        if replace_wallpaper_flag is True or set_reg_flag is True:
            green_length = int(sum_length * percent / 100)
            canvas_progress_bar.coords(canvas_shape, (green_length-50, 0, green_length, 25))
            if percent is 100:
                update_progress_bar()
            time.sleep(0.02)
        else:
            break
    top.destroy()


def run():
    th1 = threading.Thread(target=update_progress_bar)
    th2 = threading.Thread(target=replace_wallpaper)
    th3 = threading.Thread(target=set_reg)

    th1.setDaemon(True)
    th1.start()
    th2.start()
    th3.start()


top = Tk()
# top.iconbitmap('./blueWhaleLogo15.ico')
top.title('只只，正在努力设置中……')
top.geometry('300x50+290+100')
top.resizable(False, False)
top.config(bg='#535353')

# 进度条
sum_length = 200
canvas_progress_bar = Canvas(top, width=sum_length, height=20)
canvas_shape = canvas_progress_bar.create_rectangle(0, 0, 0, 25, fill='green')
canvas_progress_bar.place(relx=0.5, rely=0.5, anchor=CENTER)

run()
top.mainloop()

# pyinstaller -w -F -i blueWhaleLogo15.ico wallpaper.py
