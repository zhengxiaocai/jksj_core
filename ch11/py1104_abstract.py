"""
知识点：
1.抽象类的定义： class Name(metaclass=ABCMeta):
                @abstractmethod
2.抽象类无法实例化
3.继承了抽象类的类，必须实现所有的abstractmethod
"""
from abc import ABCMeta, abstractmethod


class Entity(metaclass=ABCMeta):
    @abstractmethod
    def get_title(self):
        pass

    @abstractmethod
    def set_title(self, title):
        pass


class Document(Entity):
    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title


if __name__ == '__main__':
    document = Document()
    document.set_title('Harry Potter')
    print(document.get_title())

    entity = Entity()
