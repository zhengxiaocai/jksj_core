class MyInputError(Exception):
    """Exception raised when there're errors in input"""

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return '{} is invalid input'.format(repr(self.value))


if __name__ == '__main__':
    try:
        raise MyInputError(1)
    except MyInputError as e:
        print('error: {}'.format(e))
