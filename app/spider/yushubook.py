from app.libs.httper import Http
from flask import current_app

class Yushubook:
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    key_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    @classmethod
    def search_by_isbn(cls, isbn):
        isbn_url = cls.isbn_url.format(isbn)
        result = Http.get(isbn_url)
        return result

    @classmethod
    def search_by_key(cls, keyword, page):
        key_url = cls.key_url.format(keyword, current_app.config['PER_PAGE'], cls.calculate_start(page))
        result = Http.get(key_url)
        return result

    @staticmethod
    def calculate_start(page):
        return (page-1) * current_app.config['PER_PAGE']