"""
知识点：
1.类属性 直接在外边定义，变量名为全大写
2.类函数 @classmethod(cls) 主要用cls创建不同的构造方法
3.静态函数 @staticmethod() 操作跟实例没啥关系的东西
4.类内用属性时，不能缺省self 类名
"""


class Document:
    WELCOME_STR = 'Welcome, The context for this book is {}'

    def __init__(self, title, author, context):
        print('init function called')
        self.title = title
        self.author = author
        self.__context = context

    # 类函数
    @classmethod
    def create_empty_book(cls, title, author):
        return cls(title=title, author=author, context='Nothing')

    # 成员函数
    def get_context_length(self):
        return len(self.__context)

    # 静态函数
    @staticmethod
    def get_welcome(context):
        return Document.WELCOME_STR.format(context)


if __name__ == '__main__':
    empty_book = Document.create_empty_book('Harry Potter', 'J.K. Rowling')

    print(empty_book.get_context_length())
    print(empty_book.get_welcome('indeed nothing'))
