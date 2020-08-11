def my_decorator(func):
    def wrapper():
        print('wrapper of decorator')
        func()

    return wrapper


def greet():
    print('hello, world')


if __name__ == '__main__':
    greet = my_decorator(greet)
    greet()
