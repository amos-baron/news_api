from news_report import NewsReport
import bs4
import urllib.request


class YnetReport(NewsReport):
    def __init__(self, article):
        self.url = f"https://www.ynet.co.il/news/article/{article}"
        self.source = urllib.request.urlopen(self.url)
        self._soup = bs4.BeautifulSoup(self.source, 'html.parser')

    def get_raw_html(self):
        return self.source

    def get_description(self):
        description = self._get_object('div', 'class', 'subTitleWrapper')
        return ''.join(description)

    def get_headline(self):
        headlines = self._get_object('div', 'class', 'mainTitleWrapper')
        return ''.join(headlines)

    def get_text(self):
        paragraphs = self._get_object('span', 'data-text', 'true')
        return ''.join(paragraphs)

    def _get_object(self, container: str, key: str, value: str):
        objects = [obj.get_text() for obj in self._soup.find_all(container, {key: value})]
        return objects
