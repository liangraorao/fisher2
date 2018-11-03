from httper import Http


class Yushubook:

    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    key_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    @classmethod
    def search_by_isbn(cls, isbn):
        isbn_url = cls.isbn_url.format(isbn)
        result = Http.get(isbn_url)
        return result

    @classmethod
    def search_by_key(cls, keyword, start=0, count=15):
        key_url = cls.key_url.format(keyword, count, start)
        result = Http.get(key_url)
        return result


