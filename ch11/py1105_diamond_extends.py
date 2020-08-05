"""
菱形继承
爷  父   子
    b
a       d
    c
使用super().__init__() 可以保证爷类只调用一次
"""


class A:
    def __init__(self):
        print('Enter A')
        print('Leave A')


class B(A):
    def __init__(self):
        print('Enter B')
        super().__init__()
        print('Leave B')


class C(A):
    def __init__(self):
        print('Enter C')
        super().__init__()
        print('Leave C')


class D(B, C):
    def __init__(self):
        print('Enter D')
        super().__init__()
        print('Leave D')


if __name__ == '__main__':
    D()
