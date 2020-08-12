# >>TODO: 多个装饰器，由内到外执行，最后函数执行。
import functools


def my_decorator1(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('execute decorator1')
        func(*args, **kwargs)

    return wrapper


def my_decorator2(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('execute decorator2')
        func(*args, **kwargs)

    return wrapper


@my_decorator1
@my_decorator2
def example():
    print('Hello, world!')


if __name__ == '__main__':
    example()
