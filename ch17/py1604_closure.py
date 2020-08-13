# >>TODO: 4）函数的返回值可以是函数对象，闭包 closure


def func_closure():
    def get_message(message):
        return 'Got a message: {}'.format(message)

    return get_message


if __name__ == '__main__':
    send_message = func_closure()
    print(send_message('Hello, world'))
