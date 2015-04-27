__author__ = 'Yang SHEN'

import platform

def get_current_os_info():
    print("Start to check current OS info.")
    print(platform.system())# Windows
    print(platform.architecture())# '64bit', 'WindowsPE'
    print(platform.python_version())

get_current_os_info()