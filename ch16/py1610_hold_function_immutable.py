# >>TODO: 用装饰器的函数，还是原来的函数吗？
from functools import wraps


def my_decorator(func):
    def wrapper(*args, **kwargs):
        print('wrapper of decorator')
        func(*args, **kwargs)

    return wrapper


def my_decorator2(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('@wraps of decorator')
        func(*args, **kwargs)

    return wrapper


@my_decorator
def greet(message):
    print('Hello, {}'.format(message))


@my_decorator2
def greet2(message):
    print('Hi, {}!'.format(message))


if __name__ == '__main__':
    # 装饰器的这个，已经不是原来那个函数了，而是wrapper
    print(greet.__name__)
    help(greet)

    # 为了避免这一情况，需要用自带装饰器@functools.wraps(func)
    print(greet2.__name__)
    help(greet2)
