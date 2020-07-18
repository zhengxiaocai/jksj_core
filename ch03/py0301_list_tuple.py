"""
列表和元组：
    相同点：都是一个可以放置任意数据类型的有序集合

    不同点：
        列表：动态的，长度大小不固定，可以任意的增删修改元素 mutable
        元组：静态的，长度大小固定，不可以增删改元素 immutable
"""

if __name__ == '__main__':
    list01 = [1, 2, 'Hello', 'world']  # 列表中同时包含int String
    print(list01)

    tup01 = ('jason', 22)
    print(tup01)

    list02 = [1, 2, 3, 4]
    list02[3] = 40  # 索引从零开始
    print(list02)

    tup02 = (1, 2, 3, 4)
    # tup02[3] = 40     tuple object does not support item assignment

    # 如果想对一个已有的元组进行改变，只能重新开辟一块儿内存，重新赋值

    tup03 = (1, 2, 3, 4)
    tup04 = tup03 + (5,)  # 看似改变了，只是创建了个新的
    print(tup04)

    list03 = [1, 2, 3, 4]
    list03.append(5)  # 列表追加就很简单
    print(list03)

    # 与其他语言不同，支持负数索引 Java中支持不？
    list05 = [1, 2, 3, 4]
    print(list05[-1])
    tup05 = (1, 2, 3, 4)
    print(tup05[-1])

    # 都支持切片操作
    list06 = [1, 2, 3, 4]
    print(list06[1:3])
    tup06 = (1, 2, 3, 4)
    print(tup06[1:3])

    # 都可以随意嵌套
    list07 = [[1, 2, 3], [4, 5]]
    tup07 = ((1, 2, 3), (4, 5))

    # 两者可以通过list() tuple()函数互相转换
    print(list((1, 2, 3)))
    print(tuple([1, 2, 3]))

    # 列表 元组常用的内置函数
    list08 = [3, 2, 3, 7, 8, 1]
    # 获取元素出现的个数
    print(list08.count(3))
    # 获取元素第一次出现的索引
    print(list08.index(3))
    # 反序排列
    list08.reverse()  # 就地反转 元组没有
    print(list(reversed(list08)))
    # 升序排列
    list08.sort()  # 就地升序 元组没有
    print(sorted(list08))
    # 降序排列
    list08.sort(reverse=True)  # 就地降序
    print(sorted(list08, reverse=True))

    tup08 = (3, 2, 3, 7, 8, 1)
    # 获取元素出现的次数
    print(tup08.count(3))
    # 获取元素第一次出现的索引
    print(tup08.index(3))
    # 元组反序排列
    print(list(reversed(tup08)))
    # 元组降序排列
    print(sorted(tup08))
    # 元组升序排列
    print(sorted(tup08, reverse=True))

    # 列表和元组存储方式不一样
    list09 = [1, 2, 3]
    print(list09.__sizeof__())
    tup09 = (1, 2, 3)
    print(tup09.__sizeof__())

    list10 = []
    print(list10.__sizeof__())
    list10.append(1)
    print(list10.__sizeof__())
    list10.append(2)
    print(list10.__sizeof__())
    list10.append(3)
    print(list10.__sizeof__())
    list10.append(4)
    print(list10.__sizeof__())
    list10.append(5)
    print(list10.__sizeof__())

    # 如何选择：
    # 不可变：元组
    # 可变：列表

    """
        都是有序的，可以存储任意类型的集合。
    区别：
        列表是动态的，长度可变，可增删改元素。存储空间大于元组，性能逊于元组。
        元组是静态的，长度不可变，不可增删改元素。元组相对于列表轻量级，性能稍优。
    """

    list11 = [1, 2, 3, 4]
    list12 = [7, 8, 9]
    print(list11 + list12)
