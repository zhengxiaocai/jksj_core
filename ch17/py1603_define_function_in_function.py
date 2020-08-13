# >>TODO: 3）在函数中定义函数


def func(message):
    def get_message(msg):
        return 'Got a message: {}'.format(msg)
    return get_message(message)


if __name__ == '__main__':
    print(func('Hello, world'))