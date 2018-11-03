from flask import jsonify, request
from helper import is_isbn_or_key
from yushubook import Yushubook
from . import web
from app.form.book import SearchForm

@web.route('/search/book')
def search():
    form = SearchForm(request.args)
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == 'isbn':
            result = Yushubook.search_by_isbn(q)
        else:
            result = Yushubook.search_by_key(q)
        return jsonify(result)
    else:
        return jsonify(form.errors)
