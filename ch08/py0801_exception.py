import sys

if __name__ == '__main__':
    # 异常
    # 10 / 0
    # ZeroDivisionError

    # order * 2
    # NameError

    # 1 + [1, 2]
    # TypeError

    try:
        s = input('Please enter two numbers separated by comma:')
        num1 = int(s.split(',')[0].strip())
        num2 = int(s.split(',')[1].strip())
    # except (ValueError, IndexError) as e:
    #     print('ValueError : {}'.format(e))
    except ValueError as e:
        print('ValueError : {}'.format(e))
    except IndexError as e:
        print('IndexError : {}'.format(e))
    except Exception as e:  # 等同于，啥也不写
        print('Other Error : {}'.format(e))

    # >>TODO:多个except只会执行一个

    print('continue')

    try:
        f = open('file.txt', 'r')
    except OSError as e:
        print('Os Error: {}'.format(e))
    except:
        print('Unexpect Error:', sys.exc_info()[0])
    finally:    # 无论如何都会执行
        f.close()

    # 处理文件，还是用with open
