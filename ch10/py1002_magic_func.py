# map filter reduce
from functools import reduce

if __name__ == '__main__':
    # map(func, iterable)
    list01 = [1, 2, 3, 4, 5]
    new_list = map(lambda x: x * 2, list01)
    print(list(new_list))
    # >>TODO: map比列表生成式，快
    # >>TODO: map是用C语言写成，运行时不需要通过Python解释器间接调用，并且内部做了优化

    # filter(func, iterable)
    new_list1 = filter(lambda x: x % 2 == 0, list01)
    print(list(new_list1))

    # reduce(func, iterable)
    product = reduce(lambda x, y: x * y, list01)
    print(product)

    """
    1. 数据量大的话，一般倾向于使用函数式编程。
    2. 数据量不大的情况下，想要程序PythonIC，列表表达式
    """