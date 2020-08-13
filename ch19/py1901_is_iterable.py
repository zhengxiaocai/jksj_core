from collections.abc import Iterable


def is_iterable(obj):
    try:
        # >>TODO: 如果obj是可迭代对象，iter(obj)会返回一个迭代器，否则TypeError
        iter(obj)
        return True
    except TypeError:
        return False


def is_iterable2(obj):
    return isinstance(obj, Iterable)


if __name__ == '__main__':
    params = [1234, '1234', [1, 2, 3, 4], set([1, 2, 3, 4]), {1: 1, 2: 2, 3: 3, 4: 4}, (1, 2, 3, 4)]
    for i in params:
        print('{} is iterable? {}'.format(repr(i), is_iterable(i)))

    print('=' * 30)

    for i in params:
        print('{} is iterable? {}'.format(repr(i), is_iterable2(i)))
