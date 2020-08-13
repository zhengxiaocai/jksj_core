# >>TODO: 类装饰器，用__call__()
class Count:
    def __init__(self, func):
        self.func = func
        self.num_call = 0

    def __call__(self, *args, **kwargs):
        self.num_call += 1
        print('num of call is {}'.format(self.num_call))
        return self.func(*args, **kwargs)

    def update_num(self):
        self.num_call += 1


@Count
def example():
    print('Hello, world!')


if __name__ == '__main__':
    example()
    example()

    count1 = Count(example)
    count2 = Count(example)
    count1.update_num()
    print(count1.num_call)
    print(count2.num_call)
