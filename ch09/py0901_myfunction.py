def my_func(message):
    print('Got a message: {}'.format(message))


def my_sum(a, b):
    return a + b


def find_largest_element(l):
    if not isinstance(l, list):
        print('input is not type of list')
        return
    if len(l) == 0:
        print('empty list')
        return
    largest_element = l[0]
    for item in l:
        if item > largest_element:
            largest_element = item
    print('largest element is: {}'.format(largest_element))


if __name__ == '__main__':
    my_func('Hello world')
    result = my_sum(3, 5)
    print(result)

    find_largest_element([8, 1, -3, 2, 0])

    # >>TODO: Python是动态语言，参数可以接受任意类型
    print(my_sum([1, 2], [3, 4]))
    print(my_sum('Hello', 'World'))
