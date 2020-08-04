def is_continuity(l):
    return all([x - i == l[0] for i, x in enumerate(l)])


if __name__ == '__main__':
    list01 = [1, 2, 3, 4]
    list02 = [2, 3, 5]
    print(is_continuity(list01))
    print(is_continuity(list02))
