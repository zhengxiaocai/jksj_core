# >>TODO: 可以确保内部函数的隐私，内部函数只能外部函数调用，不会暴露在全局变量中。
# >>TODO: 合理的嵌套能提升函数的运行效率
# >>TODO: 如果下边的检查写到递归里，每次递归一次都要执行检查，效率低下。


def f1():
    print('Hello')

    def f2():
        print('world')

    f2()


def factorial(num):
    if not isinstance(num, int):
        raise Exception('input must be a int')
    if num < 0:
        raise Exception('input must be greater or equal to 0')

    def inner_factorial(input_num):
        if input_num <= 1:
            return 1
        else:
            return input_num * inner_factorial(input_num - 1)

    return inner_factorial(num)


if __name__ == '__main__':
    f1()
    # f2()
