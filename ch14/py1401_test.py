if __name__ == '__main__':
    l1 = [1, 2, 3]
    l2 = list(l1)
    l3 = l1
    l4 = l1[:]
    print(l1 == l2)
    print(l1 is l2)

    print(l1 == l3)
    print(l1 is l3)

    print(l1 == l4)
    print(l1 is l4)

    # >>TODO: == 是比较值是否相等；is 是比较址是否相等。

    a = 10
    b = 10

    print(a == b)

    print(id(a))
    print(id(b))

    print(a is b)

    c = 2570
    d = 2570

    print(c == d)

    print(id(c))
    print(id(d))

    print(c is d)

    # >>TODO: 检查是否是None时，用is。
    # >>TODO: is效率高于==，因为is不能被重载，执行is比较只是比较两个的id
    # >>TODO: 执行a==b相当于 a.__eq__(b)一般都会重写eq方法，比如list会比较值和顺序

    # >>TODO: 注意可变与不可变。
    t1 = (1, 2, [3, 4])
    t2 = (1, 2, [3, 4])
    print(t1 == t2)

    t1[-1].append(5)
    print(t1 == t2)
