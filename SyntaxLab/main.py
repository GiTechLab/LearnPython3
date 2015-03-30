__author__ = 'YS1003'

import sys
print('Hello Python.')


def my_func(name, greeting_times=1):
    for index in range(0, greeting_times):
        """if isinstance(name, object):"""
        print('Hello, ' + name)

my_func('Yang Shen')

my_func('MiaoMiao', 3)

print(sys.path)