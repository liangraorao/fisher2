from flask import jsonify
from helper import is_isbn_or_key
from yushubook import Yushubook
from . import web


@web.route('/search/book/<p>/<page>')
def search(p, page):
    isbn_or_key = is_isbn_or_key(p)
    if isbn_or_key == 'isbn':
        result = Yushubook.search_by_isbn(p)
    else:
        result = Yushubook.search_by_key(p)
    return jsonify(result)