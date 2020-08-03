def square1(n):
    return n ** 2


if __name__ == '__main__':
    # 不推荐使用lambda定义赋值一个函数
    square2 = lambda x: x ** 2
    print(square1(2))
    print(square2(2))

    """
    1. lambda是个表达式expression，并不是一个语句statement
    2. 只能一行，不能扩展为多行；专注处理简单问题
    """
    # 可以用在def不能用的地方，比如 列表内部
    print([(lambda x: x ** 2)(x) for x in range(10)])
    print([x * x for x in range(10)])
    # 可以当做某些函数的参数
    list01 = [(1, 20), (3, 0), (9, 10), (2, -1)]
    list01.sort(key=lambda x: x[1])
    print(list01)

    """
    使用函数的目的：
        1. 减少代码的重复性
        2. 模块化代码
    """

    """
    函数式编程，不要对元素有操作，使其变化
    """

    # 匿名函数使用场景：
    # >>TODO: 程序中需要使用一个函数完成一个简单的函数，并且只用一次。
