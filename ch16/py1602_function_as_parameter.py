# >>TODO: 2）函数可以作为参数


def get_message(message):
    return 'Got a message: {}'.format(message)


def root_call(func, message):
    print(func(message))


if __name__ == '__main__':
    root_call(get_message, 'hello, world')
