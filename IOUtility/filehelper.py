__author__ = 'Yang SHEN'

import platform

def get_osinfo():
    print(platform.system())
    print(platform.architecture())


get_osinfo()
