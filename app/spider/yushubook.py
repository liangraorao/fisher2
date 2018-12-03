from app.libs.httper import Http
from flask import current_app


class Yushubook:
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    key_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    def __init__(self):
        self.total = 0
        self.books = []

    def search_by_isbn(self, isbn):
        isbn_url = self.isbn_url.format(isbn)
        result = Http.get(isbn_url)
        self.__fill_single(result)

    def search_by_key(self, keyword, page):
        key_url = self.key_url.format(keyword, current_app.config['PER_PAGE'], self.calculate_start(page))
        result = Http.get(key_url)
        self.__fill_collection(result)

    def __fill_single(self, data):
        if data:
            self.total = 1
            self.books.append(data)

    def __fill_collection(self, data):
        self.total = data['total']
        self.books = data['books']

    def calculate_start(self, page):
        return (page-1) * current_app.config['PER_PAGE']