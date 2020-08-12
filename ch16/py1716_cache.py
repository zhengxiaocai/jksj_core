# >>TODO: @functools.lru_cache 会缓存相同的参数 返回
from functools import lru_cache
import time


@lru_cache
def example(message):
    time.sleep(3)
    return message


if __name__ == '__main__':
    start1 = time.perf_counter_ns()
    example('hello')
    end1 = time.perf_counter_ns()
    print('first: {}'.format(end1 - start1))

    start2 = time.perf_counter_ns()
    example('hello')
    end2 = time.perf_counter_ns()
    print('second: {}'.format(end2 - start2))
