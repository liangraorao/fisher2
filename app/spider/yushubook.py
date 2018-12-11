from app.models.base import db
from app.libs.httper import Http
from flask import current_app

from app.models.book import Book


class Yushubook:
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    key_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    def __init__(self):
        self.total = 0
        self.books = []

    def search_by_isbn(self, isbn):
        isbn_url = self.isbn_url.format(isbn)
        result = Http.get(isbn_url)

        # 从数据库查询是否有该书，如果没有，执行保存数据库，有的话跳过
        book = Book()
        res = Book.query.filter_by(isbn=result['isbn']).first()
        if res is None:
            book.set_attrs(result)
            db.session.add(book)
            db.session.commit()

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

    @property
    def first(self):
        return self.books[0] if self.total >= 1 else None

