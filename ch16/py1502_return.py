def my_func1(b):
    b = 2


def my_func2(b):
    # >>TODO: 那么如何改变不可变变量呢，return
    b = 2
    return b


def my_func3(l2):
    # >>TODO: 当参数为可变对象，改变他，就会影响所有指向他的变量
    l2.append(4)


def my_func4(l2):
    # >>TODO: 原可变参数不变
    l2 = l2 + [4]


def my_func5(l2):
    # >>TODO: 如果要改变用+这种形式，还是return
    l2 = l2 + [4]
    return l2


if __name__ == '__main__':
    a = 1
    my_func1(a)
    print(a)

    # >>TODO: 当执行函数体内的 b=2 赋值操作时，会重新创建一个新对象。

    c = 1
    c = my_func2(c)
    print(c)

    l1 = [1, 2, 3]
    my_func3(l1)
    print(l1)

    l2 = [1, 2, 3]
    my_func4(l2)
    print(l2)

    l3 = [1, 2, 3]
    l3 = my_func5(l3)
    print(l3)

    # >>TODO: 区分 “改变变量” 和 “重新赋值”
    # >>TODO: 推荐最后一种，return
    # >>TODO: Python中的参数传递为赋值传递。

    # >>TODO: 总结
    # >>TODO: 如果可变，当其改变时，所有的引用都会变
    # >>TODO: 如不可变，简单的赋值只能影响其中一个变量的值。

    # 如果改变一个值，第一就是把可变当做参数传入，然后改变；
    # 第二就是，创建一个新变量，返回给原变量
