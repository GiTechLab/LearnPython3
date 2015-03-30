__author__ = 'YS1003'

print(3424)


def func_test(name, greeting_times=1):
    """ DocString --
    :rtype : object
    :param name:
    :param greeting_times:
    :return:
    """
    for index in range(0, greeting_times):
        print('Hello, ' + name)
        index+1


func_test('Yang SHEN')

func_test('MiaoMiao', 3)




