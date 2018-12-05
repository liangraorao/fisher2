from flask import jsonify, request,render_template, flash
from app.libs.helper import is_isbn_or_key
from app.spider.yushubook import Yushubook
from . import web
from app.form.book import SearchForm
from app.view_models.book import BookCollection, BookViewModel
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
        # return json.dumps(books, default=(lambda o: o.__dict__))

    else:
        flash('搜索的关键字不符合要求，请重新输入')
        # return jsonify(form.errors)
    return render_template('search_result.html', books=books)


@web.route('/book/<isbn>/detail')
def book_detail(isbn):
    yushu_book = Yushubook()
    yushu_book.search_by_isbn(isbn)
    book = BookViewModel(yushu_book.first)
    return render_template('book_detail.html', book=book, wishes=[], gifts=[])


@web.route('/test')
def test():
    r = {
        'name': '',
        'age': 16
    }
    r1= {

    }
    flash('flash消息闪现')
    # return jsonify(r)
    return render_template('test.html', data=r)