# >>TODO: 浅拷贝，重新分配一块内存，创建一个新的对象，里边的元素是对原对象中子对象的引用
import copy

if __name__ == '__main__':
    l1 = [1, 2, 3]
    l2 = list(l1)
    print(l2)
    print(l1 == l2)
    print(l1 is l2)

    s1 = set([1, 2, 3])
    s2 = set(s1)
    print(s2)
    print(s1 == s2)
    print(s1 is s2)

    l3 = l1[:]
    print(l3)
    print(l1 == l3)
    print(l1 is l3)

    """
    常见的浅拷贝方法：
    1. 使用数据类型本身的构造器 list02 = list(list01)
    2. 切片 list02 = list01[:]
    3. copy.copy(object) 适用于任何类型
    """

    # >>TODO：元组不一样，用: 和 tuple()并不能创建一份浅拷贝
    # >>TODO: 元组是静态的，只创建一次
    tuple01 = (1, 2, 3)
    tuple02 = tuple(tuple01)
    print(tuple01 == tuple02)
    print(tuple01 is tuple02)
