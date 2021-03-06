"""
知识点：
1.类定义，没有继承关系的话 class Name:
2.双下划线开头的是私有
3.要定义实例属性，需要在__init__先声明下
"""


class Document:
    def __init__(self, title, author, context):
        print('init function called')
        self.title = title
        self.author = author
        self.__context = context
        self.page_num = 0

    def get_context_length(self):
        return len(self.__context)

    def intercept_context(self, length):
        self.__context = self.__context[:length]

    def set_page_num(self, page_num):
        self.page_num = page_num


if __name__ == '__main__':
    harry_potter_book = Document('Harry Potter', 'J.K Rowling',
                                 '... Forever Do not believe any thing is capable of thinking independently ...')

    print(harry_potter_book.title)
    print(harry_potter_book.author)
    print(harry_potter_book.get_context_length())

    harry_potter_book.intercept_context(10)

    print(harry_potter_book.get_context_length())

    # 私有属性不允许在类外访问
    # print(harry_potter_book.__context)

    # >>TODO: 类，一群有着相同属性和方法的对象的集合
