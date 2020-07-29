if __name__ == '__main__':
    list01 = [1, 2, 3, 4]
    for i in list01:
        print(i)

    # 遍历字典的键
    d = {'name': 'jason', 'dob': '2000-01-01', 'gender': 'male'}
    for k in d:
        print(k)

    # 遍历字典的值
    for v in d.values():
        print(v)

    # 同时遍历字典的键值
    for k, v in d.items():
        print('key: {}, value: {}'.format(k, v))

    # 通过索引访问
    list02 = [1, 2, 3, 4, 5, 6, 7]
    for index in range(0, len(list02)):
        if index < 5:
            print(list02[index])

    # 一种更方便的方式是通过 enumerate()
    for index, value in enumerate(list02):
        if index < 5:
            print(list02[index])

    # name_price: 产品名称(str)到价格(int)的映射字典
    # name_color: 产品名字(str)到颜色(list of str)的映射字典
    name_price = {}
    name_color = {}
    for name, price in name_price.items():
        if price >= 1000:
            continue
        for color in name_color[name]:
            if color == 'red':
                continue
            print('name: {}, color: {}'.format(name, color))

    # while循环，也可以遍历列表
    list03 = [1, 2, 3, 4]
    index = 0
    while index < len(list03):
        print(list03[index])
        index += 1

    """
    使用场景：
        for：如果是遍历一个已知的集合，找出满足条件的元素，或者进行某种操作
        while： 如果需要在满足某个条件前，不断地执行某项操作，并且没有特定的集合去遍历
    """

    # 比如交互式问答系统
    while True:
        text = input('Please enter your question, enter "q" to exit')
        if text == 'q':
            print('Exit system')
            break
        print("I don't know!")

    # 效率相关
    """
    range()函数直接由C写成，速度特别快。
    """
