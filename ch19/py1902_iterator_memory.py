import os
import psutil


def show_memory_info(hint):
    pid = os.getpid()
    p = psutil.Process(pid)

    info = p.memory_full_info()
    memory = info.uss / 1024 / 1024
    print('{} memory used: {} MB'.format(hint, memory))


def test_iterator():
    show_memory_info('initing iterator')
    list_1 = [i for i in range(1000000)]
    show_memory_info('after iterator initiated')
    print(sum(list_1))
    show_memory_info('after sum called')


def test_generator():
    show_memory_info('initing generator')
    list_2 = (i for i in range(1000000))
    show_memory_info('after generator initiated')
    print(sum(list_2))
    show_memory_info('after sum called')


if __name__ == '__main__':
    test_iterator()
    test_generator()