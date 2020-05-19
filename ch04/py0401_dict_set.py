"""
从py3.7开始，dict为有序的了。

相比于列表 元组，字典性能更优。

测试执行速度：timeit.timeit('python script')
"""
import timeit


def find_product_price(products, product_id):
    for product in products:
        if product[0] == product_id:
            return product[1]
    return None


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

    # 根据键访问，如果键不存在，就会报异常KeyError
    print(d3['name'])
    try:
        print(d3['abc'])
    except KeyError as e:
        print('Key Error.')

    # 可以用字典的get方法，指定找不到的时候的默认值。默认是None
    print(d3.get('age'))
    print(d3.get('abc'))
    print(d3.get('abc', 'abc not found'))

    # 集合不支持索引操作，集合是一个哈希表。TypeError
    try:
        print(s1[0])
    except TypeError as e:
        print('集合不支持索引操作。', e)

    # 判断是否是字典/集合的一项 item in dict/set
    print('name' in d1)
    print('names' in d1)
    print(1 in s1)

    # 增加 dict[new_key] = value
    d1['dob'] = '1999-02-01'
    print(d1)

    # 删除 dict.pop(key)；pop(不存在的key) 报错KeyError
    d1.pop('name')
    print(d1)
    try:
        d1.pop('abc')
    except KeyError as e:
        print('KeyError')

    # 集合增加 set.add(value)
    s1.add(4)
    print(s1)

    # 集合删除 set.remove(value)
    s1.remove(1)
    print(s1)

    # 排序
    d4 = {'b': 1, 'a': 2, 'c': 10}
    d4_sorted_by_key = sorted(d4.items(), key=lambda x: x[0])
    d4_sorted_by_value = sorted(d4.items(), key=lambda x: x[1])
    print(d4_sorted_by_key)
    print(d4_sorted_by_value)

    s3 = {3, 4, 2, 1}
    print(sorted(s3))

    # 实际应用，如果存在list里
    products_list = [(143121312, 100), (432314553, 30), (32421912367, 150), (937153201, 30)]
    print(f'The price of product 432314553 is {find_product_price(products_list, 432314553)}')

    # 实际应用，在字典中
    products_dict = {143121312: 100, 432314553: 30, 32421912367: 150}
    print(f'The price of product 432314553 is {products_dict[432314553]}')





