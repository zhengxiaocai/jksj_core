# >>TODO: 嵌套函数，外部变量可以访问不可以修改，如果要修改，用nonlocal
# >>TODO: 嵌套函数，外部变量和内部重名，内部会覆盖掉外部


def outer():
    x = 'local'

    def inner():
        nonlocal x
        x = 'nonlocal'
        print('inner')

    inner()
    print('outer:', x)


def outer2():
    x = 'local'

    def inner():
        x = 'nonlocal'
        print('inner')

    inner()
    print('outer:', x)


if __name__ == '__main__':
    outer()
    outer2()
