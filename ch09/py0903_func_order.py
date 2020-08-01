# >>TODO: 如果是在函数里边调用函数，定义顺序就无所谓了
# >>TODO: 因为def是可执行语句，在函数调用之前都不存在，只要保证调用的时候函数已经声明


def my_func(message='None'):
    my_sub_func(message)


def my_sub_func(messge):
    # >>TODO: 参数可以带默认值
    print('Got a message: {}'.format(messge))


if __name__ == '__main__':
    my_func('Hello world')
    my_func()
