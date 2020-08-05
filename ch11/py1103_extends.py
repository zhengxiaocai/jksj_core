"""
知识点：
1.继承的写法 class Name(subName)：
2.子类在构造函数里，需要显式的调用父类的构造方法，一般用super().__init__(**kw)，无self
3.构造器执行顺序 先子类后父类
"""


class Entity:
    def __init__(self, object_type):
        print('parent class init called')
        self.object_type = object_type

    def get_context_length(self):
        raise Exception('get_context_length not implemented')

    def print_title(self):
        print(self.title)


class Document(Entity):
    def __init__(self, title, author, context):
        print('Document class init called')
        super().__init__('Document')
        self.title = title
        self.author = author
        self.__context = context

    def get_context_length(self):
        return len(self.__context)


class Video(Entity):
    def __init__(self, title, author, video_length):
        print('Video class init called')
        super().__init__('Video')
        self.title = title
        self.author = author
        self.__video_length = video_length

    def get_context_length(self):
        return self.__video_length


if __name__ == '__main__':
    harry_potter_book = Document('Harry Potter', 'J.K Rowling',
                                 '... Forever Do not believe any thing is capable of thinking independently ...')
    harry_potter_video = Video('Harry Potter', 'J.K Rowling', 120)

    print(harry_potter_book.object_type)
    print(harry_potter_video.object_type)

    print(harry_potter_book.title)
    print(harry_potter_video.title)

    print(harry_potter_book.get_context_length())
    print(harry_potter_video.get_context_length())

    harry_potter_book.print_title()
