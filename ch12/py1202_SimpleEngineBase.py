from ch12.py1201_SearchEngineBase import SearchEngineBase, main


class SimpleEngine(SearchEngineBase):
    def __init__(self):
        super().__init__()
        self.__id_to_text = {}

    def process_corpus(self, path_id, text):
        self.__id_to_text[path_id] = text

    def search(self, query):
        results = []
        for path_id, text in self.__id_to_text.items():
            if query in text:
                results.append(path_id)
        return results


if __name__ == '__main__':
    search_engine = SimpleEngine()
    main(search_engine)
