__author__ = 'Yang SHEN'

import platform
import os

def get_osinfo():
    #Refer to: http://www.cnblogs.com/rollenholt/archive/2012/04/23/2466179.html

    print(platform.system())
    print(platform.architecture())
    print(os.getcwd())#get current dir
    print(os.listdir(os.getcwd()))#list all folders and files
    print(os.path.isdir(os.getcwd()))
    print(os.path.isfile(os.getcwd()))
    print(os.path.exists(os.getcwd()))
    print(os.path.exists(os.getcwd() + "\\filehelper.py"))
    print(os.path.split(os.getcwd() + "\\filehelper.py"))#get container folder and file
    print(os.path.splitext(os.getcwd() + "\\filehelper.py"))

get_osinfo()

