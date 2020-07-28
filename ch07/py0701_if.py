if __name__ == '__main__':
    # y = |x|
    x = 9
    if x < 0:
        y = -x
    else:
        y = x

    # elif
    if x == 0:
        print('red')
    elif x == 1:
        print('yellow')
    else:
        print('green')

    """
    判断条件的省略用法，可以省略，但是不鼓励
    String      空字符串解析成False，其余为True
    int         0解析成False，其余为True
    Bool        False，True
    list|tuple|dict|set     空为False，其余为True
    Object      None为False，其余为True
    """
