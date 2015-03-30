__author__ = 'YS1003'

# import sys
print('Hello Python.')


def my_func(name, greeting_times=1):
    """Docstring: This is a test for function in Python."""
    try:
        for index in range(0, greeting_times):
            # if isinstance(name, object):
            print('Hello, ' + name)
    except:
        print('Error found..')

my_func('Yang Shen')

my_func('MiaoMiao', 3)

my_func('MiaoMiao', 'a')

print(my_func.__doc__)

# "print(sys.path)"""