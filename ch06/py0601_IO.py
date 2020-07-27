if __name__ == '__main__':
    # 键盘输入
    name = input('your name:')
    gender = input('you are a boy? y/n')

    welcome_str = 'Welcome to the matrix {prefix} {name}.'
    welcome_dict = {
        'name': name,
        'prefix': 'Mr.' if gender == 'y' else 'Mrs'
    }

    print('Authorizing...')
    print(welcome_str.format(**welcome_dict))
    print(welcome_str.format(prefix='Mr.', name='Jason'))
