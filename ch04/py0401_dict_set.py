"""
从py3.7开始，dict为有序的了。

相比于列表 元组，字典性能更优。
特别是查找 添加 删除操作时，常数时间复杂度内完成。

集合和字典基本相同，唯一的区别，集合没有键值配对，是一系列无序的、唯一的元素组合。

测试执行速度：timeit.timeit('python script')
"""
import time


def find_product_price(products, product_id):
    for id, price in products:
        if id == product_id:
            return price
    return None


def find_unique_price_using_list(products):
    unique_price_list = []
    for _, price in products:
        if price not in unique_price_list:
            unique_price_list.append(price)
    return len(unique_price_list)


def find_unique_price_using_set(products):
    unique_price_set = set()
    for _, price in products:
        unique_price_set.add(price)
    return len(unique_price_set)


if __name__ == '__main__':
    # 字典的创建方式
    dict01 = {'name': 'jason', 'age': 20, 'gender': 'male'}
    dict02 = dict({'name': 'jason', 'age': 20, 'gender': 'male'})
    dict03 = dict([('name', 'jason'), ('age', 20), ('gender', 'male')])
    dict04 = dict(name='jason', age=20, gender='male')
    print(dict01 == dict02 == dict03 == dict04)

    # 集合的创建方式
    set01 = {1, 2, 3}
    set02 = set([1, 2, 3])
    print(set01 == set02)

    # 字典和集合，无论键或者值，都是混合类型
    set03 = {1, 'hello', 5.0}

    # 元素访问，可以直接访问键；如果不存在，就会抛出异常
    dict05 = {'name': 'jason', 'age': 20}
    print(dict05['name'])
    # print(dict05['location']) KeyError: 'location'

    # 相比于这种粗暴的方式，用get会更温和一些，因为，可以提供一个默认值
    # 如果不提供默认值，获取不到的时候，默认返回None
    print(dict05.get('name'))
    print(dict05.get('location'))
    print(dict05.get('location', 'None'))

    # 集合不支持索引操作，因为集合本质上是个哈希表
    # print(set03[0])   TypeError: 'set' object is not subscriptable

    # 要判断一个元素在不在字典 集合内，可以用in
    dict06 = {'name': 'jason', 'age': 20}
    set04 = {1, 2, 3}
    print('name' in dict06)
    print('location' in dict06)
    print(1 in set04)
    print(4 in set04)

    # 增加 删除 更新
    dict06['gender'] = 'male'
    dict06['dob'] = '1992-05-13'
    print(dict06)
    dict06['dob'] = '1993-05-13'
    print(dict06)
    dict06.pop('dob')
    print(dict06)

    set04.add(4)
    print(set04)
    set04.remove(1)
    print(set04)

    # 排序
    dict07 = {'b': 1, 'a': 2, 'c': 10}
    dict07_sorted_by_key = sorted(dict07.items(), key=lambda x: x[0])
    print(dict07_sorted_by_key)
    dict07_sorted_by_value = sorted(dict07.items(), key=lambda x: x[1])
    print(dict07_sorted_by_value)

    set05 = {3, 4, 2, 1}
    print(sorted(set05))

    products_list = [(143121312, 100), (432314553, 30), (32421912367, 150)]
    print('The price of product 432314553 is {}'.format(find_product_price(products_list, 432314553)))

    products_dict = {143121312: 100, 432314553: 30, 32421912367: 150}
    print('The price of product 432314553 is {}'.format(products_dict.get(432314553)))

    print('number of unique price is {}'.format(find_unique_price_using_list(products_list)))

    print('number of unique price is {}'.format(find_unique_price_using_set(products_list)))

    id = [x for x in range(0, 10000)]
    price = [x for x in range(20000, 30000)]
    products = list(zip(id, price))

    start_using_list = time.perf_counter()
    find_unique_price_using_list(products)
    end_using_list = time.perf_counter()
    print('time elapse using list: {}'.format(end_using_list - start_using_list))

    start_using_set = time.perf_counter()
    find_unique_price_using_set(products)
    end_using_set = time.perf_counter()
    print('time elapse using set: {}'.format(end_using_set - start_using_set))
