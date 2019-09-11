# encoding: utf-8
import urllib.request, sys

# page = urllib.request.urlopen('http://tieba.baidu.com/p/1753935195')
# print(page)
# htmlcode = page.read()
#
# pageFile = open('E:\\text_lj\\pagecode.txt','w')
# pageFile.write(htmlcode.decode("utf-8"))
# pageFile.close()
import win32api
import win32con
import win32gui

key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER, "Control Panel\\Desktop", 0, win32con.KEY_SET_VALUE)
win32api.RegSetValueEx(key, "WallpaperStyle", 0, win32con.REG_SZ, "2")
# 2：拉伸适应桌面；0：桌面居中
win32api.RegSetValueEx(key, "TileWallpaper", 0, win32con.REG_SZ, "0")
win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, 'D:\\wallpaper\\img7.jpg', 1 + 2)
# 关闭打开的键
win32api.RegCloseKey(key)