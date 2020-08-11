# >>TODO: 1）函数可以赋值


def func(message):
    print('Got a message: {}'.format(message))


if __name__ == '__main__':
    send_message = func
    send_message('hello, world')
