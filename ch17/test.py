import functools


def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('wrapper of decorator')
        return func(*args, **kwargs)

    return wrapper


@my_decorator
def example1():
    print('example1')


@my_decorator
def example2():
    return 'Hello, world!'


if __name__ == '__main__':
    example1()
    print(example2())
