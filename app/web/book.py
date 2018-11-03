from flask import jsonify, Blueprint

from helper import is_isbn_or_key
from yushubook import Yushubook

web = Blueprint('web', __name__)


@web.route('/search/book/<p>')
def search(p):
    isbn_or_key = is_isbn_or_key(p)
    if isbn_or_key == 'isbn':
        result = Yushubook.search_by_isbn(p)
    else:
        result = Yushubook.search_by_key(p)
    return jsonify(result)