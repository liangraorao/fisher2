from flask import jsonify, request
from app.libs.helper import is_isbn_or_key
from app.spider.yushubook import Yushubook
from . import web
from app.form.book import SearchForm
from app.view_models.book import BookViewModel


@web.route('/book/search')
def search():
    form = SearchForm(request.args)
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == 'isbn':
            result = Yushubook.search_by_isbn(q)
            result = BookViewModel.package_single(result, q)
        else:
            result = Yushubook.search_by_key(q, page)
            result = BookViewModel.package_collection(result, q)

        return jsonify(result)
    else:
        return jsonify(form.errors)
