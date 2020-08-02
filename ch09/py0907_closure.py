# >>TODO: 闭包：嵌套函数，外部函数返回的是个函数
# >>TODO: 好处：清楚、直观；把不必要的放到外层，提升效率。


def nth_power(exponent):
    def exponent_of(base):
        return base ** exponent

    return exponent_of


if __name__ == '__main__':
    square = nth_power(2)
    cube = nth_power(3)
    print(square)
    print(cube)

    print(square(2))
    print(cube(2))
