from flask import jsonify, request
from app.libs.helper import is_isbn_or_key
from app.spider.yushubook import Yushubook
from . import web
from app.form.book import SearchForm
from app.view_models.book import BookCollection
import json

@web.route('/book/search')
def search():
    form = SearchForm(request.args)
    books = BookCollection()

    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        yushu_book = Yushubook()

        if isbn_or_key == 'isbn':
            yushu_book.search_by_isbn(q)
        else:
            yushu_book.search_by_key(q, page)

        books.fill(yushu_book, q)
        # 对象不可以被序列化
        # return jsonify(books)
        return json.dumps(books, default=(lambda o: o.__dict__))
    else:
        return jsonify(form.errors)
