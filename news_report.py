from abc import abstractmethod

class NewsReport:
    def __init__(self, article):
        pass

    @classmethod
    def version(self): return "1.0"

    @abstractmethod
    def get_raw_html(self): raise NotImplementedError

    @abstractmethod
    def get_headline(self): raise NotImplementedError

    @abstractmethod
    def get_text(self): raise NotImplementedError
