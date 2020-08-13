# >>TODO: 输入合法性校验
import functools


def validation_check(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if len(args[0]) > 5:
            return func(*args, **kwargs)
        else:
            raise Exception('Validation Exception')

    return wrapper


@validation_check
def example(message):
    print(message)


if __name__ == '__main__':
    example('Hello, world!')
    # example('hello')
