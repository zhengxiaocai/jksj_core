# >>TODO: 浅拷贝带来的问题，无法完整拷贝一个对象。
# >>TODO: 浅copy的元素是对原对象元素的引用
import copy

if __name__ == '__main__':
    l1 = [[1, 2], (30, 40)]
    l2 = copy.copy(l1)
    l1.append(100)
    l1[0].append(3)

    print(l1)
    print(l2)

    l1[1] += (50, 60)
    print(l1)
    print(l2)
