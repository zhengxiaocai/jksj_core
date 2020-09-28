import json

if __name__ == '__main__':
    s01 = {'a': 1, 'b': 2, 'c': '我'}
    d01 = json.dumps(s01)
    print(d01)

    """
    json序列化的时候，遇到中文会转换为Unicode
    """
