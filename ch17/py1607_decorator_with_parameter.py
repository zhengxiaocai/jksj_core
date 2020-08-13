def my_decorator(func):
    def wrapper(msg):
        print('wrapper of decorator')
        func(msg)

    return wrapper


@my_decorator
def greet(message):
    print('hello, {}'.format(message))


if __name__ == '__main__':
    greet('Tom')
