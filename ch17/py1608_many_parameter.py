# >>TODO: Python中不存在函数重载，只看方法名，同名后边会覆盖掉前边。
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print('wrapper of decorator')
        func(*args, **kwargs)

    return wrapper


@my_decorator
def greet(message):
    print('hello: {}'.format(message))


@my_decorator
def g(name, message):
    print('{}, {}'.format(message, name))


if __name__ == '__main__':
    greet('world')
    g('Tom', 'Hi')
