import re
from ch12.py1201_SearchEngineBase import SearchEngineBase, main


class BOWEngine(SearchEngineBase):
    def __init__(self):
        super().__init__()
        self.__id_to_words = {}

    def process_corpus(self, path_id, text):
        self.__id_to_words[path_id] = self.parse_text_to_words(text)

    def search(self, query):
        query_words = self.parse_text_to_words(query)
        results = []
        for path_id, words in self.__id_to_words.items():
            if self.query_match(query_words, words):
                results.append(path_id)
        return results

    @staticmethod
    def query_match(query_words, words):
        for query_word in query_words:
            if query_word in words:
                return True

    @staticmethod
    def parse_text_to_words(text):
        # 使用正则去除标点符号和回车
        text = re.sub(r'[^\w]', ' ', text)
        # 转化为小写
        text = text.lower()
        # 根据空格分隔为单词列表
        word_list = text.split(' ')
        # 去除空
        word_list = filter(None, word_list)
        # 返回单词的set
        return set(word_list)


if __name__ == '__main__':
    bow_engine = BOWEngine()
    main(bow_engine)
