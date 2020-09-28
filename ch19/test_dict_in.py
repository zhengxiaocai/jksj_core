if __name__ == '__main__':
    a = {'a': 1}
    c = {'a': 2}
    b = {'a': 1, 'b': 2}
    print(list(a.items())[0] in b.items())
    print(a.items())
    print(b.items())

    a = {"a": [1, 2]}
    b = {"a": [1, 2], "b": 2}
    print(list(a.items())[0] in b.items())

    a = {"a": [1, 2], 'b': 2}
    b = {"a": [1, 2], "b": 2}
    print(all(i in b.items() for i in list(a.items())))
