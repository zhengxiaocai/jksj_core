def get_sum(a, b):
    return a + b


print('testing')
print('{} + {} = {}'.format(1, 2, get_sum(1, 2)))

if __name__ == '__main__':
    print('main')

    # >>TODO: 直接在开头写和main优先级相同，谁先执行要看顺序。
    # >>TODO: import导入文件时，会把暴露在外边的先执行下
    # >>TODO: __name__作为Python的内置魔法属性，import时，会被赋值为模块的名称，不等于__main__
