"""
元组 列表：一个可以放置任意类型数据的有序集合
区别：
    列表是动态的  mutable
        长度大小不固定，可以随意增减
    元素是静态的  immutable
        长度大小固定，无法改变

"""

if __name__ == '__main__':
    # 数据类型可以混合
    list01 = [1, 2, 'hello', 'world']
    print(list01)

    tuple01 = ('jason', 22)
    print(tuple01)

    # list改动，很简单
    list02 = [1, 2, 3, 4]
    list02[3] = 40
    print(list02)

    # tuple改动，报错 TypeError
    tuple02 = (1, 2, 3, 4)
    try:
        tuple02[3] = 40
    except TypeError as e:
        print('tuple is immutable.')
    # 如果非要改动，就给变量重新赋值
    tuple02 = (1, 2, 3, 40)

    # 元组相加
    tuple03 = tuple02 + (50,)
    print(tuple03)

    list02.append(50)
    print(list02)

    # list tuple 均支持负数索引
    print(list02[-1])
    print(tuple03[-1])

    # list tuple 均支持切片操作
    print(list02[1:3])
    print(tuple03[1:3])

    # list tuple 均可以任意嵌套
    list03 = [[1, 2, 3], [4, 5]]
    tuple04 = ((1, 2, 3), (4, 5))

    # list tuple 两者可以转换
    tuple05 = tuple(list03)
    print(tuple05)
    list04 = list(tuple05)
    print(list04)

    # list 常用的内置
    list05 = [3, 2, 3, 7, 8, 1]
    # list.count(item)  返回元素出现次数
    print(list05.count(3))
    # list.index(item)  返回元素第一次出现的索引
    print(list05.index(3))
    # list.reverse()    就地反转list
    list05.reverse()
    print(list05)
    # list.sort()       就地排序list，升序
    list05.sort()
    print(list05)

    # tuple 常用内置
    tuple06 = (3, 2, 3, 7, 8, 1)
    # tuple.count(item) 返回元素出现次数
    print(tuple06.count(3))
    # tuple.index(item) 返回元素第一次出现的索引
    print(tuple06.index(3))
    # reversed(tuple)   返回反序排列的生成器
    print(list(reversed(tuple06)))
    # sorted(tuple)     返回升序排列的生成器
    print(sorted(tuple06))

    # 储存方式是不一样的
