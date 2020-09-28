import string
import random


def get_username():
    min_length = 6
    max_length = 16

    username_seed = string.digits + string.ascii_letters + string.punctuation
    return ''.join([random.choice(username_seed) for i in range(random.randint(min_length, max_length))])


if __name__ == '__main__':
    print(string.digits)
    print(string.ascii_letters)
    print(string.punctuation)

    for i in range(10):
        print(get_username())
