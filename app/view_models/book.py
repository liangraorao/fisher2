
class BookViewModel:
    def __init__(self, book):
        self.title = book['title']
        self.author = '、'.join(book['author'])
        self.publisher = book['publisher']
        self.image = book['image']
        self.price = book['price']
        self.summary = book['summary']
        self.pages = book['pages']
        self.isbn = book['isbn']

    @property
    def intro(self):
        intros = filter(lambda x: True if x else False,
                        [self.author, self.publisher, self.price])
        return ' | '.join(intros)


class BookCollection:
    def __init__(self):
        self.total = 0
        self.books = []
        self.keyword = ''

    def fill(self, yushu_book, keyword):
        self.total = yushu_book.total
        self.keyword = keyword
        self.books = [BookViewModel(book)for book in yushu_book.books]


class __BookViewModel:

    @classmethod
    def package_single(cls, data, keyword):
        returned = {
            "book": [],
            "total": 0,
            "keyword": keyword
        }
        if data:
            returned['total'] = 1
            returned['book'] = [cls.__cut_book_data(data)]
        return returned

    @classmethod
    def package_collection(cls, data, keyword):
        returned = {
            "book": [],
            "total": 0,
            "keyword": keyword
        }
        if data:
            returned['total'] = data['total']
            returned['book'] = [cls.__cut_book_data(book) for book in data['books']]
        return returned

    @classmethod
    def __cut_book_data(cls, data):
        res = {
            "author": '、'.join(data['author']),
            "publisher": data['publisher'],
            "summary": data['summary'],
            "title": data['title'],
            "price": data['price'],
            "pages": data['pages'] or '',
            "image": data['image'],
            'isbn': data['isbn']
        }
        return res

