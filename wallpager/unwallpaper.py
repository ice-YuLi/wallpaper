# encoding: utf-8
import os, sys
# pywin32
import win32api
import win32con
# pip install pygubu
from tkinter_test import *
import ctypes


def delete_picture(root):
    try:
        ls = os.listdir(root)
        ls_length = len(ls)
        if ls_length == 0:
            os.rmdir(root)
        else:
            for i in ls:
                c_path = os.path.join(root, i)
                if os.path.isdir(c_path):
                    delete_picture(c_path)
                else:
                    os.remove(c_path)
        os.rmdir(root)
    except Exception as e:
        print(e)


def delete_reg():
    reg_root = win32con.HKEY_CLASSES_ROOT
    # 键的路径（具体路径自行修改）
    reg_path = "Directory\\Background\\shell\\wallpaper\\command"
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
        key_flag = False
    else:
        key_flag = True
        win32api.RegCloseKey(key)
    if key_flag:
        try:
            # 删除值（key也有close方法，可以用with结构）
            # with win32api.RegOpenKeyEx(reg_root, reg_path, 0, reg_flags) as key:
            #     win32api.RegDeleteValue(key, 'test_value')
            # 删除键（需要获取其父键，通过父键删除子键）
            reg_parent, subkey_name = os.path.split(reg_path)
            try:
                key2 = win32api.RegOpenKeyEx(reg_root, reg_parent, 0, reg_flags)
            except Exception as e:
                print(e)
                key2 = None
            key_flag2 = False
            if key2 is None:
                key_flag2 = False
            else:
                key_flag2 = True
            if key_flag2:
                win32api.RegDeleteKeyEx(key2, subkey_name)
                win32api.RegCloseKey(key2)
                reg_parent2, subkey_name2 = os.path.split(reg_parent)
                try:
                    key3 = win32api.RegOpenKeyEx(reg_root, reg_parent2, 0, reg_flags)
                except Exception as e:
                    print(e)
                    key3 = None
                key_flag3 = False
                if key3 is None:
                    key_flag3 = False
                else:
                    key_flag3 = True
                if key_flag3:
                    win32api.RegDeleteKeyEx(key3, subkey_name2)
                    win32api.RegCloseKey(key3)
                else:
                    win32api.RegCloseKey(key3)
                    pass
            else:
                pass
        except Exception as e:
            print(e)
            sys.exit()


if __name__ == "__main__":
    delete_reg()
    delete_picture('D:\\wallpaper\\')
    ctypes.windll.user32.MessageBoxW(0, '删除成功', '右键快捷菜单设置（更换壁纸）', 0)
# pyinstaller -w -F -i blueWhaleLogo15.ico unwallpaper.py



