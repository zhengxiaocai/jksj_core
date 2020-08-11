# >>TODO: 相比于传入，可以直接用@


def my_decorator(func):
    def wrapper():
        print('wrapper of decorator')
        func()

    return wrapper


@my_decorator
def greet():
    print('hello, world')


if __name__ == '__main__':
    greet()
