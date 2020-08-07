# >>TODO: deepcopy定义：分配一块新的内存，创建一个新的对象，并将原来对象中的元素，
# >>TODO:    已递归的方式，通过创建新的子对象拷贝到新对象中
import copy

if __name__ == '__main__':
    l1 = [[1, 2], (30, 40)]
    l2 = copy.deepcopy(l1)
    l1.append(100)
    l1[0].append(3)

    print(l1)
    print(l2)

    # >>TODO: 如果copy对象中存在指向自身的引用，则会陷入无限循环
    x = [1]
    x.append(x)

    print(x)

    y = copy.deepcopy(x)
    print(y)

    # print(x == y)
