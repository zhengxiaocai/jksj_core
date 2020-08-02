# >>TODO: 局部变量只在函数内部有效，一旦函数执行完毕，局部变量就会回收
# >>TODO: MIN MAX 是全局变量，在当前文件中任何地方都可以访问

MIN_VALUE = 1
MAX_VALUE = 10


def update_global_direct():
    # >>TODO: 直接这样去改会被认为是局部变量
    # MIN_VALUE += 1
    pass


def update_global():
    # >>TODO: 如果要改，需要用global声明
    global MIN_VALUE, MAX_VALUE
    MIN_VALUE += 1


def local_cover_global():
    # >>TODO: 如果局部变量跟全局变量同名，局部会覆盖全局
    MAX_VALUE = 3


def validation_check(value):
    if value < MIN_VALUE or value > MAX_VALUE:
        raise Exception('validation check fails')


def read_text_from_file(file_path):
    # >>TODO: 该局部变量file只在当前函数内有效。
    with open(file_path) as file:
        pass


if __name__ == '__main__':
    update_global()
