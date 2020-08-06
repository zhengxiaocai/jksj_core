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
