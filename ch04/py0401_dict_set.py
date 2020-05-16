"""
从py3.7开始，dict为有序的了。

相比于列表 元组，字典性能更优。
"""
import timeit

if __name__ == '__main__':
    # 声明字典的几种形式
    d1 = {'name': 'jason', 'age': 20, 'gender': 'male'}
    d2 = dict([('name', 'jason'), ('age', 20), ('gender', 'male')])
    d3 = dict(name='jason', age=20, gender='male')
    print(d1 == d2 == d3)

    # 声明集合的两种方式
    s1 = {1, 2, 3}
    s2 = set([1, 2, 3])
    print(s1 == s2)

    print(timeit.timeit('s1 = {1, 2, 3}'))
    print(timeit.timeit('s2 = set([1, 2, 3])'))
