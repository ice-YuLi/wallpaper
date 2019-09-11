# encoding: utf-8
import win32api
import win32con
import ctypes
import os

# print(win32con.HKEY_CURRENT_USER)
# print(win32con.KEY_SET_VALUE)
# print(win32con.REG_SZ)
# print(win32con.HKEY_CURRENT_USER)
# print(win32con.HKEY_CURRENT_USER)
# reg_parent, subkey_name = os.path.split('SOFTWARE\Microsoft\test_key')
# print(reg_parent)
# print(subkey_name)
# print(os.path)

# ctypes.windll.user32.SystemParametersInfoW(20, 0, 'E:\\test_lj\\img8.jpg', 0)  # 设置桌面壁纸

# 根节点
reg_root = win32con.HKEY_CLASSES_ROOT
# 键的路径（具体路径自行修改）
reg_path_parent = "Directory\\Background\\shell\\wallpaper"
reg_path_children = reg_path_parent + "\\command"
# 权限和参数设置
reg_flags = win32con.WRITE_OWNER|win32con.KEY_WOW64_64KEY|win32con.KEY_ALL_ACCESS
try:
    key = win32api.RegOpenKeyEx(reg_root, reg_path, 0, reg_flags)
    for item in win32api.RegEnumKeyEx(key):
        print(item)
        i = 0
        while True:
            print(win32api.RegEnumValue(key, i))
            i += 1
except Exception as e:
    print(e)
    key = None
    pass
print(key)
keyFlag = False
if key is None:
    keyFlag = False
else:
    keyFlag = True
print(keyFlag)

try:
    # 直接创建（若存在，则为获取）
    key, _ = win32api.RegCreateKeyEx(reg_root, reg_path_parent, reg_flags)
    win32api.RegSetValueEx(key, '', 0, win32con.REG_SZ, '更换壁纸')
    key, _ = win32api.RegCreateKeyEx(reg_root, reg_path_children, reg_flags)
    win32api.RegSetValueEx(key, '', 0, win32con.REG_SZ, '我是猪儿子')
except Exception as e:
    print(e)
    key = None
print(key)