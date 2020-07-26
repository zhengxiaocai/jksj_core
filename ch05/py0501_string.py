def calculate_similarity(item, item1):
    """
    三引号主要用于多行文本的场景，比如函数注释
    :param item: 1st item
    :param item1: 2ed item
    :return: None
    """
    pass


if __name__ == '__main__':
    # 定义方式
    name = 'jason'
    city = 'beijing'
    text = 'welcome to jike shijian'

    # 单引号 双引号 三引号 相同
    s1 = 'hello'
    s2 = "hello"
    s3 = """hello"""
    print(s1 == s2 == s3)

    # 内嵌引号
    s4 = "I'm a student"

    # 转义，一个转义字符一个长度
    s5 = 'a\nb\tc'
    print(s5)
    print(len(s5))

    # 字符串常用操作，支持索引 切片 遍历
    name1 = 'jason'
    print(name1[0])
    print(name1[0:3])

    for i in name1:
        print(i, end='\t')

    # 字符串immutable 不可变
    try:
        s5[0] = 'a'
    except TypeError:
        print('TypeError')

    # 如果非要改变，只能通过创建新的字符串
    s6 = 'hello'
    print('H' + s6[1:])
    print(s6.replace('h', 'H'))

    # += py2.5以后，如果没有别的引用，就会直接扩充当前string，效率高
    s7 = ''
    for n in range(0, 10000):
        s7 += str(n)

    # 字符串拼接，除了使用+，还可以使用str的内置join方法
    list01 = []
    for n in range(0, 10000):
        list01.append(str(n))
    print(''.join(list01))

    # str.split(mark)
    path = 'hive://ads/training_table'
    # 取ads
    name_space = path.split('//')[1].split('/')[0]
    print(name_space)
    # 取training_table
    table = path.split('//')[1].split('/')[1]
    print(table)

    # str.strip(mark)  str.lstrip(mark)  str.rstrip(mark)
    s = ' my name is jason '
    print(s.strip())

    # str.find(sub, start, end)
    print(s.find('name'))

    # str.format()
    print('no data available for person with id: {}, name: {}'.format('666', name))
    # 之前的格式 %
    print('no data available for person with id: %s, name: %s' % ('888', name))
