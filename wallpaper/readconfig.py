# encoding utf-8
import configparser
import os
import sys


def readconfig():
    address = 'get_url1'
    options = '[]'
    full_path = sys.executable
    print(full_path)
    full_path = full_path[0:full_path.rindex('\\')]
    # full_path = os.getcwd()
    print(full_path)
    try:
        cf = configparser.ConfigParser()
        cf.read(full_path + '\\config.ini')
        print(full_path + '\\config.ini')
        address = cf.get("wallpaper", "address")
        options = cf.get("wallpaper", "options")
    except Exception as e:
        print(e)

    return address, options


if __name__ == "__main__":
    readconfig()