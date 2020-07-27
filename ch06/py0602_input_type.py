# input(desc) input接收的永远是str
# 如果需要别的处理，需要先格式转换一下。格式转换考虑异常

if __name__ == '__main__':
    a = input('a=')
    b = input('b=')
    print('a + b = {}'.format(a + b))
    print('type of a is {}, type of b is {}'.format(type(a), type(b)))
    print('a + b = {}'.format(int(a) + int(b)))
