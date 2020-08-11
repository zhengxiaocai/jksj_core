# >>TODO: 带自定义参数的装饰器，在外边再包一层


def repeat(n):
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                print('wrapper of decorator')
                func(*args, **kwargs)

        return wrapper

    return my_decorator


@repeat(4)
def greet(message):
    print(message)


if __name__ == '__main__':
    greet('Hello, World!')
